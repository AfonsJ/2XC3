import heapq

def a_star(G, s, d, h):
    # Initialize the open set with the start node and its f_score
    open_set = [(h[s], s)]
    open_set_nodes = {s}
    
    # Initialize the closed set as an empty set
    closed_set = set()
    
    # Initialize the g_score and f_score dictionaries
    g_score = {node: float('inf') for node in G}
    g_score[s] = 0
    f_score = {node: float('inf') for node in G}
    f_score[s] = h[s]
    
    # Initialize the predecessor dictionary
    predecessors = {node: None for node in G}
    
    while open_set:
        # Get the node with the lowest f_score from the open set
        _, current = heapq.heappop(open_set)
        open_set_nodes.remove(current)
        
        # If the current node is the destination node, return the predecessor dictionary and the shortest path
        if current == d:
            return predecessors, f_score[d]
        
        # Add the current node to the closed set
        closed_set.add(current)
        
        # Iterate over the neighbors of the current node
        for neighbor, weight in G[current].items():
            if neighbor in closed_set:
                continue
            
            # Calculate the tentative g_score for the neighbor
            tentative_g_score = g_score[current] + weight
            
            # If the tentative g_score is better than the current g_score of the neighbor
            if tentative_g_score < g_score[neighbor]:
                # Update the g_score and f_score of the neighbor
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]
                
                # Update the predecessor of the neighbor
                predecessors[neighbor] = current
                
                # Add the neighbor to the open set if it's not already in it
                if neighbor not in open_set_nodes:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_nodes.add(neighbor)

    # If the destination node is not reachable, return None
    return None



def reconstruct_path_a_star(predecessors, source, destination):
    # Initialize an empty list to store the path
    path = []
    
    # Start with the destination node as the current node
    current = destination
    
    # Iterate backwards through the predecessor dictionary until the source node is reached
    while current != source:
        # Add the current node to the path
        path.append(current)
        
        # Update the current node to its predecessor in the dictionary
        current = predecessors[current]
    
    # Add the source node to the path, completing it
    path.append(source)
    
    # Reverse the path so that it goes from the source to the destination, and return it
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

# # Now we call the a_star function passing it the nessecary variables.

# predecessors, shortest_path = a_star(G, s, d, h)

# # Print the values
# print("Predecessor Dictionary: " + str (predecessors))
# print("Total Weight: "+str(shortest_path))

# # Reconstruct the path from the predecessor dictionary and print.
# path_list = reconstruct_path(predecessors, s, d)
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

# 