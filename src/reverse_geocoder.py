import geocoder

def resolve_street_name(y, x):
    location = geocoder.mapbox([y, x], method='reverse', key='sk.eyJ1IjoidGxhbmdlMzEiLCJhIjoiY2twcHdteW9mMGJ5aDJ2cXo0aGNrYXJxeiJ9.cNynn4H2BIB5WATrujzrwA')
    street_name = location.current_result.address.partition(',')[0]
    return street_name