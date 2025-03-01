# Build & Track ML Pipelines with DVC

## How to run?

conda create -n test python=3.11 -y

conda activate test

pip install -r requirements.txt


## DVC Commands => with dvc we don't need to use main.py

git init

dvc init

dvc repro => execute the pipeline

dvc dag => pipeline diagram

dvc metrics show => show the metrics