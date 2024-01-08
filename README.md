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


INITALIZE GIT
git init


