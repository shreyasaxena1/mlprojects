import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

from src.exception import CustomException
from sklearn.model_selection  import GridSearchCV


def save_object(file_path, obj):
    """Save a Python object using pickle."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_model(X_train, X_test, y_train, y_test, models, params):
    """
    Train and evaluate multiple models on given training and test data.

    Args:
        X_train: Training features
        X_test: Test features
        y_train: Training labels
        y_test: Test labels
        models: Dictionary of models to evaluate
        params: Dict of paramter for model

    Returns:
        dict: Mapping of model name -> test r2_score
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e, sys)
