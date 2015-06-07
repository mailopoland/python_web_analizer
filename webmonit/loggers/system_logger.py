from logger import Logger
from settings.settings import Settings

class SystemLogger(Logger):

    def __init__(self):
        settings = Settings()
        super(SystemLogger, self).__init__(settings.system_log_name(), settings.system_log_name() + ".log")
    
    def report_error(self, txt):
        self.logger.error(txt)
        
    def report_debug(self, txt):
        self.logger.debug(txt) 