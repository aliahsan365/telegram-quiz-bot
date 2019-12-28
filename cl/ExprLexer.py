# Generated from Expr.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("#\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\6\2\21\n\2\r\2\16\2\22\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\6\7\36\n\7\r\7\16\7\37\3\7\3\7\2\2\b\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\3\2\4\3\2\62;\4\2\f\f\"\"\2$\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\3\20\3\2\2\2\5\24\3\2\2\2\7\26\3\2\2\2")
        buf.write("\t\30\3\2\2\2\13\32\3\2\2\2\r\35\3\2\2\2\17\21\t\2\2\2")
        buf.write("\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2")
        buf.write("\2\23\4\3\2\2\2\24\25\7-\2\2\25\6\3\2\2\2\26\27\7/\2\2")
        buf.write("\27\b\3\2\2\2\30\31\7,\2\2\31\n\3\2\2\2\32\33\7\61\2\2")
        buf.write("\33\f\3\2\2\2\34\36\t\3\2\2\35\34\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\b\7\2\2\"\16")
        buf.write("\3\2\2\2\5\2\22\37\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    MES = 2
    MENYS = 3
    MUL = 4
    DIV = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "MES", "MENYS", "MUL", "DIV", "WS" ]

    ruleNames = [ "NUM", "MES", "MENYS", "MUL", "DIV", "WS" ]

    grammarFileName = "Expr.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


