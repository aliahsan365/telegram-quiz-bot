import networkx as nx
import matplotlib.pyplot as plt



G = nx.Graph()
l1 = [1,2,3]
G.add_node('P1', content = l1)
print(G.nodes['P1']['content'])

l2 = [4,5,6]
G.add_node('P2',content = l2)
print(G.nodes['P2']['content'])

G.add_edge('P1', 'P2', label='I1' )
print(G['P1']['P2']['label'])











