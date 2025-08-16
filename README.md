🎓 Student Performance Prediction

This project predicts student performance in Mathematics based on multiple factors such as reading and writing scores.
It follows a fully modularized ML pipeline (data ingestion → preprocessing → model training → deployment with Flask).

🚀 Features

End-to-end Machine Learning pipeline

Handles missing values, encoding, and standardization(using transformers)

Model comparison with hyperparameter tuning

Saves best model + parameters automatically

Deployed using Flask with simple web UI (home.html, index.html)

Includes logging and exception handling

Well-commented code for better understanding ✍️

📂 Project Structure
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   ├── predict_pipeline.py
│   ├── utils.py
│   ├── logger.py
│   ├── exception.py
├── templates/
│   ├── home.html
│   ├── index.html
├── artifacts/        # Auto-created (stores preprocessor & model)
├── requirements.txt
├── setup.py
├── app.py            # Flask app entry point

⚙️ Installation & Setup
1. Clone repo & create environment
git clone <your-repo-link>
cd student-performance-prediction

conda create -n mlproj python=3.8 -y
conda activate mlproj
pip install -r requirements.txt

2. Train pipeline (runs ingestion → transformation → model training)
python src/pipeline/train_pipeline.py


This will create artifacts/preprocessor.pkl and artifacts/model.pkl.

3. Run the Flask app
python app.py


App will start at: http://127.0.0.1:5000/

⚡ Advanced (Manual Component Execution)

You can also run each step manually if you want to debug or explore intermediate outputs:

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

# 1) Data Ingestion
ing = DataIngestion()
train_path, test_path = ing.initiate_data_ingestion()

# 2) Data Transformation
trans = DataTransformation()
train_arr, test_arr, preprocessor = trans.initiate_data_transformation(train_path, test_path)

# 3) Model Training
trainer = ModelTrainer()
trainer.initiate_model_trainer(train_arr, test_arr)

⚠️ Important Notes

If you ever see this error:

AttributeError: 'str' object has no attribute 'transform'


👉 Delete the entire artifacts/ folder and re-run the training pipeline:

rm -rf artifacts/
python src/pipeline/train_pipeline.py


When forking/cloning, others won’t face this error if they run the pipeline from the start.

train_pipeline.py already triggers ingestion & transformation, so you don’t need to run those files manually unless debugging.

💡 Future Improvements

Add CI/CD integration

Deploy on cloud (Heroku/AWS/GCP)

Extend to predict scores in multiple subjects
