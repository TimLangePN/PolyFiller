import geocoder
from bootstrap import *
import sys

mapbox_api_key = retrieve_mapbox_api_key()

def resolve_street_name(y, x):
    lat_lon = [y, x]
    if not lat_lon:
        sys.exit('Coordinates cannot be empty')
    else:
        location = geocoder.mapbox([y, x], method='reverse', key=mapbox_api_key)
        street_name = location.current_result.address.partition(',')[0]
        return street_name