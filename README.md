# Connectome

Created as part of an university project "Innovationlab Big Data Science" at LMU Munich.


# Code setup
Folder structure based on Cookiecutter for Data science https://github.com/drivendata/cookiecutter-data-science.

Directory structure:

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── Archive            <- Old files
├── conf               <- Space for credentials
│
├── data
│   └──                <- to be filled
│
├── docs               <- Space for Sphinx documentation
│
├── notebooks          <- Jupyter notebooks. Naming convention is date YYYYMMDD (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `20211208-jqp-KB-rf-baseline`.
│
├── references         <- Explanatory Materials, documents and transcripts
│
├── results            <- Intermediate analysis as HTML, PDF, LaTeX, etc.
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files etc
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── ConnectomeR    <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── preprocessing  <- Scripts to turn raw data into features for modeling
│   │   └── preprocessing_matlab_files.py
│   │   └── data_loader.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── gradient_boosting.py
│   │   └── rf.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tests              <- unittests
    ├── test_preprocessing_matlab_files.py
    └── test_train_test_split.py  
```


# Workflow

The typical workflow to develop code is the following:

- Prototype code in a jupyter notebook
- Move code into a function that takes data and parameters as inputs and returns the processed data or trained model as output.
- Test the function in the jupyter notebook
- Move the function into the src folder
- Import the function in the jupyter notebook 
- Test the function is working


# Demo Video

The following video displays the full pipeline from preprocessing to model outputs:

https://user-images.githubusercontent.com/51715552/158160781-d1e6c7bc-de14-49b9-98ce-d7f9198411d1.mp4


