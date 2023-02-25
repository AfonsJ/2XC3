from collections import deque

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def get_size(self):
        return len(self.adj)


#Breadth First Search
def BFS2(G, node1, node2):
    visited = set()  # Initialize an empty set to keep track of visited nodes
    queue = deque([(node1, [node1])])  # Initialize a queue with a tuple containing node1 and a list with node1 as its only element
    while queue:  # While the queue is not empty
        node, path = queue.popleft()  # Dequeue the first node and its path from the queue
        if node == node2:  # If the current node is node2
            return path  # Return the path from node1 to node2
        visited.add(node)  # Add the current node to the visited set
        for neighbor in G.adjacent_nodes(node):  # Loop through each neighbor of the current node
            if neighbor not in visited:  # If the neighbor has not been visited
                queue.append((neighbor, path + [neighbor]))  # Enqueue the neighbor and its path (which includes the current path plus the neighbor)
    return []  # If no path is found from node1 to node2, return an empty list


def DFS2(G, node1, node2):
    visited = set()  # Initialize an empty set to keep track of visited nodes
    path = []  # Initialize an empty list to store the path from node1 to node2
    if DFS2_helper(G, node1, node2, visited, path):  # Call the DFS2_helper function and check if it returns True
        return path  # If the helper function found a path from node1 to node2, return the path
    else:
        return []  # Otherwise, return an empty list

def DFS2_helper(G, node, node2, visited, path):
    visited.add(node)  # Add the current node to the visited set
    path.append(node)  # Add the current node to the path list
    if node == node2:  # If the current node is node2, return True (i.e., a path has been found)
        return True
    for neighbor in G.adjacent_nodes(node):  # Loop through each neighbor of the current node
        if neighbor not in visited:  # If the neighbor has not been visited
            if DFS2_helper(G, neighbor, node2, visited, path):  # Recursively call the DFS2_helper function with the neighbor as the new node argument
                return True  # If a path has been found, return True
    path.pop()  # If the loop completes without finding a path to node2, remove the current node from the path list
    return False  # Return False to indicate that no path has been found from the current node to node2




##############################################################
#########################TEST CODE#############################
# create a Graph object with 10 nodes
# create a graph with 6 nodes
g = Graph(6)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(5, 4)
g.add_node()  # add node 6 to the graph
g.add_edge(4, 6)  # connect node 4 to node 6




# print the adjacency list
print(g.adj)
print(BFS2(g,3,5))
print(DFS2(g,3,5))
# print(MVC(graph))
###############################################################
#########################TEST CODE#############################







