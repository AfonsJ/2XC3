import SPAlgorithm
import Graph

class Bellman_Ford(SPAlgorithm.SPAlgorithm):
    def calc_sp(self, graph:Graph, source:int, dest:int):
        # Function for total distance
        def total_dist(dist):
            total = 0
            for key in dist.keys():
                total += dist[key]
            return total

        G = graph    
        pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {} #Distance dictionary
        nodes = list(G.adj.keys())

        #Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        #Meat of the algorithm
        for _ in range(G.number_of_nodes()):
            for node in nodes:
                for neighbour in G.adj[node]:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node

        return total_dist(dist)