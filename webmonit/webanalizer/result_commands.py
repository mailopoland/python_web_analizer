from loggers.system_logger import SystemLogger

class ResultCommands(object):
        
    # site_url for error logging (now, maybe in future we can extend it)
    def __init__(self, site_url):
        self.__site_url__ = site_url
    
    def get_msg(self, cmd):
        try:
            result = eval(cmd, {"__builtins__":None}, self.__commands__())
        except Exception as e:
            SystemLogger().report_error("Error during result commands: " + cmd + " for:" + self.__site_url__ + " Error msg:" + e)
            result = "Error: Cannot evaluate result action: " + cmd
        
        return result
    
    def __message__(self, txt):
        return txt
    
    def __commands__(self):
        return  {
                 'MESSAGE' : self.__message__
                }
    
    