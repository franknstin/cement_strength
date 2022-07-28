from sklearn import datasets
import yaml
import sys, os
from cement_strength.exception import CementException
import pandas as pd
from cement_strength.constant import *
import numpy as np
import dill


def read_yaml_file(file_path:str)-> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise CementException(e,sys)


def load_data(file_path:str, schema_file_path:str) -> pd.DataFrame:
    
    """
    file_path: str
    """
    try:
        dataset_schema = read_yaml_file(schema_file_path)

        schema = dataset_schema[COLUMN_KEY]

        dataset = pd.read_csv(file_path)

        error_message = ""


        for column in dataset.columns:
            if column in list(schema.keys()):
                dataset[column].astype(schema[column])
            else:
                error_message = f"{error_message} \nColumn: [{column}] is not in the schema."

        if len(error_message) > 0:
            raise Exception(error_message)

        return dataset

    except Exception as e:
        raise CementException(e,sys)

def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise CementException(e, sys) from e


def save_object(file_path:str,obj):
    """
    file_path: str
    obj: Any sort of object
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e,sys) from e