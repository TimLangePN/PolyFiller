from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="PolyFiller")


def get_street(lat, lon):
    location = geolocator.reverse(lat+","+lon)
    rawstring = location._raw['address']
    return rawstring['road']


def get_city(lat, lon):
    location = geolocator.reverse(lat+","+lon)
    rawstring = location._raw['address']
    if 'town' in rawstring:
        return rawstring['town']
    elif 'city' in rawstring:
        return rawstring['city']

# currently takes road and town from raw geopy data and returns it to the location variable
# need to check on why this is randomly timing out, maybe loop through location instead of calling it individually
