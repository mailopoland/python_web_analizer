import urllib3, os.path
from settings.settings import Settings
from webanalizer.check_commands import CheckCommands
from loggers.system_logger import SystemLogger

class PageAnalizer(object):        
    
    
    def check(self, site_url, check_cmd, result_cmd):
        last_ver_file_name = site_url.replace("/","|") + str(hash(check_cmd)) + str(hash(result_cmd))
        result_download_site = self.__download_site__(site_url, last_ver_file_name)
        # download first 
        if(result_download_site == 1):
            return 1
        # error return it
        if(result_download_site != 0):
            return result_download_site
        
        commands = CheckCommands(self.last_ver, self.cur_ver)
        try:
            x = 1
            res = eval('x+1')
            #res2 = eval('commands.site_changed()')
            #res3 = eval("SITE_CHANGED()",{"__builtins__":None},{"SITE_CHANGED()", commands.site_changed})
            
            zmienna = {
                       'SITE_CHANGED' : commands.site_changed
                       }
            
            
            res4 = eval(" SITE_CHANGED() or not(SITE_CHANGED())", {}, zmienna)
            result = eval(check_cmd, {"__builtins__":None}, zmienna)
        except Exception as e:
            SystemLogger().report_error("Error during check conditions: " + check_cmd + " for:" + site_url + " Error msg:" + e)
            result = False
        if(result == True):
            return 0
        else:
            return 1
    
    def result_cmd(self, cmd):
        
        # todo evaluate cmd and return result (you can start from it I think, not from check
        return cmd
        
    # return 0: is OK (site was download before), 1: is OK (but site didn't was download before), any_other: return msg with error
    def __download_site__(self,site_url,file_url):
        self.site_url = site_url
        http = urllib3.PoolManager()
        try:
            r = http.request('GET', site_url)
        except Exception:
            return "Error during download page " + site_url
        if(r.status != 200):
            return "Error during download page " + site_url + "  error status code: " + r.status
        # save downloaded site
        self.cur_ver = r.data
        last_file = Settings().temp_dir() + file_url
        
        # if we have last copy of this site (not first execute)
        if os.path.isfile(last_file):
            try:
                with open(last_file) as f:
                    # save old version to variable
                    self.last_ver = f.read().replace('\n', '')
            except Exception:
                return "Error during open " + last_file + ". Wrong access permissions?"
            return 0
        
        try:
            # write last_file with current site version (for next daemon iteration)
            with open(last_file, "w+") as f:
                f.write(self.cur_ver)
        except Exception:
            return "Error during save " + last_file + ". Wrong access permissions?"
        
        return 1
        
        
        