# AMRDC Data Scraper

A Python-based tool for downloading quality-controlled datasets from the Arctic and Antarctic Meteorological Research Data Center (AMRDC) using their CKAN API. This tool automatically filters and downloads datasets, organizing them into a structured format for easy access and management.

## Key Features

- 🔍 Automatically filters for quality-controlled datasets
- 📁 Downloads each dataset into its own directory
- 📊 Saves metadata for each dataset
- 🚫 Skips ZIP file downloads
- 📈 Shows real-time download progress
- ↩️ Resumes interrupted downloads
- 🔄 Skips existing files to avoid duplicates

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Conda package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/amrdc-scraper.git
cd amrdc-scraper
```

2. Create the Conda environment:
```bash
conda env create -f environment.yml
```

3. Activate the environment:
```bash
conda activate amrdc-scraper
```

## Usage

Run the scraper using:
```bash
python main.py
```

### How it Works

1. **Dataset Discovery**: 
   - Connects to the AMRDC CKAN API
   - Retrieves a list of all available datasets
   - Filters for datasets containing "quality-controlled" in their names

2. **Download Process**:
   - Creates a directory for each dataset
   - Saves dataset metadata as `meta.json`
   - Downloads all associated files (excluding ZIP files)
   - Shows progress for both overall downloads and individual files

3. **Output Organization**:
   ```
   downloaded_data/
   ├── dataset-name-1/
   │   ├── meta.json
   │   ├── data_file1.nc
   │   └── data_file2.csv
   ├── dataset-name-2/
   │   ├── meta.json
   │   └── data_file1.nc
   └── ...
   ```

### Progress Tracking

The tool provides real-time feedback on:
- Total number of datasets found
- Current dataset being processed
- List of files to be downloaded for each dataset
- Individual file download progress
- Overall download progress

## Example Output

```
Found 50 quality-controlled datasets
Overall Progress: 100%|██████████| 50/50 [02:30<00:00,  3.00s/dataset]

Processing dataset [1/50]: dataset-name-here

Files to be downloaded for dataset-name-here:
1. file1.nc (Type: application/x-netcdf)
2. file2.csv (Type: text/csv)
3. file3.txt (Type: text/plain)

Downloading file1.nc: 100%|██████████| 50MB/50MB [00:30<00:00, 1.67MB/s]
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Data provided by the Arctic and Antarctic Meteorological Research Data Center (AMRDC)
- Built using the CKAN API

## Note

This tool is designed for research purposes and should be used in accordance with AMRDC's terms of service and data usage policies.
