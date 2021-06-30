import os
import sys
import ctypes

if __debug__:
    pass
else:
    os.chdir(sys._MEIPASS)

icon_path = 'poly.ico'

# This bit gets the taskbar icon working properly in Windows
if sys.platform.startswith('win'):
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(u'polyfiller')