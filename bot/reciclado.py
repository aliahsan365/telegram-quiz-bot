
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




---
if user_data is None:
    user_data['encuesta'] = args[0]
else:
    print(user_data['encuesta'])
    print('aaaaaaaaaaaaaaaaaaahhh')





------------



estadisticas = dict()


def save_graph(estadisticas):
    pickle_out = open("estadisticas.pickle", "wb")
    pickle.dump(G,pickle_out)
    pickle_out.close()



def load_graph():
    pickle_in = open("stats.pickle","rb")
     = pickle.load(pickle_in)
    return Gin

estaditicas_generales = {{p1:{opc1,contador},{opc2,contador},...},{p2:{opc1,contador},{opc2,contador},...}...}

def actualizar_estadisticas():
    #dicionariodelusuario
    #por cada preguntaz en diccionario usuario
    user_data = {{p1,opc},{p2,opc}....}

    if p1 in estadisticas:
         dict = estadisticas[p1]
         //opc como key de dict nuevo
