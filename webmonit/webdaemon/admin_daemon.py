#standard python libs
import os.path
import time

from settings.settings import Settings

class AdminDaemon(object):
    
    def is_running(self):
        return os.path.isfile(Settings().process())
    def status(self):
        if(AdminDaemon().is_running()):
            return "Daemon is running"
        else:
            return "Daemon is not running"
        
    def start(self):
        if(AdminDaemon().is_running()):
            print("Can't start because daemon is already run\n")
        else:
            if(os.system("python " + Settings().webdaemon() + " start") == 0):
                print("Daemon is starting...")
                time.sleep(0.1)
                # newline
                print("")
            else:
                print("Daemon start failed\n")
        
    def stop(self): 
        if not(AdminDaemon().is_running()):
            print("Can't stop because daemon is already stopped\n")
        else:
            if(os.system("python " + Settings().webdaemon() + " stop") == 0):
                print("Daemon is stopped\n")
            else:
                print("Daemon stop failed\n")