import sys
import os

sys.path.append(os.path.abspath("src"))

from Briefly.config.configuration import ConfigurationManager
from Briefly.components.model_trainer import ModelTrainer
from Briefly.logging import logger



class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()