import yaml
import os
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_name: Path) -> ConfigBox:
    try:
        with open(path_name) as file:
            yaml_file=yaml.safe_load(file)
            logger.info(f"yaml file  from these path {path_name} successfully loaded")

            return ConfigBox(yaml_file)
    except BoxValueError:
        raise ValueError("yaml file is emty")
    except Exception as e:
        raise e
        

@ensure_annotations

def create_directories(path_to_directories: list, verbose=True):

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"successfully created directory at :{path}")


@ensure_annotations

def save_json(path: Path, data: dict):

    with open(path,"w") as file:
        json.dump(data,file,indent=4)
    logger.info(f"converted to json {path}")


@ensure_annotations

def load_json(path: Path) -> ConfigBox:

    with open(path) as file:
        content=json.load(file)

        logger.info(f"successfully json data loaded {path}")

        return ConfigBox(content)



@ensure_annotations
def save_bin(data: Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"file saved at {path}")



@ensure_annotations
def load_bin(path: Path) -> Any:

    content=joblib.load(path)
    logger.info(f"file is loaded from {path}")

    return content




