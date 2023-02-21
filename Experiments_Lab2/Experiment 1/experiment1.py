import graph
import random

# i nodes, j edges
def create_random_graph(i,j):
    randg = graph.Graph(i)
    maxe = int(round((i*(i-1))/2))
    rande = []

    # Checking if edge value doesn't surpass max num of edges
    if j > maxe:
        j = maxe

    # creating a random edge
    def make_edge():
        rand1 = random.randint(0,(i-1))
        rand2 = random.randint(0,(i-1))
        while rand1 == rand2:
            rand1 = random.randint(0,(i-1))
            rand2 = random.randint(0,(i-1))
        add_edge([rand1,rand2])

    # Checking if edge already was created
    def add_edge(e):
        if e not in rande:
            rande.append(e)
        else:
            make_edge()

    # running the make_edge function, followed by finally adding the edge to our graph instance
    for t in range(j):
        make_edge()

    for edge in rande:
        randg.add_edge(edge[0],edge[1])

    # return the graph
    return randg


#additional function used during testing to print the graph with a function added to the graph class
def print_graph(g):
    print("Graph : ")
    g.list_nodes()



g = create_random_graph(10,4)
print_graph(g)