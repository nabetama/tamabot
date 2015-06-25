# -*- coding: utf-8 -*-

import logging
from logging import FileHandler, Formatter

""" logger = Logger()
logger.logger.debug("This is debug message.")
logger.logger.info("This is info message.")
logger.logger.warning("This is warning message.")
logger.logger.error("This is error message.")
logger.logger.critical("This is critical message.")
"""
class Logger(object):
    def __init__(self, *args):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(name=__name__)

        formatter = Formatter(fmt='%(asctime)s  %(message)s', datefmt='%Y/%m/%d %p %I:%M:%S')

        file_handler = FileHandler('/var/log/tamabot.log', 'a+')
        file_handler.level = logging.INFO
        file_handler.formatter = formatter
        self.logger.addHandler(file_handler)
