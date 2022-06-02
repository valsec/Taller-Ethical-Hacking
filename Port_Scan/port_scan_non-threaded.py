import argparse
import socket


def connection_scan(target_ip, target_port):
    try:
        con_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con_socket.connect((target_ip, target_port))
        con_socket.send(b'Banner_query\r\n')
        print(f"[+] {target_port}/tcp open")
    except OSError:
        print(f"[-] {target_port}/tcp closed")
    finally:
        con_socket.close()


def port_scan(target, port):
    try:
        target_ip = socket.gethostbyname(target)
        connection_scan(target_ip, int(port))
    except OSError:
        print(f"[^] Cannot resolve {target}: Unknow host")
        return


def all_port_scan(target):
    try:
        target_ip = socket.gethostbyname(target)
        for i in range(1, 65536):
            connection_scan(target_ip, i)
    except OSError:
        print(f"[^] Cannot resolve {target}: Unknow host")


def argument_parser():
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP Address and list of ports or "
                                                 "all ports scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs="?", help="Host IP Address")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-Separated por list. surch as '25,80,8080' or "
                                                         "all for all ports.")
    var_args = vars(parser.parse_args())
    return var_args


if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"]
        print(f"[*] Scanning {host}")
        if 'all' in ports:
            all_port_scan(host)
        else:
            ports = ports.split(',')
            for port in ports:
                port_scan(host, port)
    except AttributeError:
        print("Error. Please providen the ommand-line arguments before running.")
