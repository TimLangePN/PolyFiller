import PySimpleGUI as sg
from validator import *

# GUI wrapped and starts the init function
sg.theme('dark black')

layout = [[sg.Text('Add a KML:')],
          [sg.Input(key='file'), sg.FileBrowse(key='file')],
          [sg.Text('Amount of Points per Polygon'), sg.Input(key='points', size=(2, None))],
          [sg.OK('Start'), sg.Cancel('Cancel')]]

window = sg.Window('PolyFiller', layout, icon='favicon.ico')

# Event loop to check if values are correct/filled
while True:
    event, values = window.read()
    validate_content(event, values, window)