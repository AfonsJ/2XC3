import WeightedGraph
class HeuristicGraph(WeightedGraph.WeightedGraph):
    def __init__(self):
        self.adj = {}
        self.weights = {}
        self.__heuristic = {}

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

    def w(self, node1:int, node2:int):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]
    
    def set_heuristic(self, h):
        self.__heuristic = h
        
    def get_heuristic(self):
        return self.__heuristic