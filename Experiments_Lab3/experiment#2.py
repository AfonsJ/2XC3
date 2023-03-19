import random
import bst
import lab6
import sys
import matplotlib.pyplot as plt


# We are running an experiment where we will create an RBTs & BSTs 
# based on perfectly sorted lists of length size of 10 000 


# Using create random list function from sorting lab
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]



# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# Swap Function
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]



def experiment2():
    NUM_OF_SWAPS = 200
    list_swaps = [i for i in range(0, 10001, NUM_OF_SWAPS)] # Swaps for each run
    list_height_diff = []
    bst_tree_height = 10000 # Worst possible case for BST tree
    for each_swap in list_swaps:
        L = create_near_sorted_list(10000, 20000, each_swap)
       
        # Create both trees
        bst_tree = bst.BSTTree()
        rb_tree = lab6.RBTree()
        
        # Insert into both trees
        for value in L:
            # Inserting into a BST a perfectly sorted list will create the worst possible type of tree
            # because searching for a node involves traversing the height of the tree, and in this case, 
            # the height is the same as the number of nodes, so in this experiment we avoid reaching/surpassing 
            # the recursion limit by not inserting a perfectly sorted list into the tree.
            rb_tree.insert(value)
            if each_swap >= 200: 
                bst_tree.insert(value)
            else:
                bst_tree_height = 10000 # We say the height is worst case to avoid max recursion limit
            
        if each_swap >= 200: 
            bst_tree_height = bst_tree.get_height()
        else:
            bst_tree_height = 10000 # We say the height is worst case to avoid max recursion limit
        # Calculate height difference
        list_height_diff.append(abs(bst_tree_height - rb_tree.get_height()))
    print(list_height_diff)



    plt.plot(list_swaps, list_height_diff, 'o-', label='Average height difference')
    plt.xlabel('Number of swaps')
    plt.ylabel('Absolute height difference')
    plt.title('Comparison of BST and RBT for near-sorted lists')
    plt.legend()
    plt.show()


sys.setrecursionlimit(10000)
experiment2()
