import os
import pandas as pd
import numpy as np
import logging
import argparse
from sklearn.model_selection import train_test_split
from get_data import get_data, read_config_file
from load_data import load_data

def split_and_save_data(config_path):
    """
    Split data into training and test sets
    """

    config = read_config_file(config_path)
    raw_data_set = config["load_data"]["raw_dataset_csv"]
    train_data_set = config["split_data"]["train_data_path"]
    test_data_set = config["split_data"]["test_data_path"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    df = pd.read_csv(raw_data_set, sep=",")
    train, test = train_test_split(df, 
                                    test_size=split_ratio, 
                                    random_state=random_state
                                    )

    train.to_csv(train_data_set, sep=",", encoding="utf-8")
    test.to_csv(test_data_set, sep=",", encoding="utf-8")
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_and_save_data(parsed_args.config)
