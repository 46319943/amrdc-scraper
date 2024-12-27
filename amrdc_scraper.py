import json
import os
import requests
from pathlib import Path
from tqdm import tqdm

class AMRDCScraper:
    BASE_URL = "https://amrdcdata.ssec.wisc.edu/api/3/action"
    
    def __init__(self, output_dir="downloaded_data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
    def get_dataset_list(self):
        """Fetch list of all datasets and filter for quality-controlled ones."""
        response = requests.get(f"{self.BASE_URL}/package_list")
        response.raise_for_status()
        
        all_datasets = response.json()["result"]
        return [ds for ds in all_datasets if "quality-controlled" in ds]
    
    def get_dataset_info(self, dataset_name):
        """Fetch detailed information for a specific dataset."""
        response = requests.get(
            f"{self.BASE_URL}/package_show",
            params={"id": dataset_name}
        )
        response.raise_for_status()
        return response.json()["result"]
    
    def download_file(self, url, output_path):
        """Download a file with progress bar."""
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        with open(output_path, 'wb') as f:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=output_path.name) as pbar:
                for data in response.iter_content(block_size):
                    f.write(data)
                    pbar.update(len(data))
    
    def download_dataset(self, dataset_name, dataset_number, total_datasets):
        """Download a complete dataset including metadata and resources."""
        print(f"\nProcessing dataset [{dataset_number}/{total_datasets}]: {dataset_name}")
        
        # Create dataset directory
        dataset_dir = self.output_dir / dataset_name
        dataset_dir.mkdir(exist_ok=True)
        
        # Get and save metadata
        dataset_info = self.get_dataset_info(dataset_name)
        meta_path = dataset_dir / "meta.json"
        with open(meta_path, 'w') as f:
            json.dump(dataset_info, f, indent=2)
        
        # List all files to be downloaded
        resources_to_download = [
            resource for resource in dataset_info.get("resources", [])
            if resource.get("url") and resource.get("mimetype") != "application/zip"
        ]
        
        if not resources_to_download:
            print("No eligible files to download in this dataset")
            return
        
        print(f"\nFiles to be downloaded for {dataset_name}:")
        for idx, resource in enumerate(resources_to_download, 1):
            filename = resource.get("name") or Path(resource["url"]).name
            print(f"{idx}. {filename} (Type: {resource.get('mimetype', 'unknown')})")
        
        # Download resources
        for resource in resources_to_download:
            url = resource["url"]
            filename = resource.get("name") or Path(url).name
            output_path = dataset_dir / filename
            
            if output_path.exists():
                print(f"Skipping existing file: {filename}")
                continue
            
            try:
                self.download_file(url, output_path)
            except Exception as e:
                print(f"Error downloading {filename}: {str(e)}")
    
    def run(self):
        """Main execution method."""
        # Get list of quality-controlled datasets
        datasets = self.get_dataset_list()
        total_datasets = len(datasets)
        print(f"Found {total_datasets} quality-controlled datasets")
        
        # Create progress bar for overall dataset progress
        with tqdm(total=total_datasets, desc="Overall Progress", unit="dataset") as pbar:
            # Download each dataset
            for idx, dataset_name in enumerate(datasets, 1):
                try:
                    self.download_dataset(dataset_name, idx, total_datasets)
                except Exception as e:
                    print(f"Error processing dataset {dataset_name}: {str(e)}")
                finally:
                    pbar.update(1)
        
        print("\nDownload process completed!") 