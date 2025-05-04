from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
import sys
import os
def main():
   
    path = os.path.join(os.path.dirname(__file__), "teste.lion")
    input_stream = FileStream(path, encoding='utf-8')

    # Lexer
    lexer = ExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    print("Tokens reconhecidos:")
    token_stream.fill()
    for token in token_stream.tokens:
        if token.type != Token.EOF:
            print(f"{token.text} -> {lexer.symbolicNames[token.type]}")

    # Parser
    parser = ExprParser(token_stream)
    try:
        parser.program()  # esse deve ser o nome da sua regra inicial
        print("\nAnálise concluída com sucesso! Nenhum erro léxico ou sintático encontrado.")
    except Exception as e:
        print(f"\n{e}")

if __name__ == "__main__":
    main()
