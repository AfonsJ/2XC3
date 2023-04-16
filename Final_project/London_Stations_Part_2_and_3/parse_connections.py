import csv

def parse_connections(file_path):
    connections = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            station1 = str(row['station1'])
            station2 = str(row['station2'])
            time = int(row['time'])

            if station1 not in connections:
                connections[station1] = {}
            connections[station1][station2] = time

            if station2 not in connections:
                connections[station2] = {}
            connections[station2][station1] = time
    return connections

# graph = parse_connections('london_connections.csv')
# print(graph)
