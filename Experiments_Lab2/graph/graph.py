from collections import deque
import random

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
    
    # # Not Needed - Just print g.adj
    # # Custom function for displaying graph
    # def list_nodes(self):
    #     print(self.adj)



#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False


#Breadth First Search2
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


#Depth First Search2
def DFS2(G, node1, node2):
    visited = set()  # Initialize an empty set to keep track of visited nodes
    path = []  # Initialize an empty list to store the path from node1 to node2
    if DFS2_helperfxn(G, node1, node2, visited, path):  # Call the DFS2_helperfxn function and check if it returns True
        return path  # If the helper function found a path from node1 to node2, return the path
    else:
        return []  # Otherwise, return an empty list

#DFS2 helper fxn
def DFS2_helperfxn(G, node, node2, visited, path):
    visited.add(node)  # Add the current node to the visited set
    path.append(node)  # Add the current node to the path list
    if node == node2:  # If the current node is node2, return True (i.e., a path has been found)
        return True
    for neighbor in G.adjacent_nodes(node):  # Loop through each neighbor of the current node
        if neighbor not in visited:  # If the neighbor has not been visited
            if DFS2_helperfxn(G, neighbor, node2, visited, path):  # Recursively call the DFS2_helperfxn function with the neighbor as the new node argument
                return True  # If a path has been found, return True
    path.pop()  # If the loop completes without finding a path to node2, remove the current node from the path list
    return False  # Return False to indicate that no path has been found from the current node to node2

def BFS3(G, node1):
    # Initialize a set of visited nodes with the starting node,
    # a queue with the starting node, and a dictionary of predecessors
    # with the starting node as the key and None as the value.
    visited = {node1}
    queue = [node1]
    pred = {}
    # Loop as long as the queue is not empty
    while queue:
        # Dequeue a node from the front of the queue
        current = queue.pop(0)
        # Look at all the neighbors of the current node
        for neighbor in G.adjacent_nodes(current):
            # If a neighbor has not been visited yet, mark it as visited,
            # enqueue it, and record its predecessor in the pred dictionary.
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                pred[neighbor] = current
    # Return the pred dictionary
    return pred

def DFS3(G, node1):
    # Initialize a set of visited nodes with the starting node,
    # a stack with the starting node, and a dictionary of predecessors
    # with the starting node as the key and None as the value.
    visited = {node1}
    stack = [node1]
    pred = {}
    # Loop as long as the stack is not empty
    while stack:
        # Pop a node from the top of the stack
        current = stack.pop()
        # Look at all the neighbors of the current node
        for neighbor in G.adjacent_nodes(current):
            # If a neighbor has not been visited yet, mark it as visited,
            # add it to the stack, and record its predecessor in the pred dictionary.
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                pred[neighbor] = current
    # Return the pred dictionary
    return pred

# has cycle function
def has_cycle(G):
    marked = {node: False for node in G.adj}  # initialize all nodes as unmarked
    for node in G.adj:
        if not marked[node]:
            if dfs_cycle_helper(G, node, marked, None):
                return True
    return False


def dfs_cycle_helper(G, node, marked, parent):
    marked[node] = True
    for neighbor in G.adj[node]:
        if not marked[neighbor]:
            if dfs_cycle_helper(G, neighbor, marked, node):
                return True
        elif neighbor != parent:
            return True
    return False

# is connected function
def is_connected(G):
    marked = {node: False for node in G.adj}  # initialize all nodes as unmarked
    start_node = next(iter(G.adj))  # start BFS from any node
    q = deque([start_node])
    marked[start_node] = True
    while len(q) > 0:
        node = q.popleft()
        for neighbor in G.adj[node]:
            if not marked[neighbor]:
                marked[neighbor] = True
                q.append(neighbor)
    return all(marked.values())

#Use the methods below to determine minimum vertex covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

# Minimum Independent Set Function
def MIS(G):
    nodes = [i for i in range(len(G.adj))]
    subsets = power_set(nodes)
    max_independent_set = []
    for subset in subsets:
        is_independent_set = True
        for i in range(len(subset)):
            for j in range(i+1, len(subset)):
                if G.are_connected(subset[i], subset[j]):
                    is_independent_set = False
                    break
            if not is_independent_set:
                break
        if is_independent_set:
            if len(subset) > len(max_independent_set):
                max_independent_set = subset
    return max_independent_set


# Create Random Graph Fxn

# i nodes, j edges
def create_random_graph(i,j):
    randg = Graph(i)
    maxe = int(round((i*(i-1))/2))
    rande = []

    # Checking if edge value doesn't surpass max num of edges
    if j > maxe:
        j = maxe

    # Creating a random edge
    def make_edge():
        rand1 = random.randint(0,(i-1))
        rand2 = random.randint(0,(i-1))
        while rand1 == rand2:
            rand1 = random.randint(0,(i-1))
            rand2 = random.randint(0,(i-1))
        add_edge([rand1,rand2])

    # Checking if edge already was created
    def add_edge(e):
        if e not in rande:
            rande.append(e)
        else:
            make_edge()

    # running the make_edge function, followed by finally adding the edge to our graph instance
    for t in range(j):
        make_edge()

    for edge in rande:
        randg.add_edge(edge[0],edge[1])

    # return the graph
    return randg


# generate random graph with n nodes and density d
def generate_random_graph(n, d):
    G = Graph(n)
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < d:
                G.add_edge(i, j)
    return G

# calculate size of largest independent set
def size_of_largest_independent_set(G):
    return len(MIS(G))

# calculate size of smallest vertex cover
def size_of_smallest_vertex_cover(G):
    return len(MVC(G))



# # Not Needed - Just print g.adj
# # Additional function used during testing to print the graph with a function added to the graph class
# def print_graph(g):
#     print("Graph : ")
#     g.list_nodes()


# Uncomment the WHOLE section below....

# ###################################################################################################
# #########################TEST CODE#################################################################

# # create a new Graph with 6 nodes corresponding to the in Lab Instructions Part 1  
g = Graph(6)

g.add_edge(1, 2) # connect nodes 1 and 2
g.add_edge(1, 3) # connect nodes 1 and 3
g.add_edge(2, 4) # connect nodes 2 and 4
g.add_edge(3, 4) # connect nodes 3 and 4
g.add_edge(5, 4) # connect nodes 5 and 4
g.add_node() # add a new node 6 to the graph
g.add_edge(4, 6) # connect node 4 and node 6
#del g.adj[0] # delete node 0 from the adjacency list


# print("Graph Adjacency List: " + str(g.adj))
print("BFS:" + str(BFS2(g,3,6)))
print("DFS:" + str(DFS2(g,3,6)))
print("BFS3:"+ str(BFS3(g,1)))
print("BFS2: "+str(BFS2(g,1,6)))
# print("MVC: " + str(MVC(g)))

# rand_g = create_random_graph(10,4)
# print("Random Graph Adjacency List: " + str(rand_g.adj))

# #########################TEST CODE############################################################
# ##############################################################################################
