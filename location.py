import pandas as pd

from geopy.distance import vincenty
from geopy.geocoders import Nominatim


def validate_location(location):
    return geolocator.geocode(location)


def find_near(location):
    lat, long = location.latitude, location.longitude

    temp = ['Country', 'City', 'Street', 'Lat', 'Long', 'Time', 1000000]

    for i in data:
        distance = vincenty((lat, long), (i[3], i[4])).kilometers
        print u'{} {}\n'.format(location, distance)
        i.append(distance)

        if float(temp[6]) > distance:
            temp = i
        else:
            pass

    return temp


geolocator = Nominatim()
data = pd.read_excel('./data/location.xlsx')
data = data.as_matrix()
data = data.tolist()