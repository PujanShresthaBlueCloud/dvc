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
    alpha = config["estimators"]["ElasticNet"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["l1_ratio"]
    model_dir = config["model_dir"]
    target = config["base"]["target_col"]
    random_state = config["base"]["random_state"]
    train = pd.read_csv(train_data_path)
    test = pd.read_csv(test_data_path)
    train_y = train[target]
    test_y = test[target]
    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

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


    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    # Getting the scores and params.json files to write report
    params_file = config["reports"]["params"]
    scores_file = config["reports"]["scores"]

    with open(params_file, 'w') as f:
        params = {
            "alpha": alpha,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)

    with open(scores_file, 'w') as f:
        scores = {
            "mae": mae,
            "rmse": rmse,
            "r2_scores": r2
        }
        json.dump(scores, f, indent=4)

    # create a saved_models directory if not already exists
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(lr, model_path)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(parsed_args.config)