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


def load_graph():
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin

G = load_graph()


stats = dict()

def get_nodos_preguntas(nodos):
    preguntas = []
    for n in  nodos:
        if G.nodes[n]['tipo'] == "pregunta":
            preguntas.append(n)
    print(preguntas)
    return preguntas

def get_dict_resposta_key(lpares):
    res = dict()
    opcs = []
    for par in lpares:
        opcs.append(par[0])
    res = dict.fromkeys(opcs, 0)
    print(res)
    return res





def get_nodos_respuestas(nodos):
    respuestas = []
    for n in  nodos:
        if G.nodes[n]['tipo'] == "respuesta":
            l = G.nodes[n]['content']
            respuestas.append(l)

    return respuestas

def get_pregunta_opc_respuestas(pnodes):
    pares_preguna_opcrespuesta = []
    for pid in pnodes:
        vecinop = list(G.successors(pid))
        for vdv in vecinop :
            if G[pid][vdv]['color'] == 'blue':
                r = G.nodes[vdv]['content']
                pares = (pid,r)
                pares_preguna_opcrespuesta.append(pares)
    return pares_preguna_opcrespuesta






def ini_stats():
    nodos = G.nodes
    pnodes = get_nodos_preguntas(nodos)
    op_dict = dict()
    stats = dict.fromkeys(pnodes, op_dict)

    print(stats)

    rnodes = get_nodos_respuestas(nodos)
    print(rnodes)
    todo = get_pregunta_opc_respuestas(pnodes)

    for t in todo:
        stats[t[0]] = get_dict_resposta_key(t[1])
    print(stats)

    #stats['P1']['1'] = stats['P1']['1'] + 60
    #print(stats)
    respuestas = dict(P1='2', P2='0', P3=3)
    #print(respuestas)
    for r in respuestas:
        print(stats[r][str(respuestas[r])])
        print(r,respuestas[r])
        stats[r][str(respuestas[r])] = stats[r][str(respuestas[r])] + 1
    print('imprimo stats final final')
    print(stats)




def main():
    ini_stats()

if __name__ == '__main__':
    main()




#user_data2 = {{'p1',3},{'p2',2},{'p3',3}}



#estadisticas = {{'p1',3},{'p2',2},{'p3',3}}