import experiment2
import matplotlib.pyplot as plt

results = experiment2.run_exp()

nodes = 100
for lst in results:
    prop = []
    prob = []
    for res in lst:
        prop.append(res[0])
        prob.append(res[1])

    plt.plot(prop, prob, label=str(nodes)+' Nodes')

    nodes += 100

yticks = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
plt.yticks(yticks,yticks)
plt.xlabel("Proportion of Cycles to Nodes")
plt.ylabel("Probability of Connected Graph")
plt.title("Probability of a Connected Graph with N edges")
plt.legend()
plt.show()
