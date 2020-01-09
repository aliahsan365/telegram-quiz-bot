
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path



def convert_resposta_str(resposta):
    str = ''
    for par in resposta:
        str = str +  par[0] + ': ' + par[1] + '\n'
    return str

def pregunta(G,node):
    p = G.nodes[node]['content']
    print (p)

def resposta(G,node):
    r = G.nodes[node]['content']
    str_r = convert_resposta_str(r)
    print(str_r)




class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def dfs_alternativa(G,PID,opc):
    nodos_respondidos = []
    stack = Stack()
    stack.push(PID)
    auxopc = opc
    visited = []
    while (not stack.isEmpty()):
        c_node = stack.top()
        stack.pop()
        vecinos = list(G.successors(c_node))
        for v in vecinos:
            if G[c_node][v]['color'] == 'green':
                if G[c_node][v]['label'] == auxopc:
                    vecinos_del_vecino =  list(G.successors(v))
                    for vdv in vecinos_del_vecino:
                        if G[v][vdv]['color'] == 'blue':
                            nodos_respondidos.append(v)
                            pregunta(G,v)
                            resposta(G,vdv)
                            print('introduce opcion de respuesta:')
                            opc = input()
                            auxopc = opc

                stack.push(v)
        visited.append(c_node)


    return nodos_respondidos




def dfs_encuesta(G,EID):

    stack = Stack()
    stack.push(EID)
    visited = []
    while (not stack.isEmpty()):
        c_node = stack.top()
        stack.pop()
        vecinos = list(G.successors(c_node))
        for v in vecinos:
            if (not (v in visited)):
                if (G[c_node][v]['color'] == 'black' and G[c_node][v]['senyal'] == EID):
                    if G.nodes[v]['tipo'] == "pregunta":
                        vecinos_del_vecino =  list(G.successors(v))
                        opc = 'opc'
                        for vdv in vecinos_del_vecino:
                            if G[v][vdv]['color'] == 'blue':
                                pregunta(G,v)
                                resposta(G,vdv)
                                print('introduce opcion de respuesta:')
                                opc = input()
                        for vdv in vecinos_del_vecino:
                            if G[v][vdv]['color'] == 'green':

                                if (G[v][vdv]['label'] == opc):
                                    nodos_respondidos = dfs_alternativa(G,v,opc)
                                    for i in range(len(nodos_respondidos)):
                                        visited.append(nodos_respondidos[i])

                    stack.push(v)
        visited.append(c_node)
    return visited

def load_graph():
    print('voy a cargar el grafo')
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin

G = load_graph()

#E es el nodo inciail de la encuesta con publicinput.txt usado para obtener el grafo
dfs_encuesta(G,'E')
#si input multiencuestahabilitaresto descomentar esto.
#dfs_encuesta(G,'E3')