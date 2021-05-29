from fastkml import kml

k = kml.KML()

with open('C:\Github\PolyFiller\data\AT_Dornbirn.kml', 'rt', encoding="utf-8") as myfile:
    doc=myfile.read()


k.from_string(doc)

features = list(k.features())

print(features)