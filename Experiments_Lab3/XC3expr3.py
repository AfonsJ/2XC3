# Define XC3Node class to represent nodes in an XC3-Tree
class XC3Node:
    def __init__(self, degree):
        # Initialize node with given degree and empty children list
        self.degree = degree
        self.children = []
    
    # Add children to the node based on its degree
    def add_children(self):
        for i in range(self.degree):
            # If i > 1, child degree is i - 2, otherwise child degree is 0
            if i > 1:
                child_degree = i - 2
            else:
                child_degree = 0
            # Create child node with calculated degree and add children recursively
            child = XC3Node(child_degree)
            child.add_children()
            # Add child node to parent node's children list
            self.children.append(child)
    
    # Calculate the height of the node by recursively finding the maximum height of its children
    def height(self):
        if not self.children:
            return 0
        return max(child.height() for child in self.children) + 1
    
    # Calculate the number of nodes in the node's subtree by recursively summing the number of nodes in its children
    def num_nodes(self):
        if not self.children:
            return 1
        return sum(child.num_nodes() for child in self.children) + 1
    
# Create XC3-Trees with degrees 0 to 25 and print their degree, height, and number of nodes
for i in range(26):
    root = XC3Node(i)
    root.add_children()
    height = root.height()
    num_nodes = root.num_nodes()
    print(f"Degree {i} XC3-Tree - Height: {height}, Num Nodes: {num_nodes}")
