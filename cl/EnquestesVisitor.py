# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
import networkx as nx
import matplotlib.pyplot as plt
import pickle
import os

my_path = os.path.abspath(__file__)
print(my_path)

my_file = 'graph.png'

def save_graph(G):
    pickle_out = open("graph.pickle", "wb")

    pickle.dump(G,pickle_out)
    pickle_out.close()


#TODO: todotest
#FIXME: fixmetest
#REVIEw: review
def load_graph():
    pickle_in = open("graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    #print(Gin.nodes,Gin.edges)




def render_graph(G):
    save_graph(G)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', arrow=True)
    load_graph()
    #print("overall")
    #print(G.nodes)
    #print(G.edges)
    plt.show()
    #fig = plt.figure()
    #fig.savefig(os.path.join(my_path, my_file))
    #plt.close(fig)





#resposta : RID PUNTS RESPOSTA opcio*;
#opcio : NUMERO PUNTS PARAULES* PUNTCOMA;
class Resposta():
    def __init__(self,rid,punts):
        self.rid = rid
        self.punts = punts



#TODO: estrucutras para guardar el grafo.


def mount_graph(G,items,alternativas,encuestas):

    #l_en = encuestas[1:]

    print("mount graph")
    print(len(encuestas))


    for e in encuestas:
        l_items = e[1:]
        res = []
        for i in l_items:
            for e_l in items:
                if e_l[0] == i:
                    res.append(e_l[1])
        for r in res:
            print(r)
        lpares= []
        for i in range(0,len(res)-1):
            lpares.append((res[i],res[i+1]))
        print(lpares)















class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    G = nx.DiGraph()
    #G = nx.Graph()
    preguntas = []
    respuestas = []
    item = []
    res_item = []
    encuestas = []

    def getGraph(self):
        return self.G

    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)

        self.G.add_node(ctx.getChild(1).getText())
        print("root")
        print(self.G.nodes)
        print(self.G.edges)
        todo = []
        print("respuestas")
        for r in self.respuestas:
            todo.append(r)
            print(r)
        print("preguntas")
        for p in self.preguntas:
            todo.append(p)
            print(p)
        print("items")
        for i in self.item:
            print(i)
        print("respuestas_items")
        for ri in self.res_item:
            print(ri)
        print("encuestas")
        for e in self.encuestas:
            print(e)
        mount_graph(self.G,self.item,self.res_item,self.encuestas)
        render_graph(self.G)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocs.
    def visitBlocs(self, ctx:EnquestesParser.BlocsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        #print(ctx.getChild(0).getText())
        self.G.add_node(ctx.getChild(0).getText())
        n = ctx.getChildCount()
        res = []
        for i in range(n):
            res.append(ctx.getChild(i).getText())
        self.preguntas.append(res)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        self.G.add_node(ctx.getChild(0).getText())
        n = ctx.getChildCount()
        res = []
        for i in range(n):
            res.append(ctx.getChild(i).getText())
        self.respuestas.append(res)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#element.
    def visitElement(self, ctx:EnquestesParser.ElementContext):

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#relacio.
    def visitRelacio(self, ctx:EnquestesParser.RelacioContext):

        IID = ctx.parentCtx.getChild(0).getText()
        #print(IID)
        PID = ctx.getChild(0).getText()
        RID = ctx.getChild(2).getText()

        #self.G.add_edge(PID, RID, label = IID, color='b')

        tp = (IID,PID,RID)
        self.item.append(tp)
        self.G.add_edge(PID, RID)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#implications.
    def visitImplications(self, ctx:EnquestesParser.ImplicationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocrespostaelement.
    def visitBlocrespostaelement(self, ctx:EnquestesParser.BlocrespostaelementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#respostaelement.
    def visitRespostaelement(self, ctx:EnquestesParser.RespostaelementContext):
        AID = ctx.parentCtx.parentCtx.parentCtx.getChild(0).getText()
        OPC = ctx.getChild(1).getText()
        IID = ctx.parentCtx.parentCtx.getChild(0).getText()
        IID_OPC = ctx.getChild(3).getText()

       #print((OPC,IID))
        #PID = "P3"
        #NO SE PUEDE USAR parent cuando no es tu padre inmediato
        #necesitamos una estrcutura aparte del grafo que nos haga de memoria
        #la usaremos para montar el grafo y tambien para implementar las corecciones
        PID = ctx.parentCtx.getChild(0).getText()
        t = (AID,IID,(OPC,IID_OPC))
        self.res_item.append(t)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        EID = ctx.getChild(0).getText()
        self.G.add_node(EID)
        n = ctx.getChildCount()
        res = []
        res.append(EID)
        for i in range(3,n):
            res.append(ctx.getChild(i).getText())
        self.encuestas.append(res)
        #H = nx.path_graph(res[1:])


        #self.G.(res[1:])






        #self.G.add_edges_from(H)
        return self.visitChildren(ctx)

del EnquestesParser