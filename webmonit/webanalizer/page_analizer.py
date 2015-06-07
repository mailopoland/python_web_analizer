import urllib3, os.path
from settings.settings import Settings
from webanalizer.check_commands import CheckCommands
from webanalizer.result_commands import ResultCommands

class PageAnalizer(object):        
    
    # create unique name of saved page (old state of it)
    def file_name(self, site_url, check_cmd, result_cmd):
        # put only allowed characters and add unique code (based on check and result commands)
        self.cur_file_name = site_url.replace("/","|") + str(hash(check_cmd)) + str(hash(result_cmd))
        return self.cur_file_name
    
    def check(self, site_url, check_cmd, result_cmd):
        last_ver_file_name = self.file_name(site_url, check_cmd, result_cmd)
        result_download_site = self.__download_site__(site_url, last_ver_file_name)
        # download first 
        if(result_download_site == 1):
            return 1
        # error return it
        if(result_download_site != 0):
            return result_download_site
        
        return CheckCommands(self.last_ver, self.cur_ver, self.site_url).check(check_cmd)        
    
    def result_cmd(self, cmd):
        
        return ResultCommands(self.last_ver, self.cur_ver, self.site_url).get_msg(cmd)
        
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
                    self.last_ver = f.read()
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
        
        
        