from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger


STAGE_NAME="Model Trainer Stage"

class ModelTrainingPipeline():
    def __init__(self):
        pass


    def initiate_model_training(self):
        try:
            config=ConfigurationManager()
            model_trainer_data=config.get_model_trainer_data()
            model_data=ModelTrainer(config=model_trainer_data)
            model_data.train()
        except Exception as e:
            raise e
        
if __name__=="__main__":
    try:
        logger.info(f"-----Stage {STAGE_NAME} .......Started")
        obj=ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f"-----Satge {STAGE_NAME} .......completed")
    except Exception as e:
        raise e
    

    