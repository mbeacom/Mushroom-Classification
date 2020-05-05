# Mushroom Classification Model and API

A project, prototyped in Octave and implemented in Python, to use machine learning to classify a mushroom as poisonous/edible using the mushroom dataset from the UCI Machine Learning repository which can be viewed [here](https://www.kaggle.com/uciml/mushroom-classification).

The model is trained using a combination of logistic regression and gradient descent as minimisation method.

The idea was then to expose this model via a minimalist RESTful API, but focusing on best practices for API development.

The Python implementation purposely only uses NumPy and Pandas for linear algebra and data manipulation, this project contains **NO DEPENDENCY ON MACHINE LEARNING LIBRARIES** as the purpose was to implement logistic regression from scratch, rather than provide an efficient scalable solution for the machine learning model.

# Octave Prototype

The initial prototype for the Mushroom Classification model is found within the `prototyping` folder. The model is trained using the `train.m` or `train_withanalysis.m` scripts, with the latter outputting the validation and learning curve of the middle to the `imgs` sub directory.

# Python Implementation

The machine learning model is also implemented using python, which is all contained within the `src` folder. The `mushroom_classifier`  module is the actual implementation of the mushroom classifier model, while the `api` module uses the Flask Web Framework to expose the model via a RESTful Web API. 

For using either it is advised that a virtual environment to be setup in the root directory of the project, and then some environmental variables to be set.

## General Setup - Virtual Environment

A virtual environment should be used to work on the project, in the `src` folder of the project. Once the virtual environment is setup a `paths.pth` should be added to the virtual environments `site-packages` folder. This should just contain the absolute path to the `src` folder for the project. This allows the virtual environment to use treat the `src` folder as the 'root' of the python implementation of the project.

## mushroom_classifier Module Setup and Description

Absolute paths need to be set as environment variables for the `train.py` script within the `mushroom_classifier` module to work and export the models to the `trained_models` and `current_model` directories, the required environment variables are:

`export DATASET_DIR=ABSOLUTE-PATH-TO-DATASET-FOLDER(ie the files folder in this project)`
`export CURRENT_MODEL_DIR=ABSOLUTE-PATH-TO-CURRENT-MODEL-FOLDER`
`export TRAINED_MODELS_DIR=ABSOLUTE-PATH-TO-TRAINED-MODEL-FOLDER`

To use the provided dataset in this repository set the `DATASET_DIR` environment variable to the absolute path of the `files` folder, as to correctly run the `train.py` script a `mushrooms.csv` file and `unseen_mushrooms.csv` file need to be present in the `DATASET_DIR` directory.

The mushroom classifier model can be generated and saved by running the `train.py` within the mushroom_classifier module, this pickles the model object and saves it to both a directory containing all the trained models, and to a directory containing only the last trained model.

A diagnostics JPEG is also saved into the same directory as the model, containing graphs for the cost reduction over time, and its learning rate.

Before the `train.py` script is ran, you should run the available tests for the `mushroom_classifier` module, more specifically the `test_mushroom_classifier` contains all the tests for the `mushroom_classifier` module.

The workflow currently, is to train the model and store it, with the relevant columns for reindexing and graph diagnostics, in a folder based on the current time. This folder is then stored in the directory specified in the `TRAINED_MODELS_DIR` environment variable. 

If the currently trained model has a high enough accuracy, and correctly predicts the completely known examples as specified in the `unseen_mushrooms.csv` file, this model and all its files will be exported and overwrite anything in the current model directory, as specified by the `CURRENT_MODEL_DIR` environment variable.

## api Module Setup and Description

The model contained within the directory specified by the `CURRENT_MODEL_DIR` environment variable can be exposed via a RESTful Web Service using Flask. 

The API also requires the path to the features definition .json file specified via a environment variable:
`export FEATURE_DEFINITION_PATH=ABSOLUTE-PATH-TO-DEFINITION-FILE`

This definition file, `features-definition.json` within the `src/api` directory, contains all possible keys and allowed values for making predictions against the model.

The API also makes use of logging to log files, the directory for these logs files is specified via an environment variable:

`export LOGS_DIRECTORY=ABSOLUTE-PATH-TO-LOG-FILE-DIRECTORY`

The flask app can also be run by directly serving the `run.py` file or the `FLASK_APP` environment variable can be set to the absolute path of the `run.py` file:

`export FLASK_APP=ABSOLUTE-PATH-TO-RUN.PY-FILE`

Then the flask api can be ran using the `Flask Run` command

The flask app environment can also be specified via the environment command:

`export FLASK_ENV=development`

Once the application is running, mushroom features can be given the API to use the model to make a prediction.

For example, using the url:

`http://127.0.0.1:5000/api/prediction/submit?values=[{%22cap-shape%22:%22c%22,%22cap-surface%22:%22y%22,%22cap-color%22:%22e%22,%22bruises%22:%22f%22,%22odor%22:%22n%22,%22gill-attachment%22:%22f%22,%22gill-spacing%22:%22c%22,%22gill-size%22:%22n%22,%22gill-color%22:%22w%22,%22stalk-shape%22:%22e%22,%22stalk-root%22:%22b%22,%22stalk-surface-above-ring%22:%22s%22,%22stalk-surface-below-ring%22:%22s%22,%22stalk-color-above-ring%22:%22w%22,%22stalk-color-below-ring%22:%22w%22,%22veil-type%22:%22p%22,%22veil-color%22:%22w%22,%22ring-number%22:%22t%22,%22ring-type%22:%22s%22,%22spore-print-color%22:%22w%22,%22population%22:%22v%22,%22habitat%22:%22d%22}]`

The above URL how the mushroom attributes are added as JSON key values pairs to the JSON object within the 'values' JSON array. The response for this call will also be JSON, with a Poisonous key containing a value True or False depending on the models prediction.

Tests for the API are available within the `test_api`module.