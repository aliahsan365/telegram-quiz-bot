
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path



def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin


def encuesta(EID,G):
    preguntas_encuesta = []
    index = G.nodes[EID]['content']
    print(index)
    for i in sorted(index):
        preguntas_encuesta.append(G.nodes[i]['content'])
    return preguntas_encuesta

def  extras(G):
    P1 = G.nodes['P1']['content']
    print(P1)
    print(G.nodes['R3']['content'])
    print(G['P1']['R1']['label'])

    print(G.nodes['E']['content'])
    print(G.nodes,G.edges)

def main():
    G = load_graph()
    preguntas_encuesta = encuesta('E',G)
    print(preguntas_encuesta)



if __name__ == '__main__':
    main()


