import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
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

def quiz(bot, update, args , user_data):
    try:
        EID = args[0]
        print(EID)
        print('jodejoder')

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
    G = load_graph()
    render_graph(G)

    # engega el bot
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('token.txt').read().strip()

    # crea objectes per treballar amb Telegram
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    print("bot running")
    updater.start_polling()
    updater.idle()
    # indica que quan el bot rebi la comanda /start s'executi la funció start
    dispatcher.add_handler(CommandHandler('start', start))

    # indica que quan el bot rebi la comanda /help s'executi la funció start
    dispatcher.add_handler(CommandHandler('help', help))

    # indica que quan el bot rebi la comanda /author s'executi la funció start
    dispatcher.add_handler(CommandHandler('author', author))

    dispatcher.add_handler(CommandHandler('quiz', quiz))

    print("chaobot")


if __name__ == '__main__':
    main()