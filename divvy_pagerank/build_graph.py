import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import operator


df = pd.read_csv("../data/Divvy_Trips_2018_Q2.csv")
# df["tripduration"] = df["tripduration"].apply(lambda x: float(x.split()[0].replace(',', '')))

# test graph
edges = {"to": [0, 1, 2, 2], "from": [2, 0, 1, 1]}
df = pd.DataFrame(edges)
G = nx.from_pandas_edgelist(df, "to", "from", create_using=nx.MultiDiGraph)
print(nx.to_pandas_adjacency(G))

pr = nx.pagerank_scipy(G, alpha=0.75)
pr_sorted = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)

print(pr)

# G = nx.from_pandas_edgelist(df, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
# print(nx.to_pandas_adjacency(G, nodelist=range(20)))
#
# nx.pagerank(G, alpha=0.75)
#
# nx.draw(G, with_labels=True)
# plt.draw()
# plt.show()
