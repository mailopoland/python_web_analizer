import sys

from webdaemon.admin_daemon import AdminDaemon
from webanalizer.allsites_analizer import AllsitesAnalizer
from settings.settings import Settings

def main(argv):
    if len(argv) == 1:
        command = argv[0]
        if command == 'help':
            print("Run program with one of these commands:\n"
                  "check_now | Looking for changes in defined web sites now\n"
                  "help | Display this screen\n"
                  "settings | Information how to set up this application\n"
                  "start | Start daemon\n"
                  "status | Display web monitoring daemon status\n"
                  "stop | Stop daemon\n"
                  "time value | Set in seconds how often the daemon should check defined sites\n") 
        elif command == 'status':
            print(AdminDaemon().status() + '\n')
        elif command == 'start':
            AdminDaemon().start()
        elif command == 'stop':
            AdminDaemon().stop()
        elif command == 'check_now':
            print("Checking...\n")
            AllsitesAnalizer().analize()
            print("Please looking for result in 'result' folder.\n")
        elif command == 'settings':
            print("To set up this application change file 'settings/instuctions.settings' in the way described in the comments in this file.\n")
        else:
            print("Run program with 'help' to display available commands\n")
        sys.exit();
    elif len(argv) == 2:
        command = argv[0]
        if command == 'time':
            print(Settings().set_daemon_time(argv[1]))
        sys.exit();
            
            
    print("Run program with 'help' to display available commands\n")
    sys.exit()

if __name__ == "__main__":
    print("\nWeb monitoring"
          "\n--------------")
    main(sys.argv[1:])