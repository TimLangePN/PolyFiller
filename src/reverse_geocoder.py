from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="PolyFiller")

def get_address(lat, lon):
    location = geolocator.reverse(lat+","+lon)
    streetName = location._raw['address']['road']
    cityName = location._raw['address']['town'] 

    location = streetName +"," + cityName
    return location
# currently takes road and town from raw geopy data and returns it to the location variable
# need to check on why this is randomly timing out, maybe loop through location instead of calling it individually