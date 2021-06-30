#get boxplot
boxplot.png: data/pd_ppi.csv make_boxplot.py
	python make_boxplot.py data/pd_ppi.csv


#join PPI and protein domain
data/pd_ppi.csv: data/network_nodes.csv data/proteins_w_domains.txt protein_domain.py
	python protein_domain.py data/network_nodes.csv data/proteins_w_domains.txt



#get network connectedness of nodes
data/network_nodes.csv: data/9606.protein.links.v11.0.txt network.py
	python network.py data/9606.protein.links.v11.0.txt



.PHONY : clean
clean :
	rm -f *.png
	rm -f *.csv
