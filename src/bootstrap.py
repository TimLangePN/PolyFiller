import os
import sys
import ctypes
import PySimpleGUI as sg

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    pass
icon_path = 'poly.ico'

sg.theme('dark black')

# This bit gets the taskbar icon working properly in Windows
if sys.platform.startswith('win'):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'polyfiller')