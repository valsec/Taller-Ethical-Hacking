import socket
import sys
import pyfiglet
from datetime import datetime

ports = open('ports.txt', 'r')

def scanner(ip):
    count = 0
    for port in ports:
        print(f"{str(datetime.now)[:19]}Connecting to {ip} in port {str(int(port))}")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((str(ip), int(port)))
            if int(port) == 80:
                sock.send(b'GET /\n\n')
                banner = str(sock.recv(1024).decode()).split('\n')
                banner = banner[2].replace('Server: ', '')
            else:
                banner = sock.recv(1024).decode()
            sock.close()
        except:
            banner = ''

        if banner != '':
            print(banner)
            count+=1
        else:
            print(f"Port {str(int(port))} is closed\n")
    if count == 0:
        print(f"Host IP: {ip} is down")


def main():
    try:
        options = sys.argv[1]

        if options == '-i':
            ip = sys.argv[2]
            scanner(ip)
        elif options == '-r':
            data = sys.argv[2]
            print(f"Scanning Network {data}/24")
            data = data.split('.')
            dat_ip = f'{data[0]}.{data[1]}.{data[2]}.'
            for i in range(1, 254):
                ip = f'{dat_ip}{i}'
                
                scanner(ip)
        elif options == '-h':
            print("Options:")
            print("\t-i IP")
            print("\t-r Network")
            print("\t-h help")
            print("\texample: python3 banner_grabbing.py -i 192.168.1.5")
            print("\texample: python3 banner_grabbing.py -r 192.168.1.0")
        else:
            print("-h for help")
    except:
        print("-h for help")


if __name__ == '__main__':
    banner = pyfiglet.figlet_format("PORT SCANER TALLER EH")
    print(banner)
    main()
