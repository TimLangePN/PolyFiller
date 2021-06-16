from fastkml import kml
import sys

def parse_kml(file):
    try:
    # Instantiate a KML Object
        k = kml.KML()

        # Read sample KML residing in data dir on root
        with open(file, 'rt', encoding="utf-8") as myfile:
            doc = myfile.read()

        # Assign the above data to the instantiated KML object
        k.from_string(doc)

        # Create a list of all the features in the KML
        return list(k.features())
    except:
        sys.exit('KML File not found')
