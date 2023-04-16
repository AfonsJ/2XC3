import SPAlgorithm
import Graph
class ShortPathFinder:
    
    def __init__(self):
        self._graph = None
        self._algo = None

    def calc_short_path(self, source:int, dest:int):
        return self._algo.calc_sp(self._graph, source, dest)
        
    def set_graph(self, graph:Graph):
        self._graph = graph

    def set_algorithm(self, algorithm:SPAlgorithm):
        self._algo = algorithm()