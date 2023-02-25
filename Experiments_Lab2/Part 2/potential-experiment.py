import graph
import approximations
import matplotlib.pyplot as plt

N = 8 # Constant Node Size of 8 Nodes

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
            g = graph.create_random_graph(N,m)
            current_graph_MVC =  graph.MVC(g)
            total_size_MVC += len(current_graph_MVC)

            current_graph_AVC1 =  approximations.approx1(g)
            total_size_AVC1 += len(current_graph_AVC1)


            current_graph_AVC2 =  approximations.approx2(g)
            total_size_AVC2 += len(current_graph_AVC2)

            current_graph_AVC3 =  approximations.approx3(g)
            total_size_AVC3 += len(current_graph_AVC3)
            
        approx1_expected[m] = total_size_AVC1/total_size_MVC
        approx2_expected[m] = total_size_AVC2/total_size_MVC
        approx3_expected[m] = total_size_AVC3/total_size_MVC



    # # Printing Out Expected Performance
    # print("\nEXPECTED PERFORMACE:")
    # print("APPROX1: "+ str(approx1_expected))
    # print("APPROX2: " + str(approx2_expected))
    # print("APPROX3: " + str(approx3_expected))

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