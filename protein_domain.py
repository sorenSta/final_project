import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys

#getting input files
filename_ppi = sys.argv[-2]
filename_domain = sys.argv[-1]

ppi_df = pd.read_csv(filename_ppi, sep = ",", header = 0)
protein_domains = pd.read_csv(filename_domain, sep = "\t", header = 0)

#getting number of protein domaions connected to protein
pd_counts = protein_domains.groupby("Protein stable ID", as_index = False).count()

#getting df with nodes and protein domains
ppi_df["Protein ID"] = ppi_df["Protein ID"].str[5:]
pd_ppi_df = pd.merge(ppi_df, pd_counts, left_on = "Protein ID", right_on = "Protein stable ID", how = "left").fillna(0)

pd_ppi_df.to_csv("pd_ppi.csv", sep = ",")

