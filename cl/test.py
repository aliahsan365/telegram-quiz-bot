import pickle
import sys

import matplotlib.pyplot as plt
import networkx as nx
from EnquestesLexer import EnquestesLexer
from EnquestesParser import EnquestesParser
from EnquestesVisitor import EnquestesVisitor
from antlr4 import *
from antlr4.InputStream import InputStream


def save_graph(G):
    pickle_out = open("graph.pickle", "wb")
    pickle.dump(G, pickle_out)
    pickle_out.close()


def render_graph(G):
    layout = nx.circular_layout(G)
    arestas = G.edges()
    colores = [G[u][v]['color'] for u, v in arestas]
    nx.draw(G, layout, arrow=True, with_labels=True, edge_color=colores)
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
