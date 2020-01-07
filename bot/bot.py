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





def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


def ptr(bot,update):
    sentence = update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=sentence)



def quiz(bot, update, args):
    try:
        G = load_graph()
        #dispatcher = update.dispatcher
        #dispatcher.add_handler(MessageHandler(Filters.text, ptr))
        EID = args[0]
        if (EID in list(G.nodes)):
            bot.send_message(chat_id=update.message.chat_id, text="esta")
            camino = dfs_encuesta(G,EID)
            bot.send_message(chat_id=update.message.chat_id, text=str(camino))
            #user =  update.message.from_user
            #print(user)
            #bot.set_update_listener(listener)


        else:
            bot.send_message(chat_id=update.message.chat_id, text="no esta")





        bot.send_message(chat_id=update.message.chat_id, text=EID)



    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def render_graph(G):
    layout = nx.circular_layout(G)
    arestas = G.edges()
    colores = [G[u][v]['color'] for u, v in arestas]
    nx.draw(G, layout, arrow=True , with_labels=True, edge_color=colores)
    tags = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, layout, edge_labels=tags)
    plt.show()




def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    # engega el bot
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('token.txt').read().strip()

    # crea objectes per treballar amb Telegram
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    print("bot running")


    #conv_handler = ConversationHandler( entry_points=[CommandHandler('start', start)])
    # indica que quan el bot rebi la comanda /start s'executi la funció start
    dispatcher.add_handler(CommandHandler('start', start))

    # indica que quan el bot rebi la comanda /help s'executi la funció start
    dispatcher.add_handler(CommandHandler('help', help))

    # indica que quan el bot rebi la comanda /author s'executi la funció start
    dispatcher.add_handler(CommandHandler('author', author))

    dispatcher.add_handler(CommandHandler('quiz', quiz, pass_args=True))
    #dispatcher.add_handler(CommandHandler(Filters.text, 'quiz', quiz, pass_args=True))
    #dispatcher.add_handler(MessageHandler(Filters.text, quiz, pass_args=True))
    #dispatcher.add_error_handler(error)
    updater.start_polling()

    print("chaobot")


if __name__ == '__main__':
    main()