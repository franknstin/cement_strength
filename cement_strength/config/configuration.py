from cement_strength.constant import *
from cement_strength.entity.config_entity import *
from cement_strength.constant import *
from cement_strength.util.util import read_yaml_file
from cement_strength.exception import CementException
import os, sys
from cement_strength.logger import logging




class Configuration:

    def __init__(self, config_file_path: str =  CONFIG_FILE_PATH, current_time_stamp = CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = read_yaml_file(file_path = config_file_path),
            self.time_stamp = current_time_stamp,
            self.training_pipeline_config = self.get_training_pipeline_config()
        except Exception as e:
            raise CementException(e, sys)
            

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        
        try:
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_inggestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR_KEY,
                self.time_stamp 
                )    

            dataset_download_url = data_ingestion_info[DATASET_DOWNLOAD_URL_KEY]

            raw_data_dir = os.path.join(
                data_inggestion_artifact_dir,
                data_ingestion_info[RAW_DATA_DIR_KEY]
                )

            tgz_download_dir = os.path.join(
                data_inggestion_artifact_dir,
                data_ingestion_info[TGZ_DOWNLOAD_DIR_KEY]
                )

            ingested_train_dir = os.path.join(
                data_inggestion_artifact_dir,
                data_ingestion_info[INGESTED_DIR_KEY],
                data_ingestion_info[INGESTED_TRAIN_DIR_KEY]
                )

            ingested_test_dir = os.path.join(
                data_inggestion_artifact_dir,
                data_ingestion_info[INGESTED_DIR_KEY],
                data_ingestion_info[INGESTED_TEST_DIR_KEY]
                )


            data_ingestion_config = DataIngestionConfig(
            dataset_download_url = dataset_download_url,
            raw_data_dir = raw_data_dir,
            tgz_download_dir = tgz_download_dir,
            ingested_train_dir = ingested_train_dir, 
            ingested_test_dir = ingested_test_dir
            )
            return data_ingestion_config

        except Exception as e:
            raise CementException(e, sys)

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.get_training_pipeline_config()

            data_validation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            data_validation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATION_DIR_KEY
                )

            schema_file_path = os.path.join(
                ROOT_DIR,
                data_validation_info[SCHEMA_DIR_KEY],
                data_validation_info[SCHEMA_FILE_NAME_KEY]
                )

            report_file_path = os.path.join(
                data_validation_artifact_dir,
                self.time_stamp,
                data_validation_info[REPORT_FILE_NAME_KEY]
                )

            report_page_file_path = os.path.join(
                data_validation_artifact_dir,
                self.time_stamp,
                data_validation_info[REPORT_PAGE_FILE_NAME_KEY]
                )


            data_validation_config = DataValidationConfig(
               schema_file_path = schema_file_path, 
               report_file_path = report_file_path, 
               report_page_file_path = report_page_file_path 
            )
            return data_validation_config
        except Exception as e:
            raise CementException(e, sys)
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir = self.get_training_pipeline_config()

            data_transformation_config_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            
            data_transformation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_DIR,
                self.time_stamp
                )

            
            
            preprocessed_object_file_path = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                data_transformation_config_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY]
            )

            
            transformed_train_dir = os.path.join(
            data_transformation_artifact_dir,
            data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
            data_transformation_config_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY]
            )


            transformed_test_dir = os.path.join(
            data_transformation_artifact_dir,
            data_transformation_config_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
            data_transformation_config_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY]

            )

            data_transformation_config = DataTransformationConfig( 
                transformed_train_dir = transformed_train_dir,
                transformed_test_dir = transformed_test_dir,
                preprocessed_object_file_path = preprocessed_object_file_path 
            )
            return data_transformation_config
        except Exception as e:
            raise CementException(e, sys)

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir

            model_trainer_config_info = self.config_info[MODEL_TRAINER_CONFIG_INFO_KEY]

            model_trainer_artifact_dir = os.path.join(
                artifact_dir,
                MODEL_TRAINER_ARTIFACT_DIR,
                self.time_stamp
                )

            trained_model_file_path = os.path.join(
                model_trainer_artifact_dir,
                model_trainer_config_info[TRAINED_MODEL_DIR_KEY],
                model_trainer_config_info[MODEL_FILE_NAME_KEY]
            )

            model_config_file_path = os.path.join(model_trainer_config_info[MODEL_CONFIG_DIR_KEY],
            model_trainer_config_info[MODEL_CONFIG_FILENAME_KEY])

            base_accuracy = model_trainer_config_info[BASE_ACCURACY_KEY]

            model_trainer_config = ModelTrainerConfig(
                trained_model_file_path = trained_model_file_path, 
                base_accuracy = base_accuracy,
                model_config_file_path = model_config_file_path
            )
            logging.info(f"Model trainer config: {model_trainer_config}")
            return model_trainer_config

        except Exception as e:
            raise CementException(e, sys)

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_evaluation_config_info = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            model_evaluation_artifact = os.path.join(
                artifact_dir,
                MODEL_EVALUATION_ARTIFACT_KEY,
                ) 

            model_evaluation_file_path = os.path.join(
                model_evaluation_artifact,
                model_evaluation_config_info[MODEL_EALUATION_FILE_NAME_KEY]
                )
            
            model_evaluation_config = ModelEvaluationConfig(
                model_evaluation_file_path = model_evaluation_file_path,
                time_stamp = self.time_stamp    
                )
            logging.info(f"Model Evaluation Config: {model_evaluation_config}.")
            return model_evaluation_config

        except Exception as e:
            raise CementException(e, sys)

    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_pusher_config_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]

            export_dir_path = os.path.join(
                ROOT_DIR,
                model_pusher_config_info[MODEL_EXPORT_DIR_KEY],
                self.time_stamp
            )
            
            model_pusher_config = ModelPusherConfig(
                export_dir_path = export_dir_path
            )
            logging.info(f"Model pusher config {model_pusher_config}")
            return model_pusher_config

        except Exception as e:
            raise CementException(e, sys)
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config_info = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config_info[TRAINING_PIPELINE_NAME_KEY], 
            training_pipeline_config_info[ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(
                artifact_dir = artifact_dir
            )   
            
            return training_pipeline_config

        except Exception as e:
            raise CementException(e, sys)

