
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path



def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin


def main():
    G = load_graph()
    P1 = G.nodes['P1']['content']
    print(P1)
    print(G.nodes['R3']['content'])
    print(G['P1']['R1']['label'])


    print(G.nodes,G.edges)


if __name__ == '__main__':
    main()


