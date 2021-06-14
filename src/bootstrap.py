import json

def retrieve_kml():
    with open(".vscode\\load.json", "r", encoding="utf-8") as jsonfile:
        jsonloader = json.load(jsonfile)
        return (jsonloader["kmlpath"])

def retrieve_mapbox_api_key():
    with open(".vscode\\.secrets.json", "r", encoding="utf-8") as secret_json_file:
        secret_json_file = json.load(secret_json_file)
        return (secret_json_file["mapbox_api_key"])