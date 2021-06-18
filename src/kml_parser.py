from fastkml import kml
def parse_kml(file):
# Instantiate a KML Object
    k = kml.KML()

    # Read sample KML residing in data dir on root
    with open(file, 'rt', encoding="utf-8") as myfile:
        doc = myfile.read()

    # Assign the above data to the instantiated KML object
    k.from_string(doc)

    # Create a list of all the features in the KML
    return list(k.features())