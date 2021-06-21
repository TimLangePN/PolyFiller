import PySimpleGUI as sg
import sys
from fastkml import kml
from main import init

def validate_content(event, values, window):
    kml_path = values['file']
    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        sys.exit()
    if event == 'Start' and kml_path == '':
        sg.popup('KML can not be empty')
        return
    elif event == 'Start' and values['points'] == '':
        sg.popup('Amount of Points can not be empty')
        return
    try:
        k = kml.KML()
        with open(kml_path, 'rt', encoding="utf-8").read() as file:
            k.from_string(file)
    except:
        sg.popup('Could not read KML file')
        return
    try:
        amount_of_points = int(values['points'])
    except:
        window['points'].update(values['points'][:-len(values['points'])])
        sg.popup('Only insert numbers')
        return
    else:
        init(amount_of_points, kml_path)