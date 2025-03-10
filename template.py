import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')


project_name="Briefly"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath=Path(filepath)       #it recognises whether its a window path or a linux path and returns it int that format
    filedir, filename = os.path.split(filepath)  #this function seprerates my folder and file

    if filedir !="":
        os.makedirs(filedir,exist_ok=True) #exit_ok makes sure that if directory already exists then not ot make a new one
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if(not os.path.exists(filepath) or (os.path.getsize(filepath)==0)): #if file does't exist or its empty
        with open(filepath,'w') as f: #Here we are only creating a file and dont want to do any operation so we just
            pass                       #pass it
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")



