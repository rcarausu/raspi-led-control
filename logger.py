import os
import sys
import logging

from logging import StreamHandler
from logging.handlers import RotatingFileHandler


def configure_logging(path, filename):

    file_format = '%(asctime)s - %(levelname)s - %(name)s: %(message)s'

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.addHandler(_stream_handler(file_format))
    logger.addHandler(_file_handler(path, filename, file_format))


def _file_handler(path, name, file_format):
    log_path = os.path.join(path, name)
    handler = RotatingFileHandler(log_path + ".log", maxBytes=10000000, backupCount=4)
    handler.setFormatter(logging.Formatter(file_format))
    return handler


def _stream_handler(logger_file_format):
    handler = StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(logger_file_format))
    return handler