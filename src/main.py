import PySimpleGUI as sg
from input_validator import *
from init import *
from authorizer import *

counter = 0

TryGetKeyFile()

sg.theme('dark black')
layout = [[sg.Text('Add a KML:')],
          [sg.Input(key='file'), sg.FileBrowse(key='file')],
          [sg.Text('Amount of Points per Polygon'), sg.Input(key='points', size=(3, None))],
          [sg.OK('Start'), sg.Cancel('Cancel')]]

window = sg.Window('PolyFiller', layout, icon=icon_path)

# Event loop to check if values are correct/filled
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        sys.exit()

    validator_status = validate_content(event, values, window)[0]
    validator_message = validate_content(event, values, window)[1]

    kml_path = values['file']

    if validator_status == False:
        sg.popup(validator_message)
    elif validator_status == True:
        amount_of_points = int(values['points'])
        init_response = init(amount_of_points, counter, kml_path)
        sg.popup(init_response)