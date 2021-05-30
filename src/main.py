import geojson
from fastkml import kml
from spatial_calculations import *
from csv_writer import *

csv_file = "C:\Github\PolyFiller\data\example.csv"
# Instantiate a KML Object
k = kml.KML()

# Read sample KML residing in data dir on root
with open('C:\Github\PolyFiller\data\AT_Dornbirn.kml', 'rt', encoding="utf-8") as myfile:
    doc = myfile.read()

# Assign the above data to the instantiated KML object
k.from_string(doc)

# Create a list of all the features in the KML
features = list(k.features())

# Store all nested features in a list
primary_nested_features = list(features[0].features())

# Get polygon and calculate random points inside polygon
for feature in primary_nested_features:
    points = generate_random_points(5, feature.geometry)
    write_data_to_csv(csv_file, points)