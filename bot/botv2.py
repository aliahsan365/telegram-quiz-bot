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




def convert_resposta_str(resposta):
    str = ''
    for par in resposta:
        str = str +  par[0] + ': ' + par[1] + '\n'
    return str



def pregunta(G,node):
    p = G.nodes[node]['content']
    return p


def resposta(G,node):
    r = G.nodes[node]['content']
    str_r = convert_resposta_str(r)
    print(str_r)
    return str_r




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




def nextpreg(bot,update,user_data):

    c_node = user_data['currentnode']
    vecinos = list(G.successors(c_node))
    next_node = 'next'
    opc = update.message.text


    for v in vecinos:
        if not (v in user_data['visited']):
            if (G[c_node][v]['color'] == 'black' and G[c_node][v]['senyal'] == user_data['encuesta']):
                if G.nodes[v]['tipo'] == "pregunta":
                    vecinos_del_vecino = list(G.successors(v))
                    for vdv in vecinos_del_vecino:
                        if G[v][vdv]['color'] == 'blue':
                            p = pregunta(G, v)
                            r =  resposta(G, vdv)
                            bot.send_message(chat_id=update.message.chat_id, text=p)
                            bot.send_message(chat_id=update.message.chat_id, text=str(r))
                            opc = update.message.text

                            next_node = v

                            user_data['currentnode'] = v
                            user_data['visited'].append(c_node)

    return (c_node,opc)

def quiz(bot, update, args, user_data):
    try:
        EID = args[0]
        user_data['encuesta'] = EID
        user_data['visited'] = [EID]
        l =  list(G.successors(EID))
        p1 = l[0]
        user_data['currentnode'] = p1
        user_data['respuestas'] = dict()
        vp1 = list(G.successors(p1))
        for vdv in vp1:
            if G[p1][vdv]['color'] == 'blue':
                p = pregunta(G, p1)
                r = resposta(G, vdv)
                bot.send_message(chat_id=update.message.chat_id, text=p)
                bot.send_message(chat_id=update.message.chat_id, text=str(r))
                opc = update.message.text
                user_data['respuestas'][p1] = opc
                user_data['visited'].append(p1)
        user_data['stack_encuesta'] = Stack()
        user_data['stack_alternativa'] = Stack()
        user_data['estadisticas'] = dict()
        user_data['currentnode_alternativa'] = 'A'
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')



def encuesta(bot,update,user_data):
    try:
        (next_node,opc) = nextpreg(bot,update,user_data)
        if (next_node == 'END'):
            print('entro en el if')
            bot.send_message(chat_id=update.message.chat_id, text='gracias por contestar, hijo de puta!')
        else:
            print('entro en el else')
            user_data['respuestas'][next_node] = opc
            bot.send_message(chat_id=update.message.chat_id, text=str(user_data['respuestas']))

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


    dispatcher.add_handler(MessageHandler(Filters.text, encuesta, pass_user_data=True))


    updater.start_polling()

if __name__ == '__main__':
    main()