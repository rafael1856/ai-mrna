# ----- logger.py ---
# from the module import as
# from logger import Logger, get_logger
# then initilize as 
# logger = Logger()
# from any function initialize as 
# logger = get_logger()

import logging
import os
from logging.config import dictConfig
from os import path

import yaml


class Logger:
    """
    Create and configure logger

    Note: This is a singleton class for Logger
    """

    _logger = None

    def __new__(cls, *args, **kwargs):
        if not cls._logger:
            cls._logger = super().__new__(cls, *args, **kwargs)

            # Load the logging config file
            log_file_path = path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)), "logging.yml")
            with open(log_file_path, "r", encoding="UTF-8") as file_stream:
                config = yaml.safe_load(file_stream.read())
                dictConfig(config)

            cls._logger = logging.getLogger("python_logger")

        return cls._logger
