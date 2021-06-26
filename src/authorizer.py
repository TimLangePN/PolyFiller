from pathlib import Path
import PySimpleGUI as sg      

import os

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
    if not key:
        PromptUserForKey()

def PromptUserForKey():
    layout = [[sg.Text('Please enter your Mapbox key')],      
                    [sg.InputText()],      
                    [sg.Submit(), sg.Cancel()]]      

    window = sg.Window('Window Title', layout, icon='poly.ico')    

    event, values = window.read()    
    window.close()

    text_input = values[0]    
    sg.popup('You entered', text_input)