import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        pd.to_pickle(obj, file_path)
        logging.info(f"Object saved to {file_path}")
    except Exception as e:
        raise CustomException(e, sys)