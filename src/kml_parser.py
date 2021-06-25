from fastkml import kml
import PySimpleGUI as sg
import sys

def parse_kml(file):
    # Instantiate a KML Object
    k = kml.KML()
    # Read sample KML residing in data dir on root
    with open(file, 'rt', encoding="utf-8") as myfile:
        doc = myfile.read()
    try:
        # Assign the above data to the instantiated KML object
        k.from_string(doc)
    except:
        sg.popup('KML file is incorrect or is missing attributes')
        sys.exit()
    # Create a list of all the features in the KML
    return list(k.features())