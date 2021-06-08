import json

def retrieve_kml():
    with open(".vscode\\load.json", "r") as jsonfile:
        jsonloader = json.load(jsonfile)
        kmlpath = (jsonloader["kmlpath"])
        return kmlpath