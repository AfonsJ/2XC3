import random
import graph 
import experiment1 
import copy
import matplotlib.pyplot as plt


N = 8


def approx1(G):
    C = set()
    # Make a copy of the graph
    G_copy = copy.deepcopy(G)
    while True:#while True
        v = max(G_copy.adj, key=lambda x: len(G_copy.adj[x])) #find which node has the longest adj list
        C.add(v)
        for neighbor in G_copy.adj[v]:
            G_copy.adj[neighbor].remove(v)
        del G_copy.adj[v]
        if is_vertex_cover(G_copy,C):
            return C


def approx2(G):
    C = set()
    # Make a copy of the graph
    G_copy = copy.deepcopy(G)
    while True:
        #Select a vertex randomly from G which is not already in C
        v = random.choice(list(set(G_copy.adj) - C))#set of all nodes minus the C set e.g.set(G.adj) = {1,2,3,4} - C = {3} = {1,2,4}... list() converts to [1,2,4]
        C.add(v)
        if is_vertex_cover(G_copy,C):
            return C


def approx3(G):
    C = set()
    # Make a copy of the graph
    G_copy = copy.deepcopy(G)
    while True:
        #Select a random edge from the graph (u,v)

        #Create a list holding all the edges in G
        edge_list = []
        for u in G_copy.adj:
            for v in G_copy.adj[u]:
                (u,v) = (u,v)
                edge_list.append((u,v))
        (u,v) = random.choice(edge_list)
        C.add(u)
        C.add(v)
        for neighbor in G_copy.adj[u]:
            G_copy.adj[neighbor].remove(u)
        del G_copy.adj[u]
        for neighbor in G_copy.adj[v]:
            G_copy.adj[neighbor].remove(v)
        del G_copy.adj[v]
        if is_vertex_cover(G_copy,C):
            return C

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True


def potentialExperiment():
    m_list = [1,5,10,15,20,25,30]
    approx1_expected = {}
    approx2_expected = {}
    approx3_expected = {}
    for m in m_list:
        total_size_MVC = 0
        total_size_AVC1 = 0
        total_size_AVC2 = 0
        total_size_AVC3 = 0
        for graph_amnt in range (1000):
            g = experiment1.create_random_graph(N,m)
            current_graph_MVC =  graph.MVC(g)
            total_size_MVC += len(current_graph_MVC)

            current_graph_AVC1 =  approx1(g)
            total_size_AVC1 += len(current_graph_AVC1)


            current_graph_AVC2 =  approx2(g)
            total_size_AVC2 += len(current_graph_AVC2)

            current_graph_AVC3 =  approx3(g)
            total_size_AVC3 += len(current_graph_AVC3)
            
        approx1_expected[m] = total_size_AVC1/total_size_MVC
        approx2_expected[m] = total_size_AVC2/total_size_MVC
        approx3_expected[m] = total_size_AVC3/total_size_MVC




    print("\nEXPECTED PERFORMACE:")
    print("APPROX1: "+ str(approx1_expected))
    print("APPROX2: " + str(approx2_expected))
    print("APPROX3: " + str(approx3_expected))

    # Plot expected performance
    plt.plot(list(approx1_expected.keys()), list(approx1_expected.values()), label='Approximation 1')
    plt.plot(list(approx2_expected.keys()), list(approx2_expected.values()), label='Approximation 2')
    plt.plot(list(approx3_expected.keys()), list(approx3_expected.values()), label='Approximation 3')
    plt.xlabel('Number of edges')
    plt.ylabel('Expected size of vertex cover')
    plt.title('Expected performance of approximations')
    plt.legend()
    plt.show()
potentialExperiment()