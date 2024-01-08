import os
import logging
import argparse
from get_data import read_config_file, get_data

# def load_data(config_path: str) -> None:
def load_data(config_path):
    """
    Load the data and replace space to _ from column name and saves it to raw data folder.
    Args:
        config_path: path to data path
    Returns:
        None
    """

    try:
        config = read_config_file(config_path)
        df = get_data(config_path)
        new_cols = [col.replace(" ", "_") for col in df.columns]
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        df.to_csv(raw_data_path, index=False, header=new_cols)

    except Exception as e:
        logging.error("Error loading data in src/load_data/load_data: %s", e)
        raise e

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    load_data(parsed_args.config)
