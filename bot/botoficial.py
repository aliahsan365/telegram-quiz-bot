import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import matplotlib.pyplot as plt
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
import logging
import pickle
import numpy as np

import random
import os

#####################GRAPH##############

def load_graph():
    print('voy a cargar el grafo')
    pickle_in = open("../cl/graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    return Gin

G = load_graph()


#####################END GRAPH##########


################################stats



def save_stats(stats_save):

    pickle_out = open("stats.pickle", "wb")
    pickle.dump(stats_save,pickle_out)
    pickle_out.close()


def load_stats():
    pickle_in = open("stats.pickle","rb")
    stats = pickle.load(pickle_in)
    return stats


#OK
def get_nodos_preguntas(nodos):
    preguntas = []
    for n in  nodos:
        if G.nodes[n]['tipo'] == "pregunta":
            preguntas.append(n)
    return preguntas
#OK
def get_dict_resposta_key(lpares):

    opcs = []
    for par in lpares:
        opcs.append(par[0])
    return dict.fromkeys(opcs, 0)





#OK
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



def store_stats(stats ,respuestas):

    for r in respuestas:
        stats[r][str(respuestas[r])] = stats[r][str(respuestas[r])] + 1
    return stats





def ini_stats():
    print('voy a inicializar las stats')
    nodos = G.nodes
    pnodes = get_nodos_preguntas(nodos)
    op_dict = dict()
    stats = dict.fromkeys(pnodes, op_dict)
    todo = get_pregunta_opc_respuestas(pnodes)
    for t in todo:
        stats[t[0]] = get_dict_resposta_key(t[1])
    save_stats(stats)



############################END STATS################################


######################PRETTY PRINT################
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
######################END PRETTY PRINT#############

###########HANDLER FUNCTIONS ####################



def start(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Inicia la conversa amb el Bot.")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def help(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="/help")
        bot.send_message(chat_id=update.message.chat_id, text="/start")
        bot.send_message(chat_id=update.message.chat_id, text="/author")
        bot.send_message(chat_id=update.message.chat_id, text="/report")
        bot.send_message(chat_id=update.message.chat_id, text="/pie <idPregunta>")
        bot.send_message(chat_id=update.message.chat_id, text="/bar <idPregunta>")
        bot.send_message(chat_id=update.message.chat_id, text="/quiz ⟨idEnquesta⟩")
        bot.send_message(chat_id=update.message.chat_id, text="Bot per fer enquestes")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def author(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Ali Muhammad Shiekh.")
        bot.send_message(chat_id=update.message.chat_id, text="ali.muhammad@est.fib.upc.edu")
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def report(bot, update):
    try:
        stats = load_stats()
        text = 'pregunta valor resposta \n'
        for e in stats:
            for op in stats[e]:
                text += e + '   ' + op + '   ' + str(stats[e][op]) + '\n'
        bot.send_message(chat_id=update.message.chat_id, text=text)


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def pie(bot,update,args):
    try:
        PID = args[0]
        bot.send_message(chat_id=update.message.chat_id, text=PID)

        stats = load_stats()
        bot.send_message(chat_id=update.message.chat_id, text=stats)
        filename = "%d.png" % random.randint(0000000, 9999999)
        labels = []  # answer options
        for op in stats[PID].keys():
            labels.append(op)
        bot.send_message(chat_id=update.message.chat_id, text=labels)
        values = []  # answer values
        for val in stats[PID].values():
            values.append(val)
        plt.pie(values,labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.savefig(filename, bbox_inches='tight')
        plt.clf()
        bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))
        os.remove(filename)


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

def bar(bot,update,args):
    try:
        PID = args[0]
        stats = load_stats()
        filename = "%d.png" % random.randint(0000000, 9999999)
        labels = []
        for op in stats[PID].keys():
            labels.append(op)
        values = []  # answer values
        for val in stats[PID].values():
            values.append(val)
        plt.bar(labels, values, align='center', alpha=1)
        y_pos = np.arange(len(labels))
        plt.xticks(y_pos, labels)
        plt.savefig(filename, bbox_inches='tight')
        plt.clf()
        bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))
        os.remove(filename)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')




def quiz(bot, update, args, user_data):
    try:
        EID = args[0]
        user_data['encuesta'] = EID
        user_data['respuestas'] = dict()


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')



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




def alternativa(bot,update,user_data,v,opc):
    try:
        nodos_respondidos = []
        stack = Stack()
        stack.push(v)
        auxopc = opc
        visited = []
        while (not stack.isEmpty()):
            c_node = stack.top()
            stack.pop()
            vecinos = list(G.successors(c_node))
            for v in vecinos:
                if G[c_node][v]['color'] == 'green':
                    if G[c_node][v]['label'] == auxopc:
                        vecinos_del_vecino = list(G.successors(v))
                        for vdv in vecinos_del_vecino:
                            if G[v][vdv]['color'] == 'blue':
                                nodos_respondidos.append(v)
                                p = pregunta(G, v)
                                r = resposta(G, vdv)
                                bot.send_message(chat_id=update.message.chat_id, text=p)
                                bot.send_message(chat_id=update.message.chat_id, text=r)

                                opc = update.message.text
                                auxopc = opc

                    stack.push(v)
            visited.append(c_node)

        return nodos_respondidos


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')


def encuesta(bot,update,user_data):
    try:

        stack = Stack()
        stack.push(user_data['encuesta'])
        visited = []
        while (not stack.isEmpty()):
            c_node = stack.top()
            stack.pop()
            vecinos = list(G.successors(c_node))
            for v in vecinos:
                if (not (v in visited)):
                    if (G[c_node][v]['color'] == 'black' and G[c_node][v]['senyal'] == user_data['encuesta']):
                        if G.nodes[v]['tipo'] == "pregunta":
                            vecinos_del_vecino = list(G.successors(v))
                            opc = 'opc'
                            for vdv in vecinos_del_vecino:
                                if G[v][vdv]['color'] == 'blue':
                                    p = pregunta(G, v)
                                    r = resposta(G, vdv)
                                    bot.send_message(chat_id=update.message.chat_id, text=p)
                                    bot.send_message(chat_id=update.message.chat_id, text=r)
                                    opc = update.message.text
                            for vdv in vecinos_del_vecino:
                                if G[v][vdv]['color'] == 'green':

                                    if (G[v][vdv]['label'] == opc):
                                        nodos_respondidos = alternativa(bot,update,user_data, v, opc)
                                        for i in range(len(nodos_respondidos)):
                                            visited.append(nodos_respondidos[i])

                        stack.push(v)
            visited.append(c_node)
        return visited


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')




########################## END HANDLER FUNCTIONS#########################

def main():
    ini_stats()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    TOKEN = open('token.txt').read().strip()
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('author', author))
    dispatcher.add_handler(CommandHandler('report', report))
    dispatcher.add_handler(CommandHandler('pie', pie, pass_args=True))
    dispatcher.add_handler(CommandHandler('bar', bar, pass_args=True))
    dispatcher.add_handler(CommandHandler('quiz', quiz, pass_args=True,pass_user_data = True))
    dispatcher.add_handler(MessageHandler(Filters.text, encuesta, pass_user_data=True))
    updater.start_polling()

if __name__ == '__main__':
    main()