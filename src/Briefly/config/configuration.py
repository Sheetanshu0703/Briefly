import sys
import os

sys.path.append(os.path.abspath("src"))

from Briefly.constants import *  # Now it should work
from Briefly.utils.common import  read_yaml, create_directories
from Briefly.entity import (DataIngestionConfig)




class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        """Initialize Configuration Manager and load YAML configs."""
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Ensure artifacts directory exists
        create_directories([self.config["artifacts_root"]])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Retrieve Data Ingestion Configuration."""
        config = self.config["data_ingestion"]  # Use dictionary syntax!

        create_directories([config["root_dir"]])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config["root_dir"],
            source_URL=config["source_URL"],
            local_data_file=config["local_data_file"],
            unzip_dir=config["unzip_dir"],
        )
        return data_ingestion_config
