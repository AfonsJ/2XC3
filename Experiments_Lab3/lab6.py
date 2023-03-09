class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def get_uncle(self):
        return

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        # Assign the current node's left child to `new_root`.
        new_root = self.left
        
        # Check if `new_root` exists. If it doesn't, return.
        if new_root is None:
            return
            
        # Assign the current node's left child to the right child of `new_root`.
        self.left = new_root.right
        
        # If the current node's left child exists, assign the current node as the parent of the left child.
        if self.left is not None:
            self.left.parent = self
        
        # Assign the current node's parent to `new_root`.
        new_root.parent = self.parent
        
        # If the current node doesn't have a parent, assign `None` as the parent of `new_root`.
        if self.parent is None:
            new_root.parent = None
            
        # If the current node is a left child of its parent, assign `new_root` as the left child of its parent.
        elif self.is_left_child():
            self.parent.left = new_root
            
        # If the current node is a right child of its parent, assign `new_root` as the right child of its parent.
        else:
            self.parent.right = new_root
        
        # Assign the current node as the right child of `new_root`.
        new_root.right = self
        
        # Assign `new_root` as the parent of the current node.
        self.parent = new_root


    def rotate_left(self):
        # Assign the current node's right child to `new_root`.
        new_root = self.right
        
        # Check if `new_root` exists. If it doesn't, return.
        if new_root is None:
            return
            
        # Assign the current node's right child to the left child of `new_root`.
        self.right = new_root.left
        
        # If the current node's right child exists, assign the current node as the parent of the right child.
        if self.right is not None:
            self.right.parent = self
        
        # Assign the current node's parent to `new_root`.
        new_root.parent = self.parent
        
        # If the current node doesn't have a parent, assign `None` as the parent of `new_root`.
        if self.parent is None:
            new_root.parent = None
            
        # If the current node is a left child of its parent, assign `new_root` as the left child of its parent.
        elif self.is_left_child():
            self.parent.left = new_root
            
        # If the current node is a right child of its parent, assign `new_root` as the right child of its parent.
        else:
            self.parent.right = new_root
        
        # Assign the current node as the left child of `new_root`.
        new_root.left = self
        
        # Assign `new_root` as the parent of the current node.
        self.parent = new_root



class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def rotate_left(self, node):
        node.rotate_left()
        if node.parent is None:
            self.root = node

    def rotate_right(self, node):
        node.rotate_right()
        if node.parent is None:
            self.root = node

    def fix(self, node):
        # You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()
            return

        while node != None and node.parent != None and node.parent.is_red():
            parent = node.parent
            grandparent = parent.parent

            # case 1: parent is left child of grandparent
            if parent == grandparent.left:
                uncle = grandparent.right

                # case 1.1: uncle is red
                if uncle and uncle.is_red():
                    grandparent.make_red()
                    parent.make_black()
                    uncle.make_black()
                    node = grandparent
                else:
                    # case 1.2: uncle is black and node is right child of parent
                    if node == parent.right:
                        self.rotate_left(parent)
                        node = parent
                        parent = node.parent

                    # case 1.3: uncle is black and node is left child of parent
                    parent.make_black()
                    grandparent.make_red()
                    self.rotate_right(grandparent)

            # case 2: parent is right child of grandparent
            else:
                uncle = grandparent.left

                # case 2.1: uncle is red
                if uncle and uncle.is_red():
                    grandparent.make_red()
                    parent.make_black()
                    uncle.make_black()
                    node = grandparent
                else:
                    # case 2.2: uncle is black and node is left child of parent
                    if node == parent.left:
                        self.rotate_right(parent)
                        node = parent
                        parent = node.parent

                    # case 2.3: uncle is black and node is right child of parent
                    parent.make_black()
                    grandparent.make_red()
                    self.rotate_left(grandparent)

        self.root.make_black()
                    
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


# create a new RBT
tree = RBTree()

# insert some values
values = [5, 2, 7, 1, 8, 6, 9, 3, 4]
for value in values:
    tree.insert(value)
    print(tree)

# test rotations and fixes
node_3 = tree.root.left.right
node_4 = node_3.right

# perform a left rotation at node_3
node_3.rotate_left()
print("left rotation on node_3")
print(tree)

# perform a right rotation at node_7
node_7 = tree.root.right
node_7.rotate_right()
print("right rotation on node_7")
print(tree)

# introduce a red violation by setting node_4's left child to red
node_4.left = RBNode(10)
node_4.left.parent = node_4
node_4.left.make_red()
print("introduce a red violation by setting node_4's left child to red")
print(tree)

# fix the violation at node_4
tree.fix(node_4)
print("fix the violation at node_4")
print(tree)