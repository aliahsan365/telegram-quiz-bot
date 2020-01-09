
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
####################


def primera_pregunta(bot,update,user_data):

    eid = user_data['nodoencuesta']
    vecinos_enq = list(G.successors(eid))
    for p in vecinos_enq:
        if G.nodes[p]['tipo'] == 'pregunta':
            vecinos_p = list(G.successors(p))
            for vp in vecinos_p:
                if G[p][vp]['color'] == 'blue':
                    preg = pregunta(G,p)
                    resp = resposta(G,vp)
                    text = eid +'> ' + preg + '\n' + resp
                    bot.send_message(chat_id=update.message.chat_id, text=text)
                    opc = update.message.text
                    print(opc)

                    user_data['respuestas'][p] = opc
            user_data['nodoactual'] = p

    return p




def formular_pregunta(bot,update,user_data):
    bot.send_message(chat_id=update.message.chat_id, text=user_data['nodoactual'])
    cp = user_data['nodoactual']
    vecinos_cp = list(G.successors(cp))
    print('soy cp '+ cp)
    for ncp in vecinos_cp:
        if G[cp][ncp]['color'] == 'black' and G[cp][ncp]['senyal'] == user_data['nodoencuesta']:
            vecino_ncp = list(G.successors(ncp))
            for vncp in vecino_ncp:
                if G[ncp][vncp]['color'] == 'blue':
                    preg = pregunta(G,ncp)
                    resp = resposta(G,vncp)
                    text = user_data['nodoencuesta'] + '> ' + preg + '\n' + resp
                    bot.send_message(chat_id=update.message.chat_id, text=text)
                    opc = update.message.text
                    user_data['respuestas'][ncp] = opc
                    user_data['nodoactual'] = ncp
    return ncp


def pie(bot,update,args):
    try:
        PID = args[0]
        bot.send_message(chat_id=update.message.chat_id, text=PID)

        stats = load_stats()
        bot.send_message(chat_id=update.message.chat_id, text=stats)
        filename = "%d.png" % random.randint(0000000, 9999999)
        labels = [op for op in stats[PID].keys()]  # answer options
        bot.send_message(chat_id=update.message.chat_id, text=labels)
        values = [val for val in stats[PID].values()]  # answer values
        explode = [0.1 for v in values]
        plt.pie(values,labels=labels)
        plt.savefig(filename, bbox_inches='tight')
        #plt.show()
        plt.clf()
        bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))
        os.remove(filename)


    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')

#################################################

def quiz(bot, update, args, user_data):
    try:
        EID = args[0]
        bot.send_message(chat_id=update.message.chat_id, text=EID)

        user_data['nodoencuesta'] = EID
        vecinos = G.successors(EID)
        for v in vecinos:
            if (G[EID][v]['color'] == 'black' and G[EID][v]['content'])


        user_data['visited'] = []

        user_data['nodoactual'] = G.successors
        user_data['respuestas'] = dict()

    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')





def encuesta(bot,update,user_data):
    try:
        bot.send_message(chat_id=update.message.chat_id, text=update.message.text)







########################## END HANDLER FUNCTIONS#########################


######LOGICS ###################
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


def dfs_alternativa(bot,update,user_data):
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




def encuesta(bot,update,user_data):
    try:
        stack = Stack()
        stack.push(user_data['encuesta'])
        visited = [] # user_data['encuesta']
        while (not stack.isEmpty()):
            c_node = stack.top()
            stack.pop()
            vecinos = list(G.successors(c_node))
            for v in vecinos:
                if (not (v in visited)):
                    if (G[c_node][v]['color'] == 'black' and G[c_node][v]['senyal'] == EID):
                        if G.nodes[v]['tipo'] == "pregunta":
                            vecinos_del_vecino = list(G.successors(v))
                            opc = 'opc'
                            for vdv in vecinos_del_vecino:
                                if G[v][vdv]['color'] == 'blue':
                                    pregunta(G, v)
                                    resposta(G, vdv)
                                    opc = input()
                            for vdv in vecinos_del_vecino:
                                if G[v][vdv]['color'] == 'green':

                                    if (G[v][vdv]['label'] == opc):
                                        nodos_respondidos = dfs_alternativa(bot,update,user_data)
                                        for i in range(len(nodos_respondidos)):
                                            visited.append(nodos_respondidos[i])

                        stack.push(v)
            visited.append(c_node)
        return visited
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text='💣')




