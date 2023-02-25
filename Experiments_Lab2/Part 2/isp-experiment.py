# from graph import * -- commented out this import to ensure consistency among other files
import graph # used this import instead

# All that was changed was "graph." was added to the following functions:
# "generate_random_graph(n,d)"             ---->  "graph.generate_random_graph(n,d)"
# "size_of_largest_independent_set(G)"     ---->  "graph.size_of_largest_independent_set(G)"
# "size_of_smallest_vertex_cover(G)"       ---->  "graph.size_of_smallest_vertex_cover(G)"
# "MIS(G)"                                 ---->  "graph.MIS(G)"
# "MVC(G)"                                 ---->  "graph.MVC(G)"

# experiment with random graphs
n = 10
ds = [0.1, 0.2, 0.3, 0.4, 0.5]
for d in ds:
    G = graph.generate_random_graph(n,d)
    mis_size = graph.size_of_largest_independent_set(G)
    mvc_size = graph.size_of_smallest_vertex_cover(G)
    print("density:", d, "MIS size:", mis_size, "MVC size:", mvc_size)
    print("sum of sizes:", mis_size + mvc_size)
    print("MIS:", graph.MIS(G))
    print("MVC:", graph.MVC(G))