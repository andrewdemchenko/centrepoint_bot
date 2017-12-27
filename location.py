from geopy.geocoders import Nominatim

def validate_location(location):
    return geolocator.geocode(location)

def find_near(location):
    print(location.address)
    print((location.latitude, location.longitude))
    print(location.raw)

geolocator = Nominatim()