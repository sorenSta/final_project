STRING_DB = https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
STRING_TAR = 9606.protein.links.v11.0.txt.gz


#get boxplot
boxplot.png: pd_ppi.csv make_boxplot.py
	python make_boxplot.py pd_ppi.csv


#join PPI and protein domain
pd_ppi.csv: network_nodes.csv proteins_w_domains.txt protein_domain.py
	python protein_domain.py network_nodes.csv proteins_w_domains.txt



#get network connectedness of nodes
network_nodes.csv: 9606.protein.links.v11.0.txt network.py
	python network.py 9606.protein.links.v11.0.txt

#get data
9606.protein.links.v11.0.txt : 
	wget $(STRING_DB)
	gunzip $(STRING_TAR) 




.PHONY : clean
clean :
	rm -f *.png
	rm -f *.csv
