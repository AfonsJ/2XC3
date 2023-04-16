import Graph

class WeightedGraph(Graph.Graph):

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def get_adj_nodes(self, node:int):
        return self.adj[node]

    def add_node(self, node:int):
        self.adj[node] = []

    def add_edge(self, start:int, end:int, w:float):
        if end not in self.adj[start]:
            self.adj[start].append(end)
        self.weights[(start, end)] = w

    def get_num_of_nodes(self):
        return len(self.adj)

    # w method, returns the weight of an edge between 2 nodes
    def w(self, node1:int, node2:int):
        # returns the weight between two nodes, if there does not exist an edge between the two nodes
        # return float("inf")
        return self.weights.get((node1, node2), float("inf"))