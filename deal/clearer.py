import threading
import os
import win32api,win32con


key =win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',0,win32con.KEY_READ)
path = win32api.RegQueryValueEx(key,'Desktop')[0]

os.chdir(path)
#path_rem = path.split()

def fuck():
    global i
    for i in range(999999999):
        if os.path.exists(os.path.join(path,"%r.txt"%i) ):
            os.remove(os.path.join(path,"%r.txt"%i))
            print(i,"delete")


if __name__ == "__main__":
    fuck()
     
