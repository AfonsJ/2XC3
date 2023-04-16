import csv

def parse_stations(file_path):
    stations = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station_id = int(row['id'])
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            total_lines = int(row['total_lines'])
            stations[str(station_id)] = (latitude, longitude, total_lines)
    return stations

# stations = parse_stations('london_stations.csv')
# print(stations)