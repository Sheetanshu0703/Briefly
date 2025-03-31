import os
import sys
import os

sys.path.append(os.path.abspath("src"))

from Briefly.logging import logger
from Briefly.entity import DataValidationConfig


import os

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True  # Assume all files exist initially

            # Get all files in the dataset directory
            dataset_path = os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            all_files = os.listdir(dataset_path)

            # Check if any required file is missing
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    validation_status = False  # If any file is missing, mark as False
                    break  # Exit early if a file is missing

            # Write the validation result to the status file
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e



