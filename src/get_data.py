import os
import logging
import argparse
import yaml
import pandas

# def read_config_file(config_path: str) -> dict:
def read_config_file(config_path):
    """
    Reads the configuration file i.e, params.yaml in our case
    Args:
        config_path: path to the configuration file i.e, params.yaml in our case
    Returns:
        config: configuration all key value pairs
    """

    try:
        with open(config_path, 'r') as yaml_file:
            config = yaml.safe_load(yaml_file)

        return config
    
    except Exception as e:
        logging.error("Error getting configuration path src/get_data/read_config_file: %s", e)
        raise e

# def get_data(config_path: str) -> pd.DataFrame:
def get_data(config_path):
    """
    Gets data from the given configuration file entry point to data source.
    Args:
        config_path: The path to the configuration file params.yaml
    Returns:
        df: dataframe
    """

    try:
        logging.info("Reading configuration file")
        config = read_config_file(config_path)
        data = config["data_source"]["s3_source"]
        df = pandas.read_csv(data, sep=",", encoding="utf-8")

        return df

    except Exception as e:
        logging.error("Error in reading configuration file: %s", e)
        raise e

    


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(parsed_args.config)
