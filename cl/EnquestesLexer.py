# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\6\2\23\n\2\r\2\16\2\24\3\3\6\3\30\n\3\r\3")
        buf.write("\16\3\31\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b%\n\b")
        buf.write("\r\b\16\b&\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\3\2\5\3\2\62;\3\2c|\4\2\f\f\"\"\2,\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\3\22\3\2\2\2\5\27\3\2\2\2\7\33\3\2\2\2")
        buf.write("\t\35\3\2\2\2\13\37\3\2\2\2\r!\3\2\2\2\17$\3\2\2\2\21")
        buf.write("\23\t\2\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2")
        buf.write("\24\25\3\2\2\2\25\4\3\2\2\2\26\30\t\3\2\2\27\26\3\2\2")
        buf.write("\2\30\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\6\3\2")
        buf.write("\2\2\33\34\7-\2\2\34\b\3\2\2\2\35\36\7/\2\2\36\n\3\2\2")
        buf.write("\2\37 \7,\2\2 \f\3\2\2\2!\"\7\61\2\2\"\16\3\2\2\2#%\t")
        buf.write("\4\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2")
        buf.write("\2\2()\b\b\2\2)\20\3\2\2\2\6\2\24\31&\3\b\2\2")
        return buf.getvalue()


class EnquestesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM = 1
    ID = 2
    MES = 3
    MENYS = 4
    MUL = 5
    DIV = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "ID", "MES", "MENYS", "MUL", "DIV", "WS" ]

    ruleNames = [ "NUM", "ID", "MES", "MENYS", "MUL", "DIV", "WS" ]

    grammarFileName = "Enquestes.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


