from mapbox import Geocoder
from authorizer import *
import re
import sys

mapbox_api_key = TryGetKeyFile()
geocoder = Geocoder(access_token=mapbox_api_key)

def resolve_street_name(y, x):
    lat_lon = [y, x]
    if lat_lon:
        response = geocoder.reverse(lat = y, lon = x)
        response_gjson = response.geojson()
        gjson_properties = response_gjson['features'][0]['properties']
        try:
            response_address = gjson_properties['address']
        except:
            response_address = response_gjson['features'][0]['place_name'].split(',')[0]
        return re.sub(r'[0-9]+', '', response_address).strip()
    else:       
        sys.exit('Coordinates cannot be empty')