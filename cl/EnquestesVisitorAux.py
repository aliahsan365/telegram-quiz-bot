# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.
import networkx as nx
import matplotlib.pyplot as plt

def render_graph(G):
    pos = nx.circular_layout(G)

    nx.draw(G, pos, with_labels=True, font_weight='bold',arrow =True)
    #plt.draw()
    plt.show()



class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    G = nx.Graph()
    def getGraph(self):
        return self.G

    def visitRoot(self, ctx:EnquestesParser.RootContext):
        self.visitChildren(ctx)
        render_graph(self.G)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocs.
    def visitBlocs(self, ctx:EnquestesParser.BlocsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        #print(ctx.getChild(0).getText())
        self.G.add_node(ctx.getChild(0).getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        self.G.add_node(ctx.getChild(0).getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#element.
    def visitElement(self, ctx:EnquestesParser.ElementContext):
        self.G.add_node(ctx.getChild(0).getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#relacio.
    def visitRelacio(self, ctx:EnquestesParser.RelacioContext):
        IID = ctx.parentCtx.getChild(2).getText()
        print(IID)
        PID = ctx.getChild(0).getText()
        RID = ctx.getChild(2).getText()

        self.G.add_edge(PID, RID, weight=IID, color='b')
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        return self.visitChildren(ctx)



del EnquestesParser



