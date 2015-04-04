import os

class Settings():
    
    def main_path(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/"
    
    def process(self):
        return Settings().main_path() + 'temp/webanalizer.pid'
    
    def result(self):
        return Settings().main_path() + 'result/webanalizer.log'
    
    def webdeamon(self):
        return Settings().main_path() + 'webdeamon.py'