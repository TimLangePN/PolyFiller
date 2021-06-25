import PySimpleGUI as sg
import os
import sys

def value_resetter(window):
    window['file'].update('')
    window['points'].update('')


def validate_content(event, values, window):
    kml_path = values['file']

    if event == sg.WIN_CLOSED or event == 'Cancel':
        window.close()
        sys.exit()
    if event == 'Start' and kml_path == '':
        return False, 'KML can not be empty'
    elif event == 'Start' and values['points'] == '':
        return False, 'Amount of Points can not be empty'
    try:
        points = int(values['points'])
        assert points < 15
    except:
        value_resetter(window)
        return False, 'Insert an amount smaller than 15'
    try:
        assert os.path.exists(kml_path) == True
        assert kml_path.endswith('.kml') == True
    except AssertionError:
        value_resetter(window)
        return False, 'insert a valid .kml file'
    else:
        return True, ''