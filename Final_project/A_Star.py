import SPAlgorithm
import A_Star_Aux  # Import the modified A_Star implementation

class A_Star(SPAlgorithm.SPAlgorithm):
    def __init__(self):
        self.__adaptee = A_Star_Aux.A_Star()  # Create an instance of the A_Star_Aux class
        self.h = None
    
    def set_heuristic(self, hf):
        self.h = hf
        self.__adaptee.set_heuristic(hf)  # Set the heuristic for the A_Star_Aux instance

    def calc_sp(self, graph, source, dest):
        if self.h == None:
            print("Heuristic Function not set.")
            return None
        
        # Call the calc_sp method of the A_Star_Aux instance
        total_distance = self.__adaptee.calc_sp(graph, source, dest)
        return total_distance
