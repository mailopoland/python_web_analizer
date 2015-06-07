import time
import sys
import os

# tell that in webmonitoring folder this module should looking for others modules
sys.path.append(os.path.join( os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

from daemon import runner
from settings.settings import Settings
from webanalizer.allsites_analizer import AllsitesAnalizer
from loggers.system_logger import SystemLogger

class Webdaemon(object):
    
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.settings = Settings()
        self.pidfile_path =  self.settings.process()
        self.pidfile_timeout = 5
            
    def run(self):
        log = SystemLogger()
        analizer = AllsitesAnalizer()
        while True:
            log.report("Daemon run checking iteration")
            # this class run settings analyzer and base on it run website's changes checker 
            analizer.analize()
            repeart_time = self.settings.get_daemon_time()
            log.report_debug("Loading repeart time for daemon, value: " + str(repeart_time))
            time.sleep(repeart_time)
    
app = Webdaemon()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()