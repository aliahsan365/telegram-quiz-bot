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
        user_data['visited'] = [EID]
        l =  list(G.successors(EID))
        p1 = l[0]
        print(p1)
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
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='??')





def encuesta(bot,update,user_data):
    try:
        (next_node,opc) = nextpreg(bot,update,user_data)
        if (next_node == 'END'):

            bot.send_message(chat_id=update.message.chat_id, text='gracias por contestar, hijo de puta!')
        else:
            user_data['respuestas'][next_node] = opc
            bot.send_message(chat_id=update.message.chat_id, text=str(user_data['respuestas']))
            save_stats(store_stats(load_stats(),user_data['respuestas']))
            print(load_stats())

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='??')




########################## END HANDLER FUNCTIONS#########################






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







#################### END LOGICS




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