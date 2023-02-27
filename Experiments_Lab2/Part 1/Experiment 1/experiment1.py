import sys
sys.path.append('Experiments_Lab2\Part 1')
import graph
import random
#adding random graph code, has checks for multiples of the same edge
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


# Experiment Portion
# 100 nodes
# generate 1000 random graphs of each node count
def run_exp():
    results = []
    for j in range(100,1001,100):
        sl = []
        for t in range(1,11):
            edj = int(j/t)
            cyc = 0
            for i in range(1000):
                grph = create_random_graph(j,edj)
                if(graph.has_cycle(grph) == True):
                    cyc += 1
            prob = (cyc/1000) * 100
            sl.append(((str(1)+"/"+str(t)),prob))
        results.append(sl)
    return results