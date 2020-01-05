
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path


def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin


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


def dfs(G,EID):

    stack = Stack()
    stack.push(EID)
    visited = []
    preguntas = [EID]
    respuestas = []
    pares = []
    while (not stack.isEmpty()):
        c_node = stack.top()
        stack.pop()
        vecinos = list(G.successors(c_node))
        for v in vecinos:
            if (not (v in visited)):
                if (G[c_node][v]['color'] == 'black' and G[c_node][v]['senyal'] == EID):
                    if G.nodes[v]['tipo'] == "pregunta":
                        vecinos_del_vecino =  list(G.successors(v))
                        for vdv in vecinos_del_vecino:
                            if G[v][vdv]['color'] == 'blue':
                                print('PREGUNTA')
                                print(G.nodes[v]['content'])
                                print('RESPOSTA')
                                print(G.nodes[vdv]['content'])
                                print('anwswer question')
                                opc = input()
                                esta = 0
                                for par in list(G.nodes[vdv]['content']):
                                    if (par[0] == opc):
                                        esta = 1
                                if (esta == 0):
                                    print('no esta')
                                else:
                                    print('esta')
                                vecinos_del_vecino_del_vecino = list(G.successors(vdv))
                                for vdvdv in vecinos_del_vecino_del_vecino:
                                    if (G[vdv][vdvdv]['color'] == 'green' and G[vdv][vdvdv]['label'] == opc):
                                        print('verde')
                                        stack.push(vdvdv)


                                pares.append((v,vdv))

                                respuestas.append(vdv)
                    preguntas.append(v)
                    stack.push(v)
        visited.append(c_node)
    return preguntas,respuestas,pares



def main():
    G = load_graph()
    print(dfs(G,'E'))
    #print(dfs(G, 'E2'))
    #print(dfs(G, 'E3'))




if __name__ == '__main__':
    main()


