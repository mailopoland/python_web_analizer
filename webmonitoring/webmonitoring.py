import sys
from webdaemon.admin_daemon import AdminDaemon

def main(argv):
    if len(argv) == 1:
        command = argv[0]
        if command == 'help':
            print("Commands:\n"
                  "help | Display this screen\n"
                  "status | Display web monitoring daemon status\n"
                  "start | Start daemon"
                  "stop | Stop daemon") 
        elif command == 'status':
            print(AdminDaemon().status() + '\n')
        elif command == 'start':
            AdminDaemon().start()
        elif command == 'stop':
            AdminDaemon().stop()
        sys.exit();

    print("Run program with 'help' to display available commands\n")
    sys.exit(2)

if __name__ == "__main__":
    print("\nWeb monitoring"
          "\n--------------")
    main(sys.argv[1:])