import sys
import os

sys.path.append(os.path.abspath("src"))

from Briefly.config.configuration import ConfigurationManager
from Briefly.components.data_validation import DataValidation
from Briefly.logging import logger



class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_files_exist()