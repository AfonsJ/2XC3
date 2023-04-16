import math
from math import radians

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Earth's radius in kilometers
    earth_radius = 6371

    # Calculate the distance
    distance = earth_radius * c
    return distance

# Creates a dictionary that serves as the heuristic funcition for the A* algorithm
def create_distance_dict(stations, destination_id):
    distance_dict = {}
    # source = stations[source_id]
    destination = stations[destination_id]

    dest_lat = radians(float(destination[0]))
    dest_lon = radians(float(destination[1]))

    for station_id, station in stations.items():
        station_lat = radians(float(station[0]))
        station_lon = radians(float(station[1]))

        distance = haversine(station_lat, station_lon, dest_lat, dest_lon)
        distance_dict[str(station_id)] = distance  # Convert the station_id to a string

    return distance_dict


