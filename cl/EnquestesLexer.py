# Generated from Enquestes.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\6\4\"\n\4\r\4\16\4#\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\6\7\63\n\7\r\7\16")
        buf.write("\7\64\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\4\3\2")
        buf.write("\62;\4\2\f\f\"\"\29\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5")
        buf.write("\27\3\2\2\2\7!\3\2\2\2\t%\3\2\2\2\13/\3\2\2\2\r\62\3\2")
        buf.write("\2\2\17\20\7R\2\2\20\21\7]\2\2\21\22\7\62\2\2\22\23\7")
        buf.write("/\2\2\23\24\7;\2\2\24\25\7_\2\2\25\26\7-\2\2\26\4\3\2")
        buf.write("\2\2\27\30\7R\2\2\30\31\7T\2\2\31\32\7G\2\2\32\33\7I\2")
        buf.write("\2\33\34\7W\2\2\34\35\7P\2\2\35\36\7V\2\2\36\37\7C\2\2")
        buf.write("\37\6\3\2\2\2 \"\t\2\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2")
        buf.write("\2#$\3\2\2\2$\b\3\2\2\2%&\7]\2\2&\'\7c\2\2\'(\7/\2\2(")
        buf.write(")\7|\2\2)*\7C\2\2*+\7/\2\2+,\7\\\2\2,-\7_\2\2-.\7-\2\2")
        buf.write(".\n\3\2\2\2/\60\7<\2\2\60\f\3\2\2\2\61\63\t\3\2\2\62\61")
        buf.write("\3\2\2\2\63\64\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\66\3\2\2\2\66\67\b\7\2\2\67\16\3\2\2\2\5\2#\64\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class EnquestesLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PID = 1
    PREGUNTA = 2
    NUM = 3
    WORD = 4
    PUNTOS = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'P[0-9]+'", "'PREGUNTA'", "'[a-zA-Z]+'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "PID", "PREGUNTA", "NUM", "WORD", "PUNTOS", "WS" ]

    ruleNames = [ "PID", "PREGUNTA", "NUM", "WORD", "PUNTOS", "WS" ]

    grammarFileName = "Enquestes.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


