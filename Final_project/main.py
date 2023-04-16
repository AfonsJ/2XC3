import ShortPathFinder
import WeightedGraph
import Dijkstra
import HeuristicGraph
import A_Star
import Bellman_Ford

# Global source_node node and destination node
source_node = 0
destination_node = 4

def heuristic_function(destination_node_node):
    # Heuristic Function Definition
    return abs(source_node - destination_node_node)


def main():
    # Initialize the ShortPathFinder instance
    path_finder = ShortPathFinder.ShortPathFinder()

    # Create a WeightedGraph instance and add nodes and edges
    graph_weighted = WeightedGraph.WeightedGraph()
    graph_weighted.add_node(0)
    graph_weighted.add_node(1)
    graph_weighted.add_node(2)
    graph_weighted.add_node(3)
    graph_weighted.add_edge(0, 1, 1)
    graph_weighted.add_edge(1, 2, 2)
    graph_weighted.add_edge(2, 3, 1)
    graph_weighted.add_edge(0, 3, 4)
    graph_weighted.add_node(4)
    graph_weighted.add_edge(3, 4, 2)

    graph_heuristic = HeuristicGraph.HeuristicGraph()
    graph_heuristic.add_node(0)
    graph_heuristic.add_node(1)
    graph_heuristic.add_node(2)
    graph_heuristic.add_node(3)
    graph_heuristic.add_edge(0, 1, 1)
    graph_heuristic.add_edge(1, 2, 2)
    graph_heuristic.add_edge(2, 3, 1)
    graph_heuristic.add_edge(0, 3, 4)
    graph_heuristic.add_node(4)
    graph_heuristic.add_edge(3, 4, 2)


    # Set the heuristic function
    graph_heuristic.set_heuristic(heuristic_function)

    # This is a visual of the graph with nodes 0, 1, 2, 3 and weights in ( )
    #    0 ---(1)---> 1 ---(2)---> 2 ---(1)---> 3 ---(2)---> 4


    # Set the graph and algorithm in the ShortPathFinder instance
    path_finder.set_graph(graph_weighted)
    path_finder.set_algorithm(Dijkstra.Dijkstra)

    # Calculate the shortest path from node 0 to node 4 using Dijkstra's
    total_distance_dijkstra = path_finder.calc_short_path(source_node, destination_node)
    print(f"Dikstra: The total distance from node {source_node} to node {destination_node} is {total_distance_dijkstra}")
    

    # Set the graph and algorithm in the ShortPathFinder instance
    path_finder.set_graph(graph_heuristic)
    # Change the algorithim to use
    path_finder.set_algorithm(A_Star.A_Star)

    path_finder._algo.set_heuristic(graph_heuristic.get_heuristic())


    # Calculate the shortest path from node 0 to node 4 using A* algorithm
    total_distance_a_star = path_finder.calc_short_path(source_node, destination_node)
    print(f"A*: The total distance from node {source_node} to node {destination_node} is {total_distance_a_star}")

    # Set the graph and algorithm in the ShortPathFinder instance
    path_finder.set_graph(graph_weighted)
    path_finder.set_algorithm(Bellman_Ford.Bellman_Ford)

    # Calculate the shortest path from node 0 to node 4 using Bellman-Ford algorithm
    total_distance_bellman_ford = path_finder.calc_short_path(source_node, destination_node)
    print(f"Bellman-Ford: The total distance from node {source_node} to node {destination_node} is {total_distance_bellman_ford}")


if __name__ == "__main__":
    main()
