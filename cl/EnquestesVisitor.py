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


from pathlib import Path



data_folder = Path("cl")

file_to_save = data_folder / "graph.pickle"


def save_graph(G):
    pickle_out = open("graph.pickle", "wb")
    pickle.dump(G,pickle_out)
    pickle_out.close()

def load_graph():
    pickle_in = open("graph.pickle","rb")
    Gin = pickle.load(pickle_in)
    print(Gin.nodes, Gin.edges)


def render_graph(G):
    layout = nx.circular_layout(G)
    arestas = G.edges()
    colores = [G[u][v]['color'] for u, v in arestas]
    nx.draw(G, layout, arrow=True , with_labels=True, edge_color=colores )
    tags = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, layout, edge_labels=tags)
    plt.show()



def mount_graph(G,items,encuestas):
    for e in encuestas:
        l_items = e[1:]
        res = []
        for i in l_items:
            for e_l in items:
                if e_l[0] == i:
                    res.append(e_l[1])
        lpares= []
        semibool = 1
        n = len(res)
        for i in range(0,n-1):
            if semibool == 1:
                G.add_edge(e[0], res[i], color='black')
                semibool = 0
            lpares.append((res[i],res[i+1]))
            G.add_edge(res[i], res[i+1], color = 'black')
        #el ultimo -> al end
        G.add_edge(res[n-1],'END', color = 'black')

class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    G = nx.DiGraph()
    items = []

    encuestas = []

    def getGraph(self):
        return self.G

    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)
        ID_END = ctx.getChild(1).getText()
        self.G.add_node(ID_END)
        mount_graph(self.G,self.items,self.encuestas)
        render_graph(self.G)
        save_graph(self.G)
        load_graph()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocs.
    def visitBlocs(self, ctx:EnquestesParser.BlocsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        res = []
        for i in range(ctx.getChildCount()):
            res.append(ctx.getChild(i).getText())
        self.G.add_node(ctx.getChild(0).getText(), content=' '.join(res[3:len(res)-1])+'?')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        RID = ctx.getChild(0).getText()
        n = ctx.getChildCount()
        res = []
        for i in range(n-3):
            res.append(self.visit(ctx.getChild(i+3)))
        self.G.add_node(RID, content = res)



    #Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        opc = ctx.getChild(0).getText()
        palabras = ctx.getChild(2).getText()
        return (opc,palabras)


    # Visit a parse tree produced by EnquestesParser#element.
    def visitElement(self, ctx:EnquestesParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#relacio.
    def visitRelacio(self, ctx:EnquestesParser.RelacioContext):
        IID = ctx.parentCtx.getChild(0).getText()
        PID = ctx.getChild(0).getText()
        RID = ctx.getChild(2).getText()
        tp = (IID,PID,RID)
        self.items.append(tp)
        self.G.add_edge(PID, RID, label = IID, color = 'blue')
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

        IID = ctx.parentCtx.parentCtx.getChild(0).getText()
        OPC = ctx.getChild(1).getText()
        IID_OPC = ctx.getChild(3).getText()
        preguntaOri = 'preguntaOri'
        preguntaDest = 'preguntaDest'
        #si hay que volver se puede ir cargando el una tupla que lo relacione all.
        for i in range(len(self.items)):
            if self.items[i][0] == IID:
                preguntaOri = self.items[i][1]
        for i in range(len(self.items)):
            if self.items[i][0] == IID_OPC:
                preguntaDest = self.items[i][1]
        self.G.add_edge(preguntaOri, preguntaDest, label = OPC, color = 'green')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        EID = ctx.getChild(0).getText()
        n = ctx.getChildCount()
        items_encuesta = []

        for i in range(3,n):
            items_encuesta.append(ctx.getChild(i).getText())
        #lista de preguntas
        lp = []
        lp.append(EID)
        for item_encuesta in items_encuesta:
            for generic_item in self.items:
                if item_encuesta == generic_item[0]:
                    lp.append(generic_item[1])
        lp.append('END')
        camino = []
        for i in range(0,len(lp)-1):
            camino.append((lp[i], lp[i+1]))
        self.G.add_node(EID, content = camino)
        nx.add_path(self.G, lp, color='black')
        return self.visitChildren(ctx)

del EnquestesParser