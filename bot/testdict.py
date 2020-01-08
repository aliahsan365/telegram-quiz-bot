import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import logging
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pickle
from pathlib import Path





user_data1 = dict()

user_data1 = {'p1': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript']}

for e in user_data1:
    print(e)
    print(user_data1[e])


def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin


G = load_graph()

print(G.nodes,G.edges)

stats = dict()

def get_nodos_preguntas(nodos):
    preguntas = []
    for n in  nodos:
        if G.nodes[n]['tipo'] == "pregunta":
            preguntas.append(n)
    print(preguntas)
    return preguntas

def get_nodos_respuestas(nodos):
    respuestas = []
    for n in  nodos:
        if G.nodes[n]['tipo'] == "respuesta":
            l = G.nodes[n]['content']
            respuestas.append(l)

    return respuestas



def ini_stats():
    nodos = G.nodes
    pnodes = get_nodos_preguntas(nodos)
    op_dict = dict()
    stats = dict.fromkeys(pnodes, op_dict)

    print(stats)

    rnodes = get_nodos_respuestas(nodos)
    print(rnodes)



def main():
    ini_stats()

if __name__ == '__main__':
    main()




#user_data2 = {{'p1',3},{'p2',2},{'p3',3}}



#estadisticas = {{'p1',3},{'p2',2},{'p3',3}}