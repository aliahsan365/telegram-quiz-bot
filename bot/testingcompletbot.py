
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


def dfs_alternativa(G,AID,opc):
    stack = Stack()
    stack.push(AID)
    auxopc = opc
    visited = []
    while (not stack.isEmpty()):
        c_node = stack.top()
        stack.pop()
        vecinos = list(G.successors(c_node))
        for v in vecinos:
            if (not (v in visited)):
                if (G[c_node][v]['color'] == 'green' and G[c_node][v]['label'] == auxopc):
                    print('pregunta de alternativa')
                    print('PREGUNTA alternativa')
                    print(G.nodes[v]['content'])
                    print('RESPOSTA alternativa')
                    vecinos_del_vecino = list(G.successors(v))
                    for vdv in vecinos_del_vecino:
                        if G.nodes[vdv]['tipo'] == "respuesta":
                            print('resposta')
                            print(G.nodes[vdv]['content'])
                        print('anwswer question')
                        auxopc = input()

                    stack.push(v)
        visited.append(c_node)
    return visited




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
                                    #repetir hasta que responda bien
                                    print('no esta')
                                else:
                                    print('esta')
                        print(opc)
                        for vdv in vecinos_del_vecino:
                            if (G[v][vdv]['color'] == 'green'):
                                if (G[v][vdv]['label'] == opc):
                                    print('la respuesta coincide')
                                    print('vamos a ejecutar el dfs del alternativa')
                                    visted_alternativas = dfs_alternativa(G,v,opc)
                                    print(visted_alternativas)
                                    for elem in visted_alternativas:
                                        visited.append(elem)









                    stack.push(v)
        visited.append(c_node)
    return visited



def main():
    G = load_graph()
    #print((G.out_edges('P3')))
    print(dfs_encuesta(G,'E'))
    #print(dfs_alternativa(G, 'P3'))
    #print(dfs(G, 'E2'))
    #print(dfs(G, 'E3'))




if __name__ == '__main__':
    main()


