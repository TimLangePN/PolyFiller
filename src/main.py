from inspect import Attribute
import geojson
from fastkml import kml
from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
import json

with open(".vscode\\load.json", "r") as jsonfile:
    jsonloader = json.load(jsonfile)
    kmlpath = (jsonloader["kmlpath"])

# Instantiate a KML Object
k = kml.KML()

# Read sample KML residing in data dir on root
with open(kmlpath, 'rt', encoding="utf-8") as myfile:
    doc = myfile.read()

# Assign the above data to the instantiated KML object
k.from_string(doc)

# Create a list of all the features in the KML
features = list(k.features())

# Store all nested features in a list
nested_features = list(features[0].features())

coordinates_list = []

# Get polygon and calculate random points inside polygon
for feature in nested_features:
    random_coordinates_list = generate_random_coordinates(5, feature.geometry)
    for coordinates in random_coordinates_list:
        coordinates_list.append(coordinates)

write_header('Freiburg')

for coordinates in coordinates_list:
    street_name = resolve_street_name(str(coordinates.y), str(coordinates.x))
    write_rows(coordinates, 'Freiburg', street_name)