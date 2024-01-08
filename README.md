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


INITALIZE GIT
git init


