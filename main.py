import os

os.system("python src/data_ingestion.py")
print("Data ingestion run")

os.system("python src/data_preprocessing.py")
print("Data preprocessing run")

os.system("python src/feature_engineering.py")
print("Feature engineering run")

os.system("python src/model_building.py")
print("Model building run")

os.system("python src/model_evaluation.py")
print("Model evaluation run")
