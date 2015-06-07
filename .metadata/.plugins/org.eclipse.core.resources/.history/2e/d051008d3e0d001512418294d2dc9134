import time
import sys
import os

#tell that in webmonitoring folder this module should looking for others modules
sys.path.append(os.path.join( os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from daemon import runner
from settings.settings import Settings
from webanalizer.allsites_analizer import AllsitesAnalizer

class Webdaemon(object):
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  Settings().process()
        self.pidfile_timeout = 5
            
    def run(self):
        analizer = AllsitesAnalizer()
        while True:
            # this class run settings analyzer and base on it run website's changes checker 
            analizer.analize()
            time.sleep(3)
    
app = Webdaemon()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()