import os

dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "saved_models",
    "src",
    "notebooks"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    # create .gitkeep file inside the directory so that we can upload empty folders in github
    with open(os.path.join(dir_, ".gitkeep"), 'w') as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

for file_ in files:
    with open(file_, 'w') as f:
        pass