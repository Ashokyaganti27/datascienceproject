from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path


STAGE_NAME="Data Transformation Stage"


class DataTransformationTrainingPipeline():
    def __init__(self):
        pass
    def initiate_transformation_data(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]
            if status=="True":
                config=ConfigurationManager()
                get_transformation_data=config.get_transformation_data_config()
                transfomation_data=DataTransformation(get_transformation_data)
                transfomation_data.train_test_splitting()
            else:
                raise Exception("may be status is False")
        except Exception as e:
            raise e


if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} ... started")
        obj=DataTransformationTrainingPipeline()
        obj.initiate_transformation_data()
        logger.info(f">>>> stage {STAGE_NAME} completed......")
    except Exception as e:
        raise e