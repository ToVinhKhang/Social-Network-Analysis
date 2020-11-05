import matplotlib.pyplot as plt
import networkx as nx
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

def HighCb(G):
	Eb = nx.edge_betweenness_centrality(G);
	E  = ();
	for u, v in sorted(Eb.items(), key=lambda i: i[1], reverse = True):
		E = u;
		break;
	return E;
def GNA(G):
	links = nx.connected_components(G);
	number = nx.number_connected_components(G);
	while(number == 1):
		G.remove_edge(HighCb(G)[0], HighCb(G)[1]);
		links = nx.connected_components(G);
		number = nx.number_connected_components(G);
	return links;
def Community():
	Temp = GNA(G.copy());
	Area = [];
	for i in Temp:
		Area.append(list(i));
		return Area;
def ShowGraphAfterUseGNA():
	color = [];
	for i in G:
	    if i in Community()[0]:
	        color.append('pink');
	    else: 
	        color.append('orange');
	nx.draw(G, node_color=color, with_labels=True);
	plt.show();
def ShowGraphAtFirst():
	nx.draw(G, node_color='green', with_labels = True);
	plt.show();

#------
# Show
#------

print("------------------------------");
print("<Close the figure to continue>");
print("------------------------------");
ShowGraphAtFirst();
print("Using Girvan Newman Algorithms");
print("...........Loading............");
ShowGraphAfterUseGNA();
print("          Completed           ");
print("------------------------------");