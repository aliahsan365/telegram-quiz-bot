import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

import pickle
print(pickle.__doc__)

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

#sumalista para el piechart

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

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# engega el bot
updater.start_polling()

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




# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))

# indica que quan el bot rebi la comanda /help s'executi la funció start
dispatcher.add_handler(CommandHandler('help', help))

# indica que quan el bot rebi la comanda /author s'executi la funció start
dispatcher.add_handler(CommandHandler('author', author))


#update.message.text conté el text enviat per l’usuari,

