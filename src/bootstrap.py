import json
import sys

def retrieve_kml():
    kml_input = input('Enter KML path')
    if not kml_input:
        sys.exit('Style is not supported')
    return kml_input

def retrieve_mapbox_api_key():
    with open(".vscode\\.secrets.json", "r", encoding="utf-8") as secret_json_file:
        secret_json_file = json.load(secret_json_file)
        return (secret_json_file["mapbox_api_key"])