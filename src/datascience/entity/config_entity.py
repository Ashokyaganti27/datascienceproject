
from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path



@dataclass
class DataValidationConfig():
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict
    


@dataclass
class DataTransformationConfig():
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerconfig():
    root_dir: Path
    train_datapath: Path
    test_datapath: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str









