# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .EnquestesParser import EnquestesParser
else:
    from EnquestesParser import EnquestesParser

# This class defines a complete generic visitor for a parse tree produced by EnquestesParser.

class EnquestesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by EnquestesParser#root.
    def visitRoot(self, ctx:EnquestesParser.RootContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("root")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocs.
    def visitBlocs(self, ctx:EnquestesParser.BlocsContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("blocs")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#pregunta.
    def visitPregunta(self, ctx:EnquestesParser.PreguntaContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("pregunta")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#resposta.
    def visitResposta(self, ctx:EnquestesParser.RespostaContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("resposta")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#opcio.
    def visitOpcio(self, ctx:EnquestesParser.OpcioContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("opcio")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#element.
    def visitElement(self, ctx:EnquestesParser.ElementContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("element")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#relacio.
    def visitRelacio(self, ctx:EnquestesParser.RelacioContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("relacio")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#alternativa.
    def visitAlternativa(self, ctx:EnquestesParser.AlternativaContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("alternativa")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#implications.
    def visitImplications(self, ctx:EnquestesParser.ImplicationsContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("implications")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#blocrespostaelement.
    def visitBlocrespostaelement(self, ctx:EnquestesParser.BlocrespostaelementContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("blocrespostaelement")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#respostaelement.
    def visitRespostaelement(self, ctx:EnquestesParser.RespostaelementContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("resporataelement")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by EnquestesParser#enquesta.
    def visitEnquesta(self, ctx:EnquestesParser.EnquestaContext):
        print(ctx.getChildCount())
        g = ctx.getChildren()
        print("enquesta")
        for i in range(ctx.getChildCount()):
            elem = next(g)
            print(elem)

        return self.visitChildren(ctx)



#del EnquestesParser
