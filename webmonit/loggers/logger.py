from settings.settings import Settings
import logging

class Logger(object):

    def __init__(self, logger_name, file_name):
        settings = Settings()
        self.logger = logging.getLogger(logger_name)
        if(settings.is_debug()):
            lvl = logging.DEBUG
        else:
            lvl = logging.INFO
        self.logger.setLevel(lvl)
        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
        # Reset the logger.handlers if it already exists.
        
        handler = logging.FileHandler(settings.result_dir() + file_name)
        handler.setFormatter(formatter)
        if self.logger.handlers:
            self.logger.handlers = []
        self.logger.addHandler(handler)
        
    def report(self, txt):
        self.logger.info(txt)
        