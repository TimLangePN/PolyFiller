from inspect import Attribute
import geojson                      # Are we going to use geojson ?
from fastkml import kml
from spatial_calculations import *
from csv_writer import *
from reverse_geocoder import *
from name_resolver import *
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

# grabs the prefix from the reverse_geocoder and replaces countryname with a prefix
city_name = get_city_name(features)
country_name = get_country_prefix(str(coordinates.y), str(coordinates.x))
country_prefix = replace_country_name_to_prefix(country_name)

# Writes the header of the CSV
write_header(country_prefix, city_name)

# Loops through the coordinates and writes them with the correct values
for coordinates in coordinates_list:
    street_name = resolve_street_name(str(coordinates.y), str(coordinates.x))

    write_rows(coordinates, city_name, country_prefix, street_name)
