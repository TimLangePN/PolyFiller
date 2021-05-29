from fastkml import kml
import geojson
import shapely.wkt

# Instantiate a KML Object
k = kml.KML()

# Read sample KML residing in data dir on root
with open('C:\Github\PolyFiller\data\AT_Dornbirn.kml', 'rt', encoding="utf-8") as myfile:
    doc=myfile.read()

# Assign the above data to the instantiated KML object
k.from_string(doc)

# Create a list of all the features in the KML
features = list(k.features())

primary_nested_features = list(features[0].features())

for feature in primary_nested_features:
    g1 = shapely.wkt.loads(feature.geometry.wkt)
    g2 = geojson.Feature(geometry=g1, properties={})
    print(g2.geometry.coordinates[0])