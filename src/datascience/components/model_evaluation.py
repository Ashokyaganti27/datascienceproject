import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import mlflow
import joblib
from urllib.parse import urlparse
import mlflow.sklearn
import json
from src.datascience.entity.config_entity import ModelEvalutionConfig
from src.datascience.utils.common import save_json
from pathlib import Path
import os


os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/YagantiAshok177/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="YagantiAshok177"
os.environ["MLFLOW_TRACKING_PASSWORD"]="Ashok123@"


class ModelEvaluation():
    def __init__(self,config: ModelEvalutionConfig):
        self.config=config
    
    def eva_metrics(self,actual,pred):
        rmse=np.sqrt(mean_squared_error(actual,pred))
        mae=mean_absolute_error(actual,pred)
        r2=r2_score(actual,pred)

        return rmse,mae,r2
    

    def log_into_mlflow(self):

        test_data=pd.read_csv(self.config.test_datapath)

        model=joblib.load(self.config.model_filepath)

        test_x=test_data.drop(self.config.target_column,axis=1)

        test_y=test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)

        type_of_uri=urlparse(mlflow.get_tracking_uri()).scheme

       
        with mlflow.start_run():

            predicted_data=model.predict(test_x)

            (rmse,mae,r2)=self.eva_metrics(test_y,predicted_data)

            scores={"rmse":rmse,"mae":mae,"r2":r2}
            save_json(path=Path(self.config.metrics_file_name),data=scores)
            
            for key, value in self.config.all_params.items():
              mlflow.log_param(key, value)

            mlflow.log_param("params",self.config.all_params)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2",r2)


            if type_of_uri != "file":

                mlflow.sklearn.log_model(model,"model",registered_model_name="ElasticNet")
            else:
                mlflow.sklearn.log_model(model,"model")