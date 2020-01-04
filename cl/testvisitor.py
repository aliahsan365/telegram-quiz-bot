import sys
from antlr4 import *
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from antlr4.InputStream import InputStream
from EnquestesVisitor import EnquestesVisitor

import networkx as nx
import matplotlib.pyplot as plt
import pickle

def save_graph(G):
    pickle_out = open("graph.pickle", "wb")
    pickle.dump(G,pickle_out)
    pickle_out.close()

def render_graph(G):
    layout = nx.circular_layout(G)
    arestas = G.edges()
    colores = [G[u][v]['color'] for u, v in arestas]
    nx.draw(G, layout, arrow=True , with_labels=True, edge_color=colores )
    tags = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, layout, edge_labels=tags)
    plt.show()

if len(sys.argv) > 1:
    input_stream = FileStream(sys.argv[1])
else:
    input_stream = InputStream(input('? '))
lexer = EnquestesLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = EnquestesParser(token_stream)
tree = parser.root()
G = nx.DiGraph()
visitor = EnquestesVisitor(G)
visitor.visit(tree)
render_graph(G)
save_graph(G)









