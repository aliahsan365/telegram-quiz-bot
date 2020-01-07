
def quiz(bot, update, args):
    try:
        G = load_graph()
        EID = args[0]
        if (EID in list(G.nodes)):
            bot.send_message(chat_id=update.message.chat_id, text="esta")
            #camino = dfs_encuesta(G,EID)
            #bot.send_message(chat_id=update.message.chat_id, text=str(camino))
            #user =  update.message.from_user
            #print(user)
            #bot.set_update_listener(listener)
            while True:
                user = update.message.from_user
                sentence = update.message.text
                update.message.reply_text(sentence)
                #bot.send_message(chat_id=update.message.chat_id, text=)


        else:
            bot.send_message(chat_id=update.message.chat_id, text="no esta")





        bot.send_message(chat_id=update.message.chat_id, text=EID)



    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')
