import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

import pickle
import os.path

#print(pickle.__doc__)

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#sumalista para el piechart
pickle_path = os.path.abspath(__file__)

my_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(my_path, "cl\graph.pickle")

print("pickle path abs")
print(file_path)

def load_graph():
    pickle_in = open(file_path,"rb")
    Gin = pickle.load(pickle_in)
    print(Gin.nodes,Gin.edges)

#load_graph()


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







def main():
    print("bot running")
    # engega el bot
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('token.txt').read().strip()

    # crea objectes per treballar amb Telegram
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    updater.start_polling()

    # indica que quan el bot rebi la comanda /start s'executi la funció start
    dispatcher.add_handler(CommandHandler('start', start))

    # indica que quan el bot rebi la comanda /help s'executi la funció start
    dispatcher.add_handler(CommandHandler('help', help))

    # indica que quan el bot rebi la comanda /author s'executi la funció start
    dispatcher.add_handler(CommandHandler('author', author))

    print("chaobot")


if __name__ == '__main__':
    main()