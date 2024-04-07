import googlemaps.client
from haversine import haversine

import googlemaps

#def find_closest_bike_rack(google_api_key, origin):

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
    distance = haversine(location1, location2, unit=haversine.Unit.M)
    print("Distance = " + distance)
    return distance