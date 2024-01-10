CREATE CONDA ENVIRONMENT
conda create -n dvcwine python -y

THEN ACTIVATE ENV
conda activate dvcwine

TO DEACTIVATE
conda deactivate

CREATE TEMPLATE FILE WHICH WILL CREATE BASIC PROJECT FILE AND FOLDER STRUCTURE
touch template.py
python template.py

CREATE files get_data.py and load_data.py inside the src folder
touch src/get_data.py && touch src/load_data.py

INSTALL JUPYTER NOTEBOOK
pip install jupyterlab
AND RUN
jupyter-lab noteboos/

INSTALL DVC
pip install dvc
and initialize
dvc init
KEEP DATA FILE TO TRACK
dvc add data_given/winequality.csv

SPLIT DATA INTO test and train 
CREATE split_data.py file inside src folder
touch src/split_data.py

CREATE A MODEL TRAIN AND EVALUATE
CREATE FILE CALLED train_and_evaluate.py inside src folder
touch src/train_and_evaluate.py

AFTER TRAINING AND EVALUATING WE CREATE A REPORT FOLDER
mkdir report
and create scores.json and params.json files inside it
and write the reports of model performance

FOR PYTHON TESTING FILE INSTALL TOX
pip install tox
AND CREATE tox.ini file
touch tox.ini
ALSO INSTALL PYTEST
pip install pytest

ALSO WE CREATE TEST FOLDER
mkdir test
CREATE confest.py AND test_config.py

FOR CREATING PACKAGE 
touch setup.py

NOW CREATE WEB APP USING FLASK
mkdir webapp
mkdir webapp/static
mkdir webapp/static/css
mkdir webapp/static/script


mkdir webapp/template
touch webapp/template/index.html
touch webapp/template/base.html
touch webapp/template/404.html

WE CREATE prediction_service folder and inside it create model folder
inside predicton_service create file '__init__.py', schema_in.json and prediction.py


NOW WE NEED TO CREATE app.py file where we need flask to build app
pip install flask 


FOR CONTINUES INTEGRATION AND CONTINUEUS DEPLOYMET WE CREATE .github FOLDER
INSIDE .github FOLDER WE WILL CREATE workflows FOLDER
mkdir -p .github/workflows
INSIDE workflows FOLDER WE WILL CREATE ci-cd.yaml file GITHUB WILL AUTOMATICALLY RUN THE BUILD PROCESS AFTER THIS

WE HAVE CREATED NEW BRANCH CHECKOUT mlflow.org for more documentation
main-mlflow

CREATE log_production_model.py inside src folder
AND UPDATE dvc.yaml FILE ALSO UPDATA params.yaml FILE WITH THE mlflow-config:
CREATE artifacts folder in root directory


create an artifcats folder

mlflow server command -

mlflow server
--backend-store-uri sqlite:///mlflow.db
--default-artifact-root ./artifacts
--host 0.0.0.0 -p 1234

