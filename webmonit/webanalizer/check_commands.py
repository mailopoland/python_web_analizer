import re
from loggers.system_logger import SystemLogger

class CheckCommands(object):

    # site_url for error logging (now, maybe in future we can extend it)
    def __init__(self, prev_ver, cur_ver, site_url):
        self.__prev_ver__ = prev_ver
        self.__cur_ver__ = cur_ver
        self.__site_url__ = site_url
        
    def __site_changed__(self):
        result = self.__cur_ver__ != self.__prev_ver__
        return result
    
    def __contains__(self, txt):
        return txt in self.__cur_ver__
    
    def __contains_many__(self,txt,quantity):
        return self.__contains_many_base__(txt, quantity, self.__cur_ver__)
    
    def __contains_many_base__(self,txt,quantity,basetxt):
        i = 0
        for _ in re.finditer(txt, basetxt):
            i += 1
        return quantity == i
    
    def __in_html_el__(self,el_name,txt):
        begin = "<" + el_name + ">"
        
        begin_idx = self.__cur_ver__.find(begin)
        if(begin_idx == -1):
            return False
        
        # begin_idx have to contains index of first char after searching tag
        begin_idx += len(begin)

        
        end_idx = self.__cur_ver__[begin_idx:].find("</" + el_name + ">")
        
        if(end_idx == -1):
            return False
        
        if (end_idx == begin_idx) and (txt == ""):
            return True
        
        return self.__cur_ver__[begin_idx:-end_idx].find(txt) != -1
    
    def __in_html_el_many__(self,el_name,txt,quantity):
        begin = "<" + el_name + ">"
        
        begin_idx = self.__cur_ver__.find(begin)
        if(begin_idx == -1):
            return False
        
        # begin_idx have to contains index of first char after searching tag
        begin_idx += len(begin)

        
        end_idx = self.__cur_ver__[begin_idx:].find("</" + el_name + ">")
        
        if(end_idx == -1):
            return False
        
        if (end_idx == begin_idx) and (((txt == "") and quantity == 1) or quantity == 0):
            return True
        
        return self.__contains_many_base__(txt,quantity,self.__cur_ver__[begin_idx:-end_idx])
    
    def __commands__(self):
        return  {
                 'SITE_CHANGED' : self.__site_changed__,
                 'CONTAINS' : self.__contains__,
                 'CONTAINS_MANY' : self.__contains_many__,
                 'IN_HTML_EL' : self.__in_html_el__,
                 'IN_HTML_EL_MANY' : self.__in_html_el_many__
                }
    
    def check(self, cmd):
        try:
            result = eval(cmd, {"__builtins__":None}, self.__commands__())
        except Exception as e:
            SystemLogger().report_error("Error during check conditions: " + cmd + " for:" + self.__site_url__ + " Error msg:" + e)
            result = False
        
        if(result == True):
            return 0
        else:
            return 1
    
    