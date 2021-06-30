import seaborn as sns
import pandas as pd
import sys

#get data
filename = sys.argv[-1]
pd_ppi_df = pd.read_csv(filename, header = 0, sep = ",")

#plotting boxplot
box_plot = sns.catplot(x = "group", y = "Pfam ID", data = pd_ppi_df[pd_ppi_df["Pfam ID"] < 20], kind = "box")
box_plot.fig.suptitle("# of Protein Domains (outliers cut at > 20)")
box_plot.savefig("./protein_domains_vs_string_degree.png", bbox_inches = "tight", pad_inches = 1.0)