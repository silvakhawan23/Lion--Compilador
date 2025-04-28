# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,3,4,3,48,8,3,11,3,12,3,49,1,4,1,4,1,4,1,4,1,4,
        3,4,57,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,5,7,75,8,7,10,7,12,7,78,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,5,10,97,8,10,10,10,12,
        10,100,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,
        11,112,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,122,8,11,
        10,11,12,11,125,9,11,1,12,1,12,1,13,1,13,1,13,0,1,22,14,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,0,3,1,0,6,7,1,0,21,24,1,0,25,28,129,
        0,28,1,0,0,0,2,38,1,0,0,0,4,44,1,0,0,0,6,47,1,0,0,0,8,56,1,0,0,0,
        10,58,1,0,0,0,12,63,1,0,0,0,14,69,1,0,0,0,16,82,1,0,0,0,18,89,1,
        0,0,0,20,94,1,0,0,0,22,111,1,0,0,0,24,126,1,0,0,0,26,128,1,0,0,0,
        28,32,5,1,0,0,29,31,3,2,1,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,
        0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,3,6,3,0,36,
        37,5,2,0,0,37,1,1,0,0,0,38,39,5,3,0,0,39,40,5,29,0,0,40,41,5,4,0,
        0,41,42,3,4,2,0,42,43,5,5,0,0,43,3,1,0,0,0,44,45,7,0,0,0,45,5,1,
        0,0,0,46,48,3,8,4,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,
        50,1,0,0,0,50,7,1,0,0,0,51,57,3,10,5,0,52,57,3,12,6,0,53,57,3,14,
        7,0,54,57,3,16,8,0,55,57,3,18,9,0,56,51,1,0,0,0,56,52,1,0,0,0,56,
        53,1,0,0,0,56,54,1,0,0,0,56,55,1,0,0,0,57,9,1,0,0,0,58,59,5,29,0,
        0,59,60,5,8,0,0,60,61,3,22,11,0,61,62,5,5,0,0,62,11,1,0,0,0,63,64,
        5,9,0,0,64,65,5,10,0,0,65,66,5,29,0,0,66,67,5,11,0,0,67,68,5,5,0,
        0,68,13,1,0,0,0,69,70,5,12,0,0,70,71,5,10,0,0,71,76,3,22,11,0,72,
        73,5,13,0,0,73,75,3,22,11,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,
        0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,11,0,0,80,
        81,5,5,0,0,81,15,1,0,0,0,82,83,5,14,0,0,83,84,3,22,11,0,84,85,5,
        15,0,0,85,86,3,20,10,0,86,87,5,16,0,0,87,88,3,20,10,0,88,17,1,0,
        0,0,89,90,5,17,0,0,90,91,3,22,11,0,91,92,5,18,0,0,92,93,3,20,10,
        0,93,19,1,0,0,0,94,98,5,19,0,0,95,97,3,8,4,0,96,95,1,0,0,0,97,100,
        1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,
        0,101,102,5,20,0,0,102,21,1,0,0,0,103,104,6,11,-1,0,104,105,5,10,
        0,0,105,106,3,22,11,0,106,107,5,11,0,0,107,112,1,0,0,0,108,112,5,
        30,0,0,109,112,5,31,0,0,110,112,5,29,0,0,111,103,1,0,0,0,111,108,
        1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,123,1,0,0,0,113,114,
        10,6,0,0,114,115,3,24,12,0,115,116,3,22,11,7,116,122,1,0,0,0,117,
        118,10,5,0,0,118,119,3,26,13,0,119,120,3,22,11,6,120,122,1,0,0,0,
        121,113,1,0,0,0,121,117,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,
        123,124,1,0,0,0,124,23,1,0,0,0,125,123,1,0,0,0,126,127,7,1,0,0,127,
        25,1,0,0,0,128,129,7,2,0,0,129,27,1,0,0,0,8,32,49,56,76,98,111,121,
        123
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@start'", "'@end'", "'roar'", "'as'", 
                     "';'", "'int'", "'text'", "'='", "'hunt'", "'('", "')'", 
                     "'roarout'", "','", "'if'", "'then'", "'else'", "'while'", 
                     "'strike'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", 
                     "'&&'", "'||'", "'!'", "'=='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "STRING", "WS", "COMMENT" ]

    RULE_programa = 0
    RULE_declaracao = 1
    RULE_tipo = 2
    RULE_comandos = 3
    RULE_comando = 4
    RULE_atribuicao = 5
    RULE_entrada = 6
    RULE_saida = 7
    RULE_condicional = 8
    RULE_repeticao = 9
    RULE_bloco = 10
    RULE_expressao = 11
    RULE_aritmetica_op = 12
    RULE_logico_op = 13

    ruleNames =  [ "programa", "declaracao", "tipo", "comandos", "comando", 
                   "atribuicao", "entrada", "saida", "condicional", "repeticao", 
                   "bloco", "expressao", "aritmetica_op", "logico_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    ID=29
    INT=30
    STRING=31
    WS=32
    COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(ExprParser.ComandosContext,0)


        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.DeclaracaoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ExprParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ExprParser.T__0)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 29
                self.declaracao()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.comandos()
            self.state = 36
            self.match(ExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(ExprParser.TipoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)




    def declaracao(self):

        localctx = ExprParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ExprParser.T__2)
            self.state = 39
            self.match(ExprParser.ID)
            self.state = 40
            self.match(ExprParser.T__3)
            self.state = 41
            self.tipo()
            self.state = 42
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = ExprParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==6 or _la==7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = ExprParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.comando()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 537022976) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(ExprParser.AtribuicaoContext,0)


        def entrada(self):
            return self.getTypedRuleContext(ExprParser.EntradaContext,0)


        def saida(self):
            return self.getTypedRuleContext(ExprParser.SaidaContext,0)


        def condicional(self):
            return self.getTypedRuleContext(ExprParser.CondicionalContext,0)


        def repeticao(self):
            return self.getTypedRuleContext(ExprParser.RepeticaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = ExprParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.atribuicao()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.entrada()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.saida()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.condicional()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.repeticao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = ExprParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ExprParser.ID)
            self.state = 59
            self.match(ExprParser.T__7)
            self.state = 60
            self.expressao(0)
            self.state = 61
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EntradaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_entrada

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEntrada" ):
                listener.enterEntrada(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEntrada" ):
                listener.exitEntrada(self)




    def entrada(self):

        localctx = ExprParser.EntradaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_entrada)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(ExprParser.T__8)
            self.state = 64
            self.match(ExprParser.T__9)
            self.state = 65
            self.match(ExprParser.ID)
            self.state = 66
            self.match(ExprParser.T__10)
            self.state = 67
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaidaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_saida

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaida" ):
                listener.enterSaida(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaida" ):
                listener.exitSaida(self)




    def saida(self):

        localctx = ExprParser.SaidaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_saida)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(ExprParser.T__11)
            self.state = 70
            self.match(ExprParser.T__9)
            self.state = 71
            self.expressao(0)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 72
                self.match(ExprParser.T__12)
                self.state = 73
                self.expressao(0)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(ExprParser.T__10)
            self.state = 80
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlocoContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlocoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = ExprParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ExprParser.T__13)
            self.state = 83
            self.expressao(0)
            self.state = 84
            self.match(ExprParser.T__14)
            self.state = 85
            self.bloco()
            self.state = 86
            self.match(ExprParser.T__15)
            self.state = 87
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeticaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def bloco(self):
            return self.getTypedRuleContext(ExprParser.BlocoContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_repeticao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeticao" ):
                listener.enterRepeticao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeticao" ):
                listener.exitRepeticao(self)




    def repeticao(self):

        localctx = ExprParser.RepeticaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_repeticao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ExprParser.T__16)
            self.state = 90
            self.expressao(0)
            self.state = 91
            self.match(ExprParser.T__17)
            self.state = 92
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ComandoContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = ExprParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(ExprParser.T__18)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 537022976) != 0):
                self.state = 95
                self.comando()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(ExprParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expressao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AritmeticaContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)

        def aritmetica_op(self):
            return self.getTypedRuleContext(ExprParser.Aritmetica_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica" ):
                listener.enterAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica" ):
                listener.exitAritmetica(self)


    class ParensContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(ExprParser.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class VarContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class StringContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class IntContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class LogicaContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressaoContext,i)

        def logico_op(self):
            return self.getTypedRuleContext(ExprParser.Logico_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogica" ):
                listener.enterLogica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogica" ):
                listener.exitLogica(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 104
                self.match(ExprParser.T__9)
                self.state = 105
                self.expressao(0)
                self.state = 106
                self.match(ExprParser.T__10)
                pass
            elif token in [30]:
                localctx = ExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(ExprParser.INT)
                pass
            elif token in [31]:
                localctx = ExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(ExprParser.STRING)
                pass
            elif token in [29]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.AritmeticaContext(self, ExprParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 113
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 114
                        self.aritmetica_op()
                        self.state = 115
                        self.expressao(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.LogicaContext(self, ExprParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 117
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 118
                        self.logico_op()
                        self.state = 119
                        self.expressao(6)
                        pass

             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Aritmetica_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_aritmetica_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAritmetica_op" ):
                listener.enterAritmetica_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAritmetica_op" ):
                listener.exitAritmetica_op(self)




    def aritmetica_op(self):

        localctx = ExprParser.Aritmetica_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_aritmetica_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logico_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_logico_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico_op" ):
                listener.enterLogico_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico_op" ):
                listener.exitLogico_op(self)




    def logico_op(self):

        localctx = ExprParser.Logico_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_logico_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




