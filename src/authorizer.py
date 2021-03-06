from pathlib import Path
import sys
import PySimpleGUI as sg      
from mapbox import *
import os
from bootstrap import *

# Create hidden .key file in home dir if it does not exist. 
def TryGetKeyFile():
    home = str(Path.home())
    path = f'{home}/.polyfiller'

    if not os.path.exists(path):
        os.makedirs(path)

    file = Path(f'{path}/.key')
    file.touch(exist_ok=True)

    content = open(file)
    key = content.readline()
    while not key:
        key = PromptUserForKey()
        open(file, 'w').writelines(key)
        try:
            geocoder = Geocoder(access_token=key)
            response = geocoder.forward('Chester, NJ')
            assert response.ok == True
        except AssertionError:
            open(file, 'w').truncate()
            key = content.readline()
            sg.popup('Incorrect Mapbox key')
    return key

def PromptUserForKey():
    
    layout = [[sg.Text('Please enter your Mapbox key')],      
                    [sg.InputText()],      
                    [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('PolyFiller', layout, icon=icon_path)    

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        sys.exit()

    window.close()

    return values[0]    