import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import scipy
import operator


def ride_graph():
    df = pd.read_csv("../data/Divvy_Trips_2018_Q2.csv")
    G = nx.from_pandas_edgelist(df, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    return G


def compute_pagerank(G, damping_factor):
    return nx.pagerank_scipy(G, alpha=damping_factor)


def ride_graph_weekday():
    df = pd.read_csv("../data/Divvy_Trips_2018_Q2.csv")
    df["start_time"] = pd.to_datetime(df["start_time"])
    df_weekday = df[df["start_time"].dt.weekday < 5]
    df_weekend = df[df["start_time"].dt.weekday >= 5]
    weekday_G = nx.from_pandas_edgelist(df_weekday, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    weekend_G = nx.from_pandas_edgelist(df_weekend, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
    return weekday_G, weekend_G



def na():
    pr_sorted = sorted(pr.items(), key=operator.itemgetter(1), reverse=True)


    # test graph
    edges = {"to": [0, 1, 2, 2], "from": [2, 0, 1, 1]}
    df = pd.DataFrame(edges)
    G = nx.from_pandas_edgelist(df, "to", "from", create_using=nx.MultiDiGraph)
    print(nx.to_pandas_adjacency(G))


# G = nx.from_pandas_edgelist(df, "from_station_id", "to_station_id", create_using=nx.MultiDiGraph)
# print(nx.to_pandas_adjacency(G, nodelist=range(20)))
#
# nx.pagerank(G, alpha=0.75)
#
# nx.draw(G, with_labels=True)
# plt.draw()
# plt.show()
