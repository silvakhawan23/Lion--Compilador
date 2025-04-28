# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#programa.
    def enterPrograma(self, ctx:ExprParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ExprParser#programa.
    def exitPrograma(self, ctx:ExprParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ExprParser#declaracao.
    def enterDeclaracao(self, ctx:ExprParser.DeclaracaoContext):
        pass

    # Exit a parse tree produced by ExprParser#declaracao.
    def exitDeclaracao(self, ctx:ExprParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by ExprParser#tipo.
    def enterTipo(self, ctx:ExprParser.TipoContext):
        pass

    # Exit a parse tree produced by ExprParser#tipo.
    def exitTipo(self, ctx:ExprParser.TipoContext):
        pass


    # Enter a parse tree produced by ExprParser#comandos.
    def enterComandos(self, ctx:ExprParser.ComandosContext):
        pass

    # Exit a parse tree produced by ExprParser#comandos.
    def exitComandos(self, ctx:ExprParser.ComandosContext):
        pass


    # Enter a parse tree produced by ExprParser#comando.
    def enterComando(self, ctx:ExprParser.ComandoContext):
        pass

    # Exit a parse tree produced by ExprParser#comando.
    def exitComando(self, ctx:ExprParser.ComandoContext):
        pass


    # Enter a parse tree produced by ExprParser#atribuicao.
    def enterAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by ExprParser#atribuicao.
    def exitAtribuicao(self, ctx:ExprParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by ExprParser#entrada.
    def enterEntrada(self, ctx:ExprParser.EntradaContext):
        pass

    # Exit a parse tree produced by ExprParser#entrada.
    def exitEntrada(self, ctx:ExprParser.EntradaContext):
        pass


    # Enter a parse tree produced by ExprParser#saida.
    def enterSaida(self, ctx:ExprParser.SaidaContext):
        pass

    # Exit a parse tree produced by ExprParser#saida.
    def exitSaida(self, ctx:ExprParser.SaidaContext):
        pass


    # Enter a parse tree produced by ExprParser#condicional.
    def enterCondicional(self, ctx:ExprParser.CondicionalContext):
        pass

    # Exit a parse tree produced by ExprParser#condicional.
    def exitCondicional(self, ctx:ExprParser.CondicionalContext):
        pass


    # Enter a parse tree produced by ExprParser#repeticao.
    def enterRepeticao(self, ctx:ExprParser.RepeticaoContext):
        pass

    # Exit a parse tree produced by ExprParser#repeticao.
    def exitRepeticao(self, ctx:ExprParser.RepeticaoContext):
        pass


    # Enter a parse tree produced by ExprParser#bloco.
    def enterBloco(self, ctx:ExprParser.BlocoContext):
        pass

    # Exit a parse tree produced by ExprParser#bloco.
    def exitBloco(self, ctx:ExprParser.BlocoContext):
        pass


    # Enter a parse tree produced by ExprParser#Aritmetica.
    def enterAritmetica(self, ctx:ExprParser.AritmeticaContext):
        pass

    # Exit a parse tree produced by ExprParser#Aritmetica.
    def exitAritmetica(self, ctx:ExprParser.AritmeticaContext):
        pass


    # Enter a parse tree produced by ExprParser#Parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#Parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#Var.
    def enterVar(self, ctx:ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#Var.
    def exitVar(self, ctx:ExprParser.VarContext):
        pass


    # Enter a parse tree produced by ExprParser#String.
    def enterString(self, ctx:ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#String.
    def exitString(self, ctx:ExprParser.StringContext):
        pass


    # Enter a parse tree produced by ExprParser#Int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#Int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#Logica.
    def enterLogica(self, ctx:ExprParser.LogicaContext):
        pass

    # Exit a parse tree produced by ExprParser#Logica.
    def exitLogica(self, ctx:ExprParser.LogicaContext):
        pass


    # Enter a parse tree produced by ExprParser#aritmetica_op.
    def enterAritmetica_op(self, ctx:ExprParser.Aritmetica_opContext):
        pass

    # Exit a parse tree produced by ExprParser#aritmetica_op.
    def exitAritmetica_op(self, ctx:ExprParser.Aritmetica_opContext):
        pass


    # Enter a parse tree produced by ExprParser#logico_op.
    def enterLogico_op(self, ctx:ExprParser.Logico_opContext):
        pass

    # Exit a parse tree produced by ExprParser#logico_op.
    def exitLogico_op(self, ctx:ExprParser.Logico_opContext):
        pass



del ExprParser