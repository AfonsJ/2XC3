from parse_stations import parse_stations
from parse_connections import parse_connections
from distance import create_distance_dict
from a_star import a_star, reconstruct_path_a_star
from dijkstra import dijkstra, reconstruct_path_dijkstra




def find_path(source_id , destination_id):
    
    london_stations_csv = "london_stations.csv"
    london_connections_csv = "london_connections.csv"

    # If in "London_Stations" directory, uncomment the two lines below
    # london_stations_csv = "london_stations.csv"
    # london_connections_csv = "london_connections.csv"

    # First we need to construct the graph.
    #   1. We parse necessary files and create the graph.
    stations = parse_stations(london_stations_csv)
    G = parse_connections(london_connections_csv)


    # 2. We generate the heuristic dictionary based of our source_id.
    h = create_distance_dict(stations, destination_id)
    print(h)

    # Call to the a_star function.
    predecessors_a_start, shortest_path_weight_a_star = a_star(G, source_id, destination_id, h)

    # Call to dijkstra's 
    predecessors_dijkstra, shortest_path_weight_dijkstra = dijkstra(G, source_id, destination_id)

    # Print the values for a_star
    print("a_star:")
    print("Total Time: "+str(shortest_path_weight_a_star))

    # Reconstruct the path from the predecessor dictionary and print.
    path_list = reconstruct_path_a_star(predecessors_a_start, source_id, destination_id)
    print("Path:", end=" ")
    for i in range(0, len(path_list)):
        if path_list[i] != path_list[len(path_list)-1]:
            print(str(path_list[i]), end=" -> ")
        else:
            print(path_list[i], end="\n \n")

    # Print the values for dijkstra
    print("dijkstra:")
    print("Total Time: "+str(shortest_path_weight_dijkstra))

    # Reconstruct the path from the predecessor dictionary and print.
    path_list = reconstruct_path_dijkstra(predecessors_dijkstra, source_id, destination_id)
    print("Path:", end=" ")
    for i in range(0, len(path_list)):
        if path_list[i] != path_list[len(path_list)-1]:
            print(str(path_list[i]), end=" -> ")
        else:
            print(path_list[i])
    


source_id = "1" # Id number of station 1, "Acton Town".
destination_id = "6" # Id number of station 97, "Gallions Reach".

find_path(source_id, destination_id)