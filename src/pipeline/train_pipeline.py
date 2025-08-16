import os
import pickle
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # Step 1: Initialize and run data transformation
    data_transformation = DataTransformation()
    train_path = os.path.join("artifacts", "train.csv")
    test_path = os.path.join("artifacts", "test.csv")
    train_arr, test_arr, preprocessor = data_transformation.initiate_data_transformation(train_path,test_path)

    # Step 2: Save preprocessor into artifacts folder
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/preprocessor.pkl", "wb") as f:
        pickle.dump(preprocessor, f)

