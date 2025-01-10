from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger

STAGE_NAME="Date Ingestion Stage"

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        try:
            config=ConfigurationManager()
            data_ingetion_config=config.get_data_ingestion_config()
            data_ingetion=DataIngestion(config=data_ingetion_config)
            data_ingetion.download_file()
            data_ingetion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=="__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} ... started")
        obj=DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>> stage {STAGE_NAME} completed......")
    except Exception as e:
        raise e
