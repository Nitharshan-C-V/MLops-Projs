# MLops-Projs'

For this project we will be installing a conda env. 

The difference between a venv and a conda environment is that , 

venv : if you are working on projects which are only dedicated with python libraries only then having a venv with different python version will be sufficient 

conda: as the project complexity increases the requirement of the project will eventually scale and the packages which are required for the project will go out of scope of python alone , so for high computation and more of DL and Machine Learinging based projects we will be using conda environemnet as you can download the python verision and also the packages such as tensorflow , mlflow in the env whic is much more usefull. 

We will download and use miniconda version here as the anaconda version which we generally download is a heavy version and consumes high memory, so for light weight useage we will be using miniconda. The download procedure can be identified in the documenatation page.

## Step 1 : 
Create a repo in github for the project and clone it to your local system 

## Step 2 :

Create a Conda env with a python version of 3.8 

```bash
conda create -n kidney python=3.8 -y
``` 

Once this conda env is created next step is to activate:

```bash
conda activate kidney 
   ```

## Step 3 :

Once the conda env is active you can start installing the requirements.txt 

```bash
pip install -r requirements.txt
```

When you are done with installing , you can recheck by typing the command

```bash
pip list
```
Shows all the downloaded packages in from the requirements.txt
