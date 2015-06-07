from loggers.system_logger import SystemLogger
import difflib 

class ResultCommands(object):
        
    # site_url for error logging (now, maybe in future we can extend it)
    def __init__(self, prev_ver, cur_ver, site_url):
        self.__prev_ver__ = prev_ver
        self.__cur_ver__ = cur_ver
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
    
    def __display_differences__(self):
        #result = difflib.HtmlDiff().make_table(self.__prev_ver__.split('\n'),
        #                   self.__cur_ver__.split('\n'))
        result_list = list(difflib.Differ().compare(self.__prev_ver__.splitlines(1), self.__cur_ver__.splitlines(1)))
        result = ''.join(result_list)
        return "\n" + result
    
    def __commands__(self):
        return  {
                 'MESSAGE' : self.__message__,
                 'DISPLAY_DIFFERENCES' : self.__display_differences__
                }
    
    