from logger import Logger
from settings.settings import Settings

class SystemLogger(Logger):

    def __init__(self):
        settings = Settings()
        super(SystemLogger, self).__init__(settings.system_errors_name(), settings.system_errors_name())
    
    def report_error(self, txt):
        self.logger.error(txt)
        
        