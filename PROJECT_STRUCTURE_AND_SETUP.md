**STUDENT PERFORMANCE PREDICTION — PROJECT STRUCTURE \& DEVELOPER GUIDE (TXT)**

================================================================================



Author: Aryan Roy

Purpose: Explain the entire repository structure, end-to-end data \& code flow, how to run

&nbsp;        everything from scratch, and document common errors + fixes (including the

&nbsp;        'str object has no attribute transform' issue). This file is plain text so it

&nbsp;        renders consistently on GitHub and elsewhere.



--------------------------------------------------------------------------------

**1) PROJECT OVERVIEW**

--------------------------------------------------------------------------------

This project predicts a student's Mathematics score from multiple features (8–9 inputs).

It demonstrates a production-style Machine Learning workflow:

\- Data ingestion

\- Data transformation (encoding + scaling)

\- Model training with model selection and (optionally) hyperparameter tuning

\- Saving reusable artifacts (preprocessor.pkl, model.pkl)

\- Prediction pipeline for new data

\- Deployment via a Flask web app



Code is modularized and commented to improve readability and maintainability.

Logging and custom exception handling are used across the codebase.



--------------------------------------------------------------------------------

**2) HIGH-LEVEL ARCHITECTURE (END-TO-END FLOW)**

--------------------------------------------------------------------------------



Raw Dataset

\[Data Ingestion]

&nbsp;  - Reads raw data

&nbsp;  - Splits into train/test

&nbsp;  - Saves artifacts/train.csv and artifacts/test.csv

&nbsp;  
&nbsp;

\[Data Transformation]

&nbsp;  - Builds preprocessing pipeline (e.g., encoders, scalers)

&nbsp;  - Fits on train inputs, transforms train/test inputs

&nbsp;  - Returns train\_arr, test\_arr, and the fitted preprocessor object

&nbsp;  - Saves artifacts/preprocessor.pkl

&nbsp;  
&nbsp;  

\[Model Trainer]

&nbsp;  - Trains multiple regression models (e.g., linear, tree-based, boosting)

&nbsp;  - Evaluates models, optionally tunes hyperparameters

&nbsp;  - Selects best model and saves artifacts/model.pkl

&nbsp;  
&nbsp;  

\[Prediction Pipeline]

&nbsp;  - Loads artifacts/preprocessor.pkl and artifacts/model.pkl

&nbsp;  - Transforms incoming features and generates predictions

&nbsp;  
&nbsp;  

\[Flask App]

&nbsp;  - Exposes a simple web UI (home.html / index.html)

&nbsp;  - Accepts user input and displays predicted Math score





--------------------------------------------------------------------------------

**3) REPOSITORY LAYOUT (WHAT EACH FILE/FOLDER DOES)**

--------------------------------------------------------------------------------



root/

&nbsp; app.py

&nbsp;   - Flask entry point. Defines routes (e.g., '/', '/predictdata').

&nbsp;   - Uses PredictPipeline to transform and predict on new inputs.

&nbsp;   - Returns rendered templates or prediction output.



&nbsp; templates/

&nbsp;   home.html

&nbsp;   index.html

&nbsp;   - HTML templates for the Flask UI. One is typically the landing page,

&nbsp;     the other contains the form where users enter features and submit.



&nbsp; artifacts/   (auto-created by training; DO NOT COMMIT stale files)

&nbsp;   preprocessor.pkl   -> Fitted preprocessing pipeline (encoders/scalers/etc.)

&nbsp;   model.pkl          -> Trained best model

&nbsp;   train.csv          -> Training split saved by Data Ingestion

&nbsp;   test.csv           -> Test split saved by Data Ingestion

&nbsp;   NOTE: The content here is generated; if things break, delete and regenerate.



&nbsp; src/

&nbsp;   components/

&nbsp;     data\_ingestion.py

&nbsp;       - Reads raw data (path can be configured or embedded).

&nbsp;       - Splits into train/test (e.g., sklearn.model\_selection.train\_test\_split).

&nbsp;       - Saves split CSVs under artifacts/train.csv and artifacts/test.csv.

&nbsp;       - Returns the file paths to those CSVs.

&nbsp;     

&nbsp;     data\_transformation.py

&nbsp;       - Defines get\_data\_transformer\_object() that returns a composite transformer

&nbsp;         (e.g., ColumnTransformer/Pipeline) that encodes categoricals and scales numerics.

&nbsp;       - initiate\_data\_transformation(train\_path, test\_path):

&nbsp;         \* Reads CSVs

&nbsp;         \* Splits features/target (e.g., target 'math\_score')

&nbsp;         \* Fits the transformer on X\_train, transforms X\_train and X\_test

&nbsp;         \* Creates numpy arrays train\_arr and test\_arr (X\_transformed with y appended)

&nbsp;         \* Saves the fitted transformer to artifacts/preprocessor.pkl

&nbsp;         \* Returns train\_arr, test\_arr, and the fitted preprocessor object



&nbsp;     model\_trainer.py

&nbsp;       - Trains and evaluates multiple regression models (e.g., LinearRegression,

&nbsp;         RandomForestRegressor, GradientBoosting, etc.).

&nbsp;       - Optionally performs hyperparameter tuning (e.g., GridSearchCV/RandomizedSearchCV).

&nbsp;       - Selects the best model based on validation metrics (e.g., R^2).

&nbsp;       - Saves the best trained model object to artifacts/model.pkl.

&nbsp;       - Returns metrics for logging or printing.



&nbsp;   pipeline/

&nbsp;     train\_pipeline.py

&nbsp;       - Orchestrates the entire training flow:

&nbsp;         Data Ingestion -> Data Transformation -> Model Training -> Save artifacts

&nbsp;       - This is the ONLY script users need to run to prepare artifacts for prediction.



&nbsp;     predict\_pipeline.py

&nbsp;       - Loads artifacts/preprocessor.pkl and artifacts/model.pkl.

&nbsp;       - Expects a pandas.DataFrame of input features.

&nbsp;       - Applies preprocessor.transform(features) and model.predict(transformed).

&nbsp;       - Returns predictions.

&nbsp;       - IMPORTANT: Must actually load the pickled objects (not just set string paths).



&nbsp;   utils.py

&nbsp;     - Common helpers. Typical functions include:

&nbsp;       save\_object(file\_path, obj)   -> pickle.dump(obj, file\_path)

&nbsp;       load\_object(file\_path)        -> pickle.load(file\_path)

&nbsp;       evaluate\_models(...)          -> run model training/eval loops, return metrics

&nbsp;     - May also include path helpers or data validation functions.



&nbsp;   logger.py

&nbsp;     - Centralized logging configuration.

&nbsp;     - Logs the start/end of major steps and key variable states.



&nbsp;   exception.py

&nbsp;     - Custom exception class to wrap and re-raise errors with more context.



&nbsp; requirements.txt

&nbsp;   - Python dependency list (install with: pip install -r requirements.txt).



&nbsp; setup.py (optional)

&nbsp;   - Allows installing src as a package for clean imports (e.g., pip install -e .).





--------------------------------------------------------------------------------

**4) DATA EXPECTATIONS AND TARGET**

--------------------------------------------------------------------------------

\- Target column name is typically "math\_score".

\- Numerical columns may include (for example): "reading\_score", "writing\_score".

\- Categorical columns (if any) are encoded within the transformer created by

&nbsp; get\_data\_transformer\_object().

\- The Data Transformation step is responsible for dropping the target from inputs,

&nbsp; fitting/transforming inputs, and returning arrays with target appended as the last column.





--------------------------------------------------------------------------------

**5) HOW TO RUN (RECOMMENDED QUICKSTART)**

--------------------------------------------------------------------------------

1\. Create and activate environment, then install requirements:

&nbsp;  conda create -n mlproj python=3.8 -y

&nbsp;  conda activate mlproj

&nbsp;  pip install -r requirements.txt



2\. Train the pipeline (this runs ingestion -> transformation -> model training):

&nbsp;  python src/pipeline/train\_pipeline.py



&nbsp;  This will create the following artifacts:

&nbsp;    artifacts/preprocessor.pkl

&nbsp;    artifacts/model.pkl

&nbsp;    artifacts/train.csv

&nbsp;    artifacts/test.csv



3\. Start the Flask app:

&nbsp;  python app.py



4\. Open the app in your browser:

&nbsp;  http://127.0.0.1:5000/



NOTE: You DO NOT need to run data\_ingestion.py or data\_transformation.py manually.

&nbsp;     train\_pipeline.py already calls both steps internally.





--------------------------------------------------------------------------------

**6) ADVANCED: RUN COMPONENTS MANUALLY (FOR DEBUGGING)**

--------------------------------------------------------------------------------

Python REPL example:



from src.components.data\_ingestion import DataIngestion

from src.components.data\_transformation import DataTransformation

from src.components.model\_trainer import ModelTrainer

from src.utils import save\_object, load\_object



\# 1) Ingestion: produces artifacts/train.csv and artifacts/test.csv

ing = DataIngestion()

train\_path, test\_path = ing.initiate\_data\_ingestion()



\# 2) Transformation: returns arrays and the fitted preprocessor

trans = DataTransformation()

train\_arr, test\_arr, preprocessor = trans.initiate\_data\_transformation(train\_path, test\_path)



\# Optional: persist the preprocessor (train step also saves it)

\# save\_object(file\_path='artifacts/preprocessor.pkl', obj=preprocessor)



\# 3) Training: trains \& saves the best model to artifacts/model.pkl

trainer = ModelTrainer()

trainer.initiate\_model\_trainer(train\_arr, test\_arr)





--------------------------------------------------------------------------------

**7) FLASK APP ROUTES (TYPICAL)**

--------------------------------------------------------------------------------

\- GET  /            -> Render a home page (home.html)

\- GET  /predictdata -> Render the prediction form (index.html)

\- POST /predictdata -> Read form inputs -> Build DataFrame ->

&nbsp;                      PredictPipeline.predict(df) -> Show result



Implementation notes:

\- Ensure the form field names match the expected feature names in predict\_pipeline.

\- PredictPipeline must load BOTH preprocessor.pkl and model.pkl as Python objects.

\- Always pass a pandas.DataFrame to PredictPipeline.predict().





--------------------------------------------------------------------------------

**8) PATHS AND WORKING DIRECTORY NOTES**

--------------------------------------------------------------------------------

\- Use os.path.join and absolute paths derived from \_\_file\_\_ when needed to

&nbsp; avoid issues with relative paths.

\- Example for robust loading inside utils/predict\_pipeline:

&nbsp;   import os, pickle

&nbsp;   BASE\_DIR = os.path.dirname(os.path.abspath(\_\_file\_\_))

&nbsp;   ROOT\_DIR = os.path.abspath(os.path.join(BASE\_DIR, ".."))

&nbsp;   preprocessor\_path = os.path.join(ROOT\_DIR, "artifacts", "preprocessor.pkl")

&nbsp;   with open(preprocessor\_path, "rb") as f:

&nbsp;       preprocessor = pickle.load(f)



\- If running Flask from a different working directory, absolute paths prevent

&nbsp; FileNotFoundError for artifacts.





--------------------------------------------------------------------------------

**9) LOGGING AND EXCEPTIONS**

--------------------------------------------------------------------------------

\- logger.py sets up a central logger; each major step logs start/end and

&nbsp; critical information (file paths, shapes, metrics).

\- exception.py defines a CustomException used to wrap lower-level errors and

&nbsp; include stack traces and additional context.





--------------------------------------------------------------------------------

**10) COMMON PITFALLS AND HOW TO AVOID THEM**

--------------------------------------------------------------------------------

A) FileNotFoundError: No such file or directory: 'artifacts\\preprocessor.pkl'

&nbsp;  - Cause: Artifacts not generated yet or wrong working directory.

&nbsp;  - Fix:

&nbsp;    1) Run: python src/pipeline/train\_pipeline.py

&nbsp;    2) Use absolute paths when loading artifacts in predict pipeline.



B) NameError: name 'preprocessor' is not defined (in training)

&nbsp;  - Cause: Trying to pickle.dump(preprocessor, ...) before creating it.

&nbsp;  - Fix: Create the preprocessor via DataTransformation and capture the returned

&nbsp;         object: train\_arr, test\_arr, preprocessor = data\_transformation.initiate\_data\_transformation(...)



C) TypeError: initiate\_data\_transformation() missing 2 required positional arguments

&nbsp;  - Cause: Calling initiate\_data\_transformation() without passing train\_path and test\_path.

&nbsp;  - Fix: Provide both CSV paths returned by DataIngestion:

&nbsp;         train\_arr, test\_arr, preprocessor = trans.initiate\_data\_transformation(train\_path, test\_path)



D) IMPORTANT: AttributeError: 'str' object has no attribute 'transform'

&nbsp;  - What this means:

&nbsp;      You attempted to call preprocessor.transform(features) but 'preprocessor'

&nbsp;      is actually a string (e.g., 'artifacts/preprocessor.pkl') rather than a fitted

&nbsp;      transformer object.

&nbsp;  - Why it happens:

&nbsp;      1) You mistakenly saved a string into artifacts/preprocessor.pkl in an earlier run.

&nbsp;      2) Or you forgot to assign the loaded object back to the variable (i.e., you set

&nbsp;         preprocessor = 'artifacts/preprocessor.pkl' instead of loading it with pickle).

&nbsp;  - How to confirm:

&nbsp;      In a Python shell:

&nbsp;        import pickle

&nbsp;        with open('artifacts/preprocessor.pkl', 'rb') as f:

&nbsp;            obj = pickle.load(f)

&nbsp;        print(type(obj))

&nbsp;      You should see a sklearn transformer/pipeline type, NOT <class 'str'>.

&nbsp;  - Solutions (do ALL of these to be safe):

&nbsp;      1) Make sure utils.load\_object(file\_path) uses pickle.load(file\_obj) and returns the object.

&nbsp;      2) In predict\_pipeline.py, ASSIGN the loaded object:

&nbsp;           preprocessor = load\_object(file\_path=preprocessor\_path)

&nbsp;         NOT just setting the path string.

&nbsp;      3) Delete stale artifacts and regenerate:

&nbsp;           - Delete the entire artifacts/ folder

&nbsp;           - Re-run: python src/pipeline/train\_pipeline.py

&nbsp;      4) Use absolute paths if Flask runs from a different working directory.



E) General tip for collaborators/forkers:

&nbsp;  - Anyone who clones/forks and runs the training pipeline from scratch will

&nbsp;    generate fresh, valid artifacts and should not hit the above error.





--------------------------------------------------------------------------------

**11) RECOMMENDED WORKFLOW FOR NEW USERS (TL;DR)**

--------------------------------------------------------------------------------

1\) pip/conda install requirements

2\) Run: python src/pipeline/train\_pipeline.py

3\) Run: python app.py

4\) Use the web UI to predict a student's Math score



If anything breaks, delete artifacts/ and repeat steps 2–3.





--------------------------------------------------------------------------------

**12) FUTURE IMPROVEMENTS**

--------------------------------------------------------------------------------

\- Add unit tests (pytest) for utils, components, and pipelines

\- Add CI (GitHub Actions) for linting and tests

\- Containerize with Docker for reproducibility

\- Deploy on a cloud PaaS (Render/Railway/Heroku)

\- Add SHAP/feature importance visualizations to explain predictions

\- Extend to multiple subject predictions and/or classification tasks





*END OF FILE*



