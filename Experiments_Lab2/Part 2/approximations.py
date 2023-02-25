import graph
import copy
import random


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
        if graph.is_vertex_cover(G_copy,C):
            return C


def approx2(G):
    C = set()
    # Make a copy of the graph
    G_copy = copy.deepcopy(G)
    while True:
        # Select a vertex randomly from G which is not already in C
        v = random.choice(list(set(G_copy.adj) - C))#set of all nodes minus the C set e.g.set(G.adj) = {1,2,3,4} - C = {3} = {1,2,4}... list() converts to [1,2,4]
        C.add(v)
        if graph.is_vertex_cover(G_copy,C):
            return C


def approx3(G):
    C = set()
    # Make a copy of the graph
    G_copy = copy.deepcopy(G)
    while True:
        # Select a random edge from the graph (u,v)

        # Create a list holding all the edges in G
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
        if graph.is_vertex_cover(G_copy,C):
            return C




