import os

class Settings(object):
    
    #return parh to parent dir (webmonitoring dir)
    def __main_path__(self):
        return os.path.join( os.path.dirname(os.path.realpath(__file__)), os.path.pardir) + "/"
    
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