from mapbox import *
from bootstrap import *
import sys

mapbox_api_key = retrieve_mapbox_api_key()
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

    # Turn this if and else around, if lat lon are not null we will perform the geocoder,
    # main logic first, alt cases after, what if they are not null but they are "Blabla", it would still trigger the geocoder.