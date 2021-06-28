from mapbox import Geocoder
from authorizer import *
import sys

mapbox_api_key = TryGetKeyFile()
geocoder = Geocoder(access_token=mapbox_api_key)

def resolve_street_name(y, x):
    lat_lon = [y, x]
    if lat_lon:
        response = geocoder.reverse(lat = y, lon = x)
        response_gjson = response.geojson()
        street_name = response_gjson['features'][0]['text']
        return street_name
    else:
        sys.exit('Coordinates cannot be empty')