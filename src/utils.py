import os
import pandas as pd
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging
import sys
from sklearn.model_selection import GridSearchCV
import dill

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        pd.to_pickle(obj, file_path)
        logging.info(f"Object saved to {file_path}")
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models,params):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            # Train model
            grid_search = GridSearchCV(model, param, cv=5, n_jobs=-1)
            grid_search.fit(X_train, y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(X_train, y_train)

            # Predict test data
            y_test_pred = grid_search.predict(X_test)

            # Evaluate model
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
       with open(file_path, "rb") as file_obj:
           return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)