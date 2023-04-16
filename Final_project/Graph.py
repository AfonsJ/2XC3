# Graph Interface
class Graph:
    def get_adj_nodes(self, node:int) -> list[int]:
        pass

    def add_node(self, node:int):
        pass

    def add_edge(self, start:int, end:int, w:float):
        pass

    def get_num_of_nodes(self) -> int:
        pass

    def w(self, node:int) -> float:
        pass 
