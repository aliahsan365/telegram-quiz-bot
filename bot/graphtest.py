import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(1,10))

G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(6,7)
G.add_edge(7,8)
G.add_edge(8,9)
G.add_edge(9,1)

print(G.nodes.data())

#pintar el grafo, todo esto es lo q da la foto.
#nx.draw(G,with_labels=True)
#plt.draw()
#plt.show()













