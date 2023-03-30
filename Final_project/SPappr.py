import min_heap
import heapq

def dijkstra_approx(G, source, k):
    pred = {} # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} # Distance dictionary
    Q = min_heap.MinHeap([]) # Create a new empty min heap
    nodes = list(G.adj.keys()) # Get a list of all nodes in the graph

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf"))) # Add a new element to the min heap with key infinity
        dist[node] = float("inf") # Initialize distance to all nodes as infinity
    Q.decrease_key(source, 0) # Decrease the key of the source node to 0 and add it to the heap

    # Meat of the algorithm
    num_relaxations = {node: 0 for node in nodes} # Create a dictionary to keep track of the number of times each node has been relaxed
    while not Q.is_empty(): # While there are still nodes in the heap
        current_element = Q.extract_min() # Extract the node with the minimum distance from the heap
        current_node = current_element.value # Get the value (node ID) of the extracted element
        dist[current_node] = current_element.key # Update the distance of the current node to the extracted element's key
        if num_relaxations[current_node] == k: # If the current node has already been relaxed k times, skip it
            continue
        for neighbour in G.adj[current_node]: # For each neighbour of the current node
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]: # If the distance to the neighbour through the current node is shorter than the current best known distance to the neighbour
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour)) # Decrease the key of the neighbour to the new, shorter distance
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour) # Update the distance of the neighbour to the new, shorter distance
                num_relaxations[neighbour] += 1 # Increment the number of times the neighbour has been relaxed
                pred[neighbour] = current_node # Set the predecessor of the neighbour to the current node
    return dist # Return the distance dictionary



def bellman_ford_approx(G, source, k):
    pred = {} # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf") # Set distance to all nodes to infinity
    dist[source] = 0 # Set distance to source node to 0

    # Meat of the algorithm
    num_relaxations = {node: 0 for node in nodes} # Keep track of number of relaxations per node
    for _ in range(k): # Repeat relaxation process for k times
        for node in nodes: # For each node in the graph
            for neighbour in G.adj[node]: # For each neighbour of the node
                # If the distance to the neighbour can be improved by going through the current node
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    # If the current node has already been relaxed k times, skip this iteration
                    if num_relaxations[node] == k:
                        continue
                    # Otherwise, relax the neighbour node and update the number of relaxations for the current node
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    num_relaxations[node] += 1
                    pred[neighbour] = node # Set the current node as the predecessor of the neighbour node
    return dist # Return the distance dictionary

def a_star(G, s, d, h):
    # """
    # A* algorithm for finding the shortest path from source node s to destination node d in a directed weighted graph G
    # with a given heuristic function h.

    # :param G: the graph (in adjacency list format)
    # :param s: the source node
    # :param d: the destination node
    # :param h: the heuristic function (dictionary mapping nodes to heuristic values)
    # :return: a tuple (predecessor dictionary, shortest path)
    # """

    # Initialize distances and predecessor dictionary
    dist = {node: float('inf') for node in G}
    dist[s] = 0
    prev = {node: None for node in G}

    # Initialize priority queue with (distance + heuristic, node)
    pq = [(dist[s] + h[s], s)]
    visited = set()

    while pq:
        # Get the node with the smallest f value (distance + heuristic)
        _, u = heapq.heappop(pq)

        # If we've reached the destination, return the path
        if u == d:
            path = []
            while prev[u]:
                path.append(u)
                u = prev[u]
            path.append(s)
            return prev, list(reversed(path))

        # Otherwise, explore its neighbors
        for v, w in G[u]:
            if v in visited:
                continue
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (dist[v] + h[v], v))

        visited.add(u)

    # If we get here, there is no path from s to d
    return None, None