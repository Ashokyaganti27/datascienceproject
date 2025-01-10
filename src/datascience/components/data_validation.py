from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd
from src.datascience import logger

class DataValidation():
    def __init__(self,config: DataValidationConfig):
        self.config=config
    
    try:
        def validate_all_columns(self) -> bool:

            validation_state=None

            data=pd.read_csv(self.config.unzip_data_dir)

            data_columns=list(data.columns)

            schema_columns=self.config.all_schema.keys()

            for column in data_columns:
                if column not in schema_columns:
                    validation_state=False
                    with open(self.config.STATUS_FILE,"w") as file:
                       file.write(f"validation state is {validation_state}")
                else:
                    validation_state=True
                    with open(self.config.STATUS_FILE,"w") as file:
                       file.write(f"validation state is {validation_state}")

            return validation_state
    except Exception as e:
        raise e