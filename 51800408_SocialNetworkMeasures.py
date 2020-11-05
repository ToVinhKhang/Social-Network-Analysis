import networkx as nx
import matplotlib.pyplot as plt
import sys

#------
# DATA
#------
G=nx.Graph()
with open("../Resource/"+sys.argv[1]) as f:
    lines = f.readlines()
    x = [int(line.split()[0]) for line in lines]
    y = [int(line.split()[1]) for line in lines]
for i in range(len(x)):
	G.add_edge(x[i],y[i])

#Show graph
nx.draw(G, node_color='green', with_labels = True)
plt.show()

def InformationOfGraph():
	# Read Information of Graph
	print("-------------------------------------------------")
	print("InformationOfGraph:")
	print("Nodes: ",G.nodes())
	print("Edges: ",G.edges())
	print("Number of Nodes: ",G.number_of_nodes())
	print("Number of Edges: ",G.number_of_edges())
	print("-------------------------------------------------")

def Density():
	# Calculate Density
	n=G.number_of_nodes()
	m=G.number_of_edges()
	D=m/(n*(n-1)/2)
	print("-------------------------------------------------")
	print("Density of this network : ",D)
	print("-------------------------------------------------")

def DegreeCentrality():
	# Calculate DegreeCentrality
	TempCd=[]
	Sum=0;
	for i in range(0,len(G.nodes())):
		m=len(G.edges(i))
		n=G.number_of_nodes()
		Cd=m/(n-1)
		Sum+=Cd
		TempCd.append(Cd);
		if(i<10):
			print("DegreeCentrality of Node",i," : ",Cd)
		else:
			print("DegreeCentrality of Node",i,": ",Cd)

	# Find Average DegreeCentrality
	Avg=Sum/len(G.nodes())
	# Find Highest Lowest DegreeCentrality
	Max=max(TempCd)
	Min=min(TempCd)
	# Identify that nodes
	a=[]
	b=[]
	for i in range(0,len(TempCd)):
		if(TempCd[i]==Max):
			a.append(i);
		if(TempCd[i]==Min):
			b.append(i);
	print("--------------------------------------------------")
	print("Average DegreeCentrality : ",Avg)
	print("Lowest  DegreeCentrality : ",Min,"( Node",b,")")
	print("Highest DegreeCentrality : ",Max,"( Node",a,")")
	print("--------------------------------------------------")

def ClosenessCentrality():
	# Calculate ClosenessCentrality
	closeness=nx.closeness_centrality(G)
	Sum=0;
	TempCc=[]
	for i in range(0,len(closeness)):
		Sum+=closeness[i];
		TempCc.append(closeness[i]);
		if(i<10):
			print("ClosenessCentrality of Node",i," : ",closeness[i])
		else:
			print("ClosenessCentrality of Node",i,": ",closeness[i])
	# Find Average ClosenessCentrality
	Avg=Sum/len(G.nodes())
	# Find Highest Lowest ClosenessCentrality
	Max=max(TempCc)
	Min=min(TempCc)
	a=[]
	b=[]
	for i in range(0,len(TempCc)):
		if(TempCc[i]==Max):
			a.append(i);
		if(TempCc[i]==Min):
			b.append(i);
	# Identify that nodes
	print("------------------------------------------------------")
	print("Average ClosenessCentrality : ",Avg)
	print("Lowest  ClosenessCentrality : ",Min,"( Node",b,")")
	print("Highest ClosenessCentrality : ",Max,"( Node",a,")")
	print("------------------------------------------------------")

def BetweennessCentrality():
	# Calculate BetweennessCentrality
	betweenness=nx.betweenness_centrality(G)
	Sum=0;
	TempCb=[]
	for i in range(0,len(betweenness)):
		Sum+=betweenness[i];
		TempCb.append(betweenness[i]);
		if(i<10):
			print("BetweennessCentrality of Node",i," : ",betweenness[i])
		else:
			print("BetweennessCentrality of Node",i,": ",betweenness[i])
	# Find Average BetweennessCentrality
	Avg=Sum/len(G.nodes())
	# Find Highest Lowest BetweennessCentrality
	Max=max(TempCb)
	Min=min(TempCb)
	a=[]
	b=[]
	for i in range(0,len(TempCb)):
		if(TempCb[i]==Max):
			a.append(i);
		if(TempCb[i]==Min):
			b.append(i);
	# Identify that nodes
	print("------------------------------------------------------")
	print("Average BetweennessCentrality : ",Avg)
	print("Lowest  BetweennessCentrality : ",Min,"( Node",b,")")
	print("Highest BetweennessCentrality : ",Max,"( Node",a,")")
	print("------------------------------------------------------")

def ClusteringCentrality():
	# Calculate ClusteringCentrality
	clustering=nx.clustering(G)
	Sum=0;
	TempCclustering=[]
	for i in range(0,len(clustering)):
		Sum+=clustering[i];
		TempCclustering.append(clustering[i]);
		if(i<10):
			print("ClusteringCentrality of Node",i," : ",clustering[i])
		else:
			print("ClusteringCentrality of Node",i,": ",clustering[i])
	# Find Average ClusteringCentrality
	Avg=Sum/len(G.nodes())
	# Find Highest Lowest ClusteringCentrality
	Max=max(TempCclustering)
	Min=min(TempCclustering)
	a=[]
	b=[]
	for i in range(0,len(TempCclustering)):
		if(TempCclustering[i]==Max):
			a.append(i);
		if(TempCclustering[i]==Min):
			b.append(i);
	# Identify that nodes
	print("------------------------------------------------------")
	print("Average ClusteringCentrality : ",Avg)
	print("Lowest  ClusteringCentrality : ",Min,"( Node",b,")")
	print("Highest ClusteringCentrality : ",Max,"( Node",a,")")
	print("------------------------------------------------------")


#--------
# Result
#--------

InformationOfGraph()
Density()
print("\n")
DegreeCentrality()
print("\n")
ClosenessCentrality()
print("\n")
BetweennessCentrality()
print("\n")
ClusteringCentrality()
