import os, yaml, json,joblib, base64
from box.exceptions import BoxValueError
from box import ConfigBox
from pathlib import Path
from typing import Any
from Face_Recognition_System import logger
from ensure import ensure_annotations



@ensure_annotations
def read_yml(path_to_yml: Path)-> ConfigBox:
    """
    Docstring for read_yml
    
    :param path_to_yml: Description
    :type path_to_yml: Path
    :return: Description
    :rtype: ConfigBox
    """
    try:
        with open(path_to_yml) as yml_file:
            content = yaml.safe_load(yml_file)

            logger.info(f"Yaml file: {path_to_yml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_directories:list):
    """
    Docstring for create_directories
    
    :param path_directories: Description
    :type path_directories: list
    """
    for path in path_directories:
        os.makedirs(path, exist_ok=True)
        if True:
            logger.info(f"Created directory at :{path}")


@ensure_annotations
def save_json(path:Path, data: dict):
    """
    Docstring for save_json
    
    :param path: Description
    :type path: Path
    :param data: Description
    :type data: dict 
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved at : {path}")



@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """
     for load_json files data
    
    :param path: Description
    :type path: Path
    :return: Description
    :rtype: ConfigBox
    """

    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Docstring for save_bin
    
    :param data: Description
    :type data: Any
    :param path: Description
    :type path: Path
    """
    try:
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at : {path}")
    except Exception as e:
        logger.error(f"Error {e}! File binary not saved at : {path}")


@ensure_annotations
def load_bin(path: Path)-> Any:
    """
    Docstring for load_bin
    
    :param path: Description
    :type path: Path
    :return: Description
    :rtype: Any
    """
    data = joblib.load(path)
    logger.info(f"File loaded from :{path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Docstring for get_size
    
    :param path: Description
    :type path: Path
    :return: Description
    :rtype: str
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


""" FOr image"""
def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageInotBase64(ImagePath):
    with open(ImagePath, "rb") as f:
        return base64.b64encode(f.read())