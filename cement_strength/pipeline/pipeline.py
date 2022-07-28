from cement_strength.component.data_validation import DataValidation
from cement_strength.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from cement_strength.exception import CementException
from cement_strength.component.data_ingestion import DataIngestion
import os, sys
from cement_strength.config.configuration import Configuration

config = Configuration()
class Pipeline:

    def __init__(self, config:Configuration=config) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CementException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CementException(e,sys) from e

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise CementException(e,sys) from e

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise CementException(e, sys) from e