import heapq

def dijkstra(G, s, d):
    # Initialize the open set with the start node and its distance
    open_set = [(0, s)]

    # Initialize the distance dictionary
    distances = {node: float('inf') for node in G}
    distances[s] = 0

    # Initialize the predecessor dictionary
    predecessors = {node: None for node in G}

    while open_set:
        # Get the node with the lowest distance from the open set
        _, current = heapq.heappop(open_set)

        if current == d:
            return predecessors, distances[d]

        for neighbor, weight in G[current].items():
            tentative_distance = distances[current] + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current
                heapq.heappush(open_set, (distances[neighbor], neighbor))

    return None

#Function to reconstruct the path
def reconstruct_path_dijkstra(predecessors, source, destination):
    path = []
    current = destination

    while current != source:
        path.append(current)
        current = predecessors[current]

    path.append(source)

    return path[::-1]




# # Now we go over a short example...

# # Graph, here is a visual representation:
# #           A --1--> B --2--> C
# #           |        |        |
# #           4        5        3
# #           |        |        |
# #           v        v        v
# #           C --3--> D --1--> E
# # 
# #       - Arrows indicate the direction of edges between nodes.
# #       - Numbers next to the arrows represent the weights of the edges.


# G = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'C': 2, 'D': 5},
#     'C': {'D': 3},
#     'D': {'E': 1},
#     'E': {}
#     }

# # Start node is node A.
# s = 'A'

# # Destination node id node E.
# d = 'E'

# # Heuristic dictionary h, provides an estimate of the distance from each node to the destination node 'E'.
# h = {
#     'A': 6,
#     'B': 5,
#     'C': 2,
#     'D': 1,
#     'E': 0
#     }

# # The graph contains five nodes (A, B, C, D, and E) with directed edges 
# # and weights between them. the heuristic dictionary h provides an 
# # estimate of the distance from each node to the destination node 'E'.

# # Now we call dijkstra's function passing it the nessecary variables.

# predecessors, shortest_path = dijkstra(G, s, d)

# # Print the values
# print("Predecessor Dictionary: " + str (predecessors))
# print("Total Weight: "+str(shortest_path))

# # Reconstruct the path from the predecessor dictionary and print.
# path_list = reconstruct_path_dijkstra(predecessors, s, d)
# print("Path:", end=" ")
# for i in range(0, len(path_list)):
#     if path_list[i] != path_list[len(path_list)-1]:
#         print(str(path_list[i]), end=" -> ")
#     else:
#         print(path_list[i])

# Output:
# Predecessor Dictionary: {'A': None, 'B': 'A', 'C': 'B', 'D': 'B', 'E': 'D'}
# Total Weight: 7
# Path: A -> B -> D -> E

# G = {
#     'A': {'B': 1, 'C': 1},
#     'B': {'D': 2},
#     'C': {'D': 1},
#     'D': {'E': 3},
#     'E': {'F': 1},
#     'F': {'G': 1},
#     'G': {}
# }
# s = 'A'
# d = 'G'
# h = {
#     'A': 5,
#     'B': 4,
#     'C': 3,
#     'D': 2,
#     'E': 1,
#     'F': 0,
#     'G': 0
# }


# predecessors, shortest_path = dijkstra(G, s, d)

# # Print the values
# print("Predecessor Dictionary: " + str (predecessors))
# print("Total Weight: "+str(shortest_path))

# # Reconstruct the path from the predecessor dictionary and print.
# path_list = reconstruct_path_dijkstra(predecessors, s, d)
# print("Path:", end=" ")
# for i in range(0, len(path_list)):
#     if path_list[i] != path_list[len(path_list)-1]:
#         print(str(path_list[i]), end=" -> ")
#     else:
#         print(path_list[i])
