from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger


STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationTrainingPipeline():
    def __init__(self):
        pass

    def initiate_evaluation_data(self):
        try:
            config=ConfigurationManager()
            evaluation_data=config.get_model_evaluation_data()
            evaluation=ModelEvaluation(config=evaluation_data)
            evaluation.log_into_mlflow()
        except Exception as e:
            raise e
        
if __name__=="__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} ... started")
        obj=ModelEvaluationTrainingPipeline()
        obj.initiate_evaluation_data()
        logger.info(f">>>> stage {STAGE_NAME} completed......")
    except Exception as e:
        raise e