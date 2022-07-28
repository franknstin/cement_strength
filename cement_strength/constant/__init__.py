import os
from datetime import datetime


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


ROOT_DIR = os.getcwd()
CONFIG_DIR = 'config'
CONFIG_FILE_NAME = 'config.yaml'
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)


CURRENT_TIME_STAMP = get_current_time_stamp()


DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_ARTIFACT_DIR_KEY = 'data_ingestion'
RAW_DATA_DIR_KEY = 'raw_data_dir'
TGZ_DOWNLOAD_DIR_KEY = 'tgz_download_dir'
INGESTED_DIR_KEY = 'ingested_dir'
INGESTED_TRAIN_DIR_KEY='ingested_train_dir'
INGESTED_TEST_DIR_KEY='ingested_test_dir'
DATASET_DOWNLOAD_URL_KEY = 'dataset_download_url'



TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY = 'training_pipeline_name'
ARTIFACT_DIR_KEY = 'artifact_dir'

DATA_VALIDATION_CONFIG_KEY = 'data_validation_config'
DATA_VALIDATION_DIR_KEY = 'data_validation'
SCHEMA_DIR_KEY = 'schema_dir'
SCHEMA_FILE_NAME_KEY = 'schema_file_name'
REPORT_FILE_NAME_KEY = 'report_file_name'
REPORT_PAGE_FILE_NAME_KEY = 'report_page_file_name'



DATA_TRANSFORMATION_ARTIFACT_DIR = "data_transformation"
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_DIR_NAME_KEY = "transformed_dir"
DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY = "transformed_train_dir"
DATA_TRANSFORMATION_TEST_DIR_NAME_KEY = "transformed_test_dir"
DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY = "preprocessing_dir"
DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY = "preprocessed_object_file_name"


MODEL_TRAINER_CONFIG_INFO_KEY = 'model_trainer_config'
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
TRAINED_MODEL_DIR_KEY = 'trained_model_dir'
MODEL_FILE_NAME_KEY = 'model_file_name'
MODEL_CONFIG_DIR_KEY = 'model_config_dir'
MODEL_CONFIG_FILENAME_KEY = 'model_config_file_name'
BASE_ACCURACY_KEY = 'base_accuracy'


MODEL_EVALUATION_ARTIFACT_KEY = 'model_evaluation'
MODEL_EVALUATION_CONFIG_KEY = 'model_evaluation_config'
MODEL_EALUATION_FILE_NAME_KEY = 'model_evaluation_file_name'


MODEL_PUSHER_CONFIG_KEY = 'model_pusher_config'
MODEL_EXPORT_DIR_KEY = 'model_export_dir'


COLUMN_KEY = 'columns'
TARGET_COLUMN_KEY = 'target_column'

