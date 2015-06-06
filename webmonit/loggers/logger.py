from settings.settings import Settings
import logging

class Logger(object):

    def __init__(self, logger_name, file_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(Settings().result_dir() + file_name + ".log")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def report(self, txt):
        self.logger.info(txt)
        