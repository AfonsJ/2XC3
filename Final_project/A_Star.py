import SPAlgorithm
import SPappr
class A_Star(SPAlgorithm.SPAlgorithm):
    def __init__(self):
        self.__adaptee = SPappr.a_star
        self.h = None
    
    def set_heuristic(self, hf):
        self.h = hf

    def calc_sp(self, graph, source, dest):
        def total_dist(dist):
            total = 0
            for key in dist.keys():
                total += dist[key]
            return total
        
        if self.h == None:
            print("Heuristic Function not set.")
            return None
        
        a,b = self.__adaptee(graph, source, dest, self.h)
        return total_dist(a)
    