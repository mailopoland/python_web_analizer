import os

class Settings(object):
    
    #return parh to parent dir (webmonitoring dir)
    def __main_path__(self):
        return os.path.join( os.path.dirname(os.path.realpath(__file__)), os.path.pardir) + "/"
    
    def __daemon_time_file__(self):
        return self.settings_dir() + '.daemon_time'
    
    def settings_dir(self):
        return self.__main_path__() + 'settings/'
    
    def pid_name(self):
        return '.webanalizer.pid'
    
    def process(self):
        return self.temp_dir() + self.pid_name()
    
    def result(self):
        return self.__main_path__() + 'result/webanalizer.log'
    
    def result_dir(self):
        return self.__main_path__() + 'result/'
    
    def webdaemon(self):
        return self.__main_path__() + 'webdaemon/webdaemon.py'
    
    def instructions(self):
        return self.__main_path__() + 'settings/instructions.settings'
    
    def temp_dir(self):
        return self.__main_path__() + 'temp/'
    
    def system_log_name(self):
        return "system_logs"
    
    # change in production version
    def is_debug(self):
        return True;
    
    
    def set_daemon_time(self, new_value):
        try:
            with open(self.__daemon_time_file__(), "w+") as f:
                f.write(new_value)
        except Exception:
            return "Error during set new value\n"
        return "Set new value correct\n"
            
    def get_daemon_time(self):
        try:
            # write current site version (for next checks)
            with open(self.__daemon_time_file__(), "r") as f:
                content = f.readlines()
            return int(content[0])
        except Exception:
            # default vale: 1 minute
            return 60