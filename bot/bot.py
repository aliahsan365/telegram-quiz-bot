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


def sum_all(l):
    res = 0
    for x in l:
        res = res + x
    return res

#saca el maximo para piechart
def max_all(l):
    max = l[0];
    for x in l:
        if x > max:
            max = x
    return max






def convert_resposta_str(resposta):
    str = ''
    for par in resposta:
        str = str +  par[0] + ': ' + par[1] + '\n'
    return str

def pregunta(G,node):
    p = G.nodes[node]['content']
    print (p)
    return p

def resposta(G,node):
    r = G.nodes[node]['content']
    str_r = convert_resposta_str(r)
    print(str_r)
    return str_r


def check_encuesta(G,node):
    for v in list(G.nodes):
        if G.nodes[v]['tipo'] == 'encuesta':
            if G.nodes[node] ==  v:
                return 'esta'
    return 'no esta'


def check_pregunta(G,node):
    for v in list(G.nodes):
        if G.nodes[v]['tipo'] == 'pregunta':
            if G.nodes[node] ==  v:
                return 'esta'
    return 'no esta'



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


def dfs_alternativa(bot,update,user_data,G,PID,opc):
    nodos_respondidos = []
    stack = Stack()
    stack.push(PID)

    visited = []
    while (not stack.isEmpty()):
        c_node = stack.top()
        stack.pop()
        vecinos = list(G.successors(c_node))
        for v in vecinos:
            if G[c_node][v]['color'] == 'green':
                if G[c_node][v]['label'] == opc:
                    vecinos_del_vecino =  list(G.successors(v))
                    for vdv in vecinos_del_vecino:
                        if G[v][vdv]['color'] == 'blue':
                            nodos_respondidos.append(v)
                            p = pregunta(G, v)
                            r = resposta(G, vdv)
                            #print(str(c_node + '> ' + p + '\n' + r))
                            #opc = input()
                            bot.send_message(chat_id=update.message.chat_id, text=str(c_node  + '> ' + p + '\n' +  r))
                            opc = update.message.text
                stack.push(v)
        visited.append(c_node)


    return nodos_respondidos




def dfs_encuesta(bot,update,user_data,G,EID):

    print(user_data)

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

                                p = pregunta(G,v)
                                r = resposta(G,vdv)
                                #print(str(c_node + '> ' + p + '\n' + r))
                                #opc = input()
                                bot.send_message(chat_id=update.message.chat_id, text=str(c_node + '> ' + p + '\n' + r))
                                opc = update.message.text


                        for vdv in vecinos_del_vecino:
                            if G[v][vdv]['color'] == 'green':

                                if (G[v][vdv]['label'] == opc):
                                    nodos_respondidos = dfs_alternativa(bot,update,user_data ,G,v,opc)
                                    for i in range(len(nodos_respondidos)):
                                        visited.append(nodos_respondidos[i])

                    stack.push(v)
        visited.append(c_node)
    return visited







def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Inicia la conversa amb el Bot.")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="/help")
    bot.send_message(chat_id=update.message.chat_id, text="/start")
    bot.send_message(chat_id=update.message.chat_id, text="/author")
    bot.send_message(chat_id=update.message.chat_id, text="/quiz ⟨idEnquesta⟩")
    bot.send_message(chat_id=update.message.chat_id, text="/bar <idPregunta>")
    bot.send_message(chat_id=update.message.chat_id, text="/pie <idPregunta>")
    bot.send_message(chat_id=update.message.chat_id, text="/report")
    bot.send_message(chat_id=update.message.chat_id, text="Bot per fer enquestes")

def author(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Ali Muhammad Shiekh.")
    bot.send_message(chat_id=update.message.chat_id, text="ali.muhammad@est.fib.upc.edu")





def quiz(bot, update, args, user_data):
    try:

        G = load_graph()
        EID = args[0]
        dfs_encuesta(bot,update,user_data,G,EID)


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')




def bar(bot, update, args):
    try:
        bot.send_message(chat_id=update.message.chat_id, text='pie')
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def pie(bot, update, args):
    try:
        bot.send_message(chat_id=update.message.chat_id, text='pie')
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def report(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text='report')
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    TOKEN = open('token.txt').read().strip()
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('author', author))
    dispatcher.add_handler(CommandHandler('quiz', quiz, pass_args=True,pass_user_data = True))
    dispatcher.add_handler(CommandHandler('pie', pie, pass_args=True))
    dispatcher.add_handler(CommandHandler('bar', bar, pass_args=True))
    dispatcher.add_handler(CommandHandler('report', report))

    dispatcher.add_handler(MessageHandler(Filters.text, dfs_encuesta,pass_user_data=True))

    updater.start_polling()

if __name__ == '__main__':
    main()