from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline

STAGE_NAME="Date Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} ... started")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>> stage {STAGE_NAME} completed......")
except Exception as e:
    raise e



STAGE_NAME="Date validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} ... started")
    obj=DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>> stage {STAGE_NAME} completed......")
except Exception as e:
    raise e


STAGE_NAME="Data Transformation Stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} ... started")
    obj=DataTransformationTrainingPipeline()
    obj.initiate_transformation_data()
    logger.info(f">>>> stage {STAGE_NAME} completed......")
except Exception as e:
    raise e








logger.info("logging Successfully")