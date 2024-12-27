# AMRDC 数据抓取工具

一个基于Python的工具，用于使用CKAN API从北极和南极气象研究数据中心（AMRDC）下载质量控制数据集。该工具自动过滤和下载数据集，并将其组织成结构化格式，便于访问和管理。

## 主要特点

- 🔍 自动过滤质量控制数据集
- 📁 为每个数据集创建独立目录
- 📊 保存数据集元数据
- 🚫 跳过ZIP文件下载
- 📈 显示实时下载进度
- ↩️ 支持断点续传
- 🔄 跳过已存在的文件以避免重复

## 安装说明

### 环境要求

- Python 3.10 或更高版本
- Conda 包管理器

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/amrdc-scraper.git
cd amrdc-scraper
```

2. 创建Conda环境：
```bash
conda env create -f environment.yml
```

3. 激活环境：
```bash
conda activate amrdc-scraper
```

## 使用方法

运行抓取工具：
```bash
python main.py
```

### 工作原理

1. **数据集发现**：
   - 连接到AMRDC CKAN API
   - 获取所有可用数据集列表
   - 筛选包含"quality-controlled"的数据集

2. **下载过程**：
   - 为每个数据集创建目录
   - 将数据集元数据保存为`meta.json`
   - 下载所有相关文件（不包括ZIP文件）
   - 显示整体下载和单个文件的进度

3. **输出组织结构**：
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

### 进度跟踪

工具提供实时反馈：
- 找到的数据集总数
- 当前正在处理的数据集
- 每个数据集要下载的文件列表
- 单个文件下载进度
- 整体下载进度

## 输出示例

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

## 贡献指南

欢迎贡献！以下是参与方式：

1. Fork 仓库
2. 创建新分支 (`git checkout -b feature/improvement`)
3. 提交更改
4. 提交代码 (`git commit -am '添加新功能'`)
5. 推送到分支 (`git push origin feature/improvement`)
6. 创建 Pull Request

请确保您的代码遵循现有的代码风格并包含适当的测试。

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

- 数据由北极和南极气象研究数据中心（AMRDC）提供
- 使用 CKAN API 构建

## 注意事项

本工具仅用于研究目的，使用时请遵守AMRDC的服务条款和数据使用政策。 