import os
from pathlib import Path
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

# project name
project_name = "cnnClassifier"

#List of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utlis/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'parms.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',




]

#Writing a code to create the directory and the respective files if they do not exist
for filepath in list_of_files:
    #Path libray is used to identify the device and based on that sets the path 
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath)

    #Cheks if the filedir is not empty and if its not empty creates the directory
    if filedir !="":  
         os.makedirs(filedir, exist_ok=True)
         logging.info(f'Creating directory: {filedir} for the file: {filename}')

    #Creates an empty file if the file does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
         with open(filepath, 'w') as fp:
             pass
         logging.info(f'Creating empty file: {filepath}')

    else:
         logging.info(f'{filename} already exists')