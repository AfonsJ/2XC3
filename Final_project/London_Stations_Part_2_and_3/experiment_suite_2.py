import timeit

from parse_stations import parse_stations
from parse_connections import parse_connections
from a_star import a_star, reconstruct_path_a_star
from dijkstra import dijkstra, reconstruct_path_dijkstra
from distance import create_distance_dict


# Function to calculate the number of line transfers
def count_line_transfers(path, stations):
    line_transfers = 0
    
    for i in range(1, len(path)):
        current_station_lines = stations[path[i]][2]
        previous_station_lines = stations[path[i - 1]][2]
        
        if current_station_lines != previous_station_lines:
            line_transfers += 1

    return line_transfers

# Function to execute the experiments
def run_experiments(G, stations):
    results = []
    for source_id, _ in stations.items():
        for destination_id, _ in stations.items():
            if source_id == destination_id:
                continue

            h = create_distance_dict(stations, destination_id)


            # Measure the time taken by A* algorithm
            start_time = timeit.default_timer()
            for i in range(50):
                a_star(G, source_id, destination_id, h)
            end_time = timeit.default_timer()
            runtime_a_star = (end_time - start_time) / 50

            # Measure the time taken by Dijkstra's algorithm
            start_time = timeit.default_timer()
            for i in range(50):
                dijkstra(G, source_id, destination_id)
            end_time = timeit.default_timer()
            runtime_dijkstra = (end_time - start_time) / 50

            a_star_predecessor, shortest_path_weight_a_star = a_star(G, source_id, destination_id, h)
            dijkstra_predecessor, shortest_path_weight_dijkstra = dijkstra(G, source_id, destination_id)


            transfers_a_star = count_line_transfers(reconstruct_path_a_star(a_star_predecessor, source_id, destination_id), stations)
            transfers_dijkstra = count_line_transfers(reconstruct_path_dijkstra(dijkstra_predecessor, source_id, destination_id), stations)

            # Store the results
            results.append((source_id, destination_id, shortest_path_weight_a_star, runtime_a_star, transfers_a_star, shortest_path_weight_dijkstra, runtime_dijkstra, transfers_dijkstra))


    return results

# Function to analyze and present the results
def analyze_results(results, stations):
    a_star_faster_count = 0
    dijkstra_faster_count = 0
    same_performance_count = 0

    a_star_shorter_count = 0
    dijkstra_shorter_count = 0
    same_path_count = 0
    
    a_star_lesser_transfer_count = 0
    dijkstra_lesser_transfer_count = 0
    same_line_count = 0

    total_a_star_line_transfers = 0
    total_dijkstra_line_transfers = 0


    for res in results:
        source_id, destination_id, shortest_path_weight_a_star, runtime_a_star, transfers_a_star, shortest_path_weight_dijkstra, runtime_dijkstra, transfers_dijkstra = res

        if runtime_a_star < runtime_dijkstra:
            a_star_faster_count += 1
        elif runtime_dijkstra < runtime_a_star:
            dijkstra_faster_count += 1
        else:
            same_performance_count += 1
        
        if shortest_path_weight_a_star < shortest_path_weight_dijkstra:
            a_star_shorter_count += 1
        elif shortest_path_weight_dijkstra < shortest_path_weight_a_star:
            dijkstra_shorter_count += 1
        else:
            same_path_count += 1

        if transfers_a_star < transfers_dijkstra:
            a_star_lesser_transfer_count += 1
        elif transfers_dijkstra < transfers_a_star:
            dijkstra_lesser_transfer_count += 1
        else:
            same_line_count += 1

        total_a_star_line_transfers += transfers_a_star
        total_dijkstra_line_transfers += transfers_dijkstra

    total_pairs = len(results)
    a_star_faster_percentage = (a_star_faster_count / total_pairs) * 100
    dijkstra_faster_percentage = (dijkstra_faster_count / total_pairs) * 100
    same_performance_percentage = (same_performance_count / total_pairs) * 100

    a_star_shorter_percentage = (a_star_shorter_count / total_pairs) * 100
    dijkstra_shorter_percentage = (dijkstra_shorter_count / total_pairs) * 100
    same_path_percentage = (same_path_count / total_pairs) * 100

    a_star_less_transfer_percentage = (a_star_lesser_transfer_count / total_pairs) * 100
    dijkstra_less_transfer_percentage = (dijkstra_lesser_transfer_count / total_pairs) * 100
    same_line_percentage = (same_line_count / total_pairs) * 100

    print("Results summary:")
    print("A* algorithm is faster in " + str(round(a_star_faster_percentage, 2)) + "% of the cases.")
    print("Dijkstra's algorithm is faster in " + str(round(dijkstra_faster_percentage, 2)) + "% of the cases.")
    print("They had the same performance in " + str(round(same_performance_percentage, 2)) + "% of the cases.")

    print("\n")

    print("A* algorithm had a shorter path in " + str(round(a_star_shorter_percentage, 2)) + "% of the cases.")
    print("Dijkstra's algorithm had a shorter path in " + str(round(dijkstra_shorter_percentage, 2)) + "% of the cases.")
    print("They had the equal paths in " + str(round(same_path_percentage, 2)) + "% of the cases.")

    print("\n")

    print("A* algorithm had a lesser number of line transfers in " + str(round(a_star_less_transfer_percentage, 2)) + "% of the cases.")
    print("Dijkstra's algorithm had a lesser number of line transfers in " + str(round(dijkstra_less_transfer_percentage, 2)) + "% of the cases.")
    print("They had the equal number of line transfers in " + str(round(same_line_percentage, 2)) + "% of the cases.")

    print("\n")

    print("Total line transfers of A*: ", total_a_star_line_transfers)
    print("Total line transfers of Dijkstra: ", total_dijkstra_line_transfers)



# Main function to run the experiments and analyze the results
def main():
    london_stations_csv = "london_stations.csv"
    london_connections_csv = "london_connections.csv"

    stations = parse_stations(london_stations_csv)
    G = parse_connections(london_connections_csv)
    
    results = run_experiments(G, stations)
    # print(results)
    analyze_results(results, stations)

if __name__ == "__main__":
    main()
