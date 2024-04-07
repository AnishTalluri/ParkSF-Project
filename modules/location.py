#import googlemaps.client
from haversine import haversine, Unit

#import googlemaps
import database_operation
from geopy.geocoders import Nominatim
#from geopy.geocoders import ip

geolocator = Nominatim(user_agent="parkSF")
#locator = ip.IpGeocoder()
# def get_user_location():
#     location = locator('me')
#     ip.Ip
#     print(location)
#     return (location.latitude, location.longitude)

def translate_address_to_coordinates(origin_address):
    location = geolocator.geocode(origin_address)
    #location = get_user_location()
    latitude = location.latitude
    longitude = location.longitude
    return (latitude, longitude)

def find_closest_bike_rack(origin_address):
    location = translate_address_to_coordinates(origin_address)

    bikeData = database_operation.bike_get_all_information_neurelo()
    minimum_distance = -1
    minimum_bike = None
    all_bikes = []
    for bike in bikeData:
        destination_coordinates = (bike["LAT"], bike["LON"])
        print(destination_coordinates)
        if destination_coordinates[0] == '""' or destination_coordinates[1] == '""' or destination_coordinates[0] == "0" or destination_coordinates[1] == "1":
            continue
        destination_coordinates_float = (float(destination_coordinates[0]), float(destination_coordinates[1]))
        this_distance = calculate_distance(location, destination_coordinates_float)
        all_bikes.append((this_distance, bike["ADDRESS"]))

    sorted_all_bikes = sorted(all_bikes, key=lambda x: x[0])
    
    return sorted_all_bikes
    max = 50
    for (distance, bikeInfo) in sorted_all_bikes:
        if max <= 0:
            break
        print("Distance is " + str(distance) + " and Address is " + bikeInfo["ADDRESS"])
        max-=1
    
    return True
        
def calculate_distance_google(google_api_key, origin, destination):
    client = googlemaps.client(google_api_key)
    travel_mode = "biking"
    distance_matrix = client.distance_matrix(origin, destination, travel_mode=travel_mode)

    try:
        distance = distance_matrix["rows"][0]["elements"][0]["distance"]["value"]
        time = distance_matrix["rows"][0]["elements"][0]["duration"]["value"]
        print(f"Distance between {origin} and {destination}: {distance} meters")
        print(f"Estimated travel time: {time} seconds")
        return (distance, time)
    except (KeyError, IndexError):
        # Handle potential errors like missing data or invalid requests
        print("Error: Could not retrieve distance or time information.")
        return -1
    
def calculate_distance(location1, location2):
    distance = haversine(location1, location2, unit=Unit.MILES)
    print("Distance = " + str(distance))
    return distance