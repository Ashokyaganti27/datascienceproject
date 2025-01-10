from src.datascience.constants import *
from src.datascience.utils.common import read_yaml,create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerconfig,ModelEvalutionConfig)
import os


class ConfigurationManager:
    def __init__(self,
                config_filepath=CONFIG_FILE_PATH,
                params_filepath=PARAMS_FILE_PATH,
                schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
            
    def get_data_validation_config(self) -> DataValidationConfig:

        config=self.config.data_validation
        schema=self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )


        return data_validation_config
    

    def get_transformation_data_config(self)->DataTransformationConfig:
        config=self.config.data_transforamtion

        create_directories([config.root_dir])

        transformation_data_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )


        return transformation_data_config
    
    def get_model_trainer_data(self) -> ModelTrainerconfig:
        config=self.config.model_trainer
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_data=ModelTrainerconfig(
            root_dir=config.root_dir,
            train_datapath=config.train_datapath,
            test_datapath=config.test_datapath,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )


        return model_trainer_data

    def get_model_evaluation_data(self) -> ModelEvalutionConfig:
        config=self.config.model_evaluation
        params=self.params.ElasticNet
        schema=self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])

        model_evaluation_data=ModelEvalutionConfig(
            root_dir=config.root_dir,
            test_datapath=config.test_datapath,
            model_filepath=config.model_filepath,
            metrics_file_name=config.metrics_file_name,
            target_column=schema.name,
            all_params=params,
            mlflow_uri=os.environ["MLFLOW_TRACKING_URI"]

          )
        
        return model_evaluation_data