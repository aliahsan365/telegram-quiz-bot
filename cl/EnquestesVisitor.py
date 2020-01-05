# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
import networkx as nx



class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    items = []
    def __init__(self,G):
        self.G = G
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)
        #es el nodo END ctx.getChild(1).getText()
        self.G.add_node(ctx.getChild(1).getText() , content= "END.THANKS", tipo = "final")



    # Visit a parse tree produced by EnquestesParser#blocs.
    def visitBlocs(self, ctx:EnquestesParser.BlocsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        res = []
        for i in range(ctx.getChildCount()):
            res.append(ctx.getChild(i).getText())
        self.G.add_node(ctx.getChild(0).getText(), content=' '.join(res[3:len(res)-1])+'?', tipo = "pregunta")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        RID = ctx.getChild(0).getText()
        n = ctx.getChildCount()
        res = []
        for i in range(n-3):
            res.append(self.visit(ctx.getChild(i+3)))
        self.G.add_node(RID, content = res,tipo = "respuesta")



    #Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        opc = ctx.getChild(0).getText()
        n = ctx.getChildCount()
        palabras = []
        for i in range(n-2):
            palabras.append(ctx.getChild(i+2).getText())
        #esto del  join es para unir una lista de palabras cn espacio
        #el -1 es para ahorrarse el ;
        return (opc,' '.join(palabras[:len(palabras)-1]))


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

        for item_encuesta in items_encuesta:
            for generic_item in self.items:
                if item_encuesta == generic_item[0]:
                    lp.append(generic_item[1])


        print(lp)
        self.G.add_node(EID, content=lp, tipo = "encuesta")
        semibool = 1

        for i in range(len(lp)-1):
            if semibool == 1:
                self.G.add_edge(EID, lp[i], color='black', senyal = EID)
                semibool = 0
            self.G.add_edge(lp[i], lp[i+1], color = 'black', senyal = EID)
        self.G.add_edge(lp[len(lp)-1], 'END', color='black', senyal=EID)




        return self.visitChildren(ctx)

del EnquestesParser