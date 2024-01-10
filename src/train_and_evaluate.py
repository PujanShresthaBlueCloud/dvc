import os
import pandas as pd
import numpy as np
import argparse
import logging
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import json
from get_data import read_config_file
import mlflow

def evaluate(actual, predicted):
    """
    Evaluate the model.
    Args:
        actual: ground truth
        predicted: predicted value
    Returns:
        mae: mean absolute error
        rmse: root mean squared error
        r2: r2 score
    """
    mae = mean_absolute_error(actual, predicted)
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    r2 = r2_score(actual, predicted)

    return mae, rmse, r2

def train_and_evaluate(config_path):
    """
    Train the model on the given dataset
    Args:
        config_path: path to params file
    Returns:
        saved model
    """

    # Get all the parameters from param files to train model and evaluate
    config = read_config_file(config_path)
    train_data_path = config["split_data"]["train_data_path"]
    test_data_path = config["split_data"]["test_data_path"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    model_dir = config["model_dir"]
    target = config["base"]["target_col"]
    random_state = config["base"]["random_state"]
    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)
    train_y = train[target]
    test_y = test[target]
    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

######################## MLFLOW #########################
    # connect mlflow
    mlflow_config = config["mlflow_config"]
    remote_server_uri = mlflow_config["remote_server_uri"]

    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config["experiment_name"])

    with mlflow.start_run(run_name=mlflow_config["run_name"]) as mlops_run:



        # Training data in ElasticNet model fitting and predict
        lr = ElasticNet(
            alpha=alpha,
            l1_ratio=l1_ratio,
            random_state=random_state
        )
        lr.fit(train_x, train_y)
        predicted_qualities = lr.predict(test_x)

        # evaluation
        mae, rmse, r2 = evaluate(test_y, predicted_qualities)

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        tracking_url_type_store = urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(
                lr, 
                "model", 
                registered_model_name=mlflow_config["registered_model_name"])
        else:
            mlflow.sklearn.load_model(lr, "model")
    
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(parsed_args.config)