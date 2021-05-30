from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="PolyFiller")

def get_address(lat, lon):
    location = geolocator.reverse(lat+","+lon)
    return location.address