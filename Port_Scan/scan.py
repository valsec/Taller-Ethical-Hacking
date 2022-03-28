import sys
import socket
import pyfiglet
from datetime import datetime

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            print("Example: python3 scan.py IP")
            print("Example: python3 scan.py Hostname")
        else:
            target = socket.gethostbyname(sys.argv[1])
            print(f"{str(datetime.now())[:19]} - Scanning {target}...")
            try:
                for port in range(1,65535):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)

                    result = sock.connect_ex((target, port))
                    if result == 0:
                        print(f"Port {port} is open")
                    sock.close()

            except KeyboardInterrupt:
                print("Exiting Program")
                sys.exit()
            except socket.gaierror:
                print("Hostname not be Resolved")
                sys.exit()
            except socket.error:
                print(f"Device {target} not responding")
                sys.exit()
    else:
        print("Invalid Argument")
        print("Example: scan.py 192.168.1.5")


if __name__ == "__main__":
    
    banner = pyfiglet.figlet_format("PORT SCANER TALLER EH")
    print(banner)
    main()