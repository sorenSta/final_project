import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import sys

#get PPI data
filename = sys.argv[-1]
ppi_df = pd.read_csv(filename, header =0, sep = " ")

#filtering on combined score > 500
ppi_df = ppi_df[ppi_df["combined_score"] >= 500]

#make network
network = nx.from_pandas_edgelist(ppi_df, source = "protein1", target = "protein2")

#finding number of degrees
node_degrees = network.degree()
degree_df = pd.DataFrame(list(node_degrees), columns=["Protein ID", "Degree"])

#partition network
degree_large = degree_df[degree_df["Degree"]>100]
degree_small = degree_df[degree_df["Degree"]<= 100]

degree_large["group"] = "large"
degree_small["group"] = "small"
degree_all = pd.concat([degree_large, degree_small])

degree_all.to_csv("network_nodes.csv", sep=",", index=False)
