from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Yas Island, Abu Dhabi, United Arab Emirates")

print(location.address)
print((location.latitude, location.longitude))
print(location.raw)