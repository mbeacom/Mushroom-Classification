"""Contains method for setting up application wide logger"""
from os import path, mkdir
import sys
import logging.config
import logging

import yaml

from api.helpers import generate_enviroment_variable_yaml_loader

def setup_logging(logger_config_path, log_files_directory, 
                  env_var_tag='!ENV', default_level=logging.INFO):
    """
    Set up logger for flask app
    """

    if not path.exists(log_files_directory):
        try:
            mkdir(log_files_directory)
        except OSError as error:
            print(f'Error making logs directory: {error}.\nDefault config will be used')
            logging.basicConfig(level=default_level)


    if path.exists(logger_config_path):
        with open(logger_config_path, 'rt') as config_file:
            try:
                env_loader = generate_enviroment_variable_yaml_loader(env_var_tag)
                config = yaml.load(config_file.read(), Loader=env_loader)
                logging.config.dictConfig(config)
            except (ValueError, TypeError, AttributeError, ImportError) as error:
                print(f'Error in Logging Configuration: {error}.\nDefault config will be used')
                logging.basicConfig(level=default_level)
    else:
        print('Failed to load configuration file. Default config will be used')
        logging.basicConfig(level=default_level)
