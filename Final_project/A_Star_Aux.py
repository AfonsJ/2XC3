import min_heap
import HeuristicGraph
import SPAlgorithm

class A_Star(SPAlgorithm.SPAlgorithm):
    def __init__(self):
        self.h = None

    def set_heuristic(self, hf):
        self.h = hf

    def calc_sp(self, graph: HeuristicGraph.HeuristicGraph, source: int, dest: int):
        if self.h is None:
            print("Heuristic Function not set.")
            return None

        G = graph
        pred = {}  # Predecessor dictionary
        g_score = {node: float('inf') for node in G.adj}
        g_score[source] = 0

        open_set = min_heap.MinHeap([min_heap.Element(source, self.h(source))])
        open_set_nodes = {source}

        while not open_set.is_empty():
            current_element = open_set.extract_min()
            current_node = current_element.value

            if current_node == dest:
                return g_score[dest]

            open_set_nodes.remove(current_node)

            for neighbor in G.adj[current_node]:
                tentative_g_score = g_score[current_node] + G.w(current_node, neighbor)

                if tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = g_score[neighbor] + self.h(dest)
                    pred[neighbor] = current_node

                    if neighbor not in open_set_nodes:
                        open_set.insert(min_heap.Element(neighbor, f_score))
                        open_set_nodes.add(neighbor)

        return None
