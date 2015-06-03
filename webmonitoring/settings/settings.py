import os

class Settings():
    
    #return parh to parent dir (webmonitoring dir)
    def main_path(self):
        return os.path.join( os.path.dirname(os.path.realpath(__file__)), os.path.pardir) + "/"
    
    def process(self):
        return Settings().main_path() + 'temp/webanalizer.pid'
    
    def result(self):
        return Settings().main_path() + 'result/webanalizer.log'
    
    def webdeamon(self):
        return Settings().main_path() + 'webdaemon/webdeamon.py'