import sys
from antlr4 import *
from ExprLexer import ExprLexer  # Alterado para ExprLexer
from ExprParser import ExprParser  # Alterado para ExprParser

# Função para testar o código na sua linguagem (Expr)
def test_expr_code(code):
    # Cria um fluxo de entrada para o código fonte
    input_stream = InputStream(code)
    
    # Cria o lexer e passa o fluxo de entrada
    lexer = ExprLexer(input_stream)  # Alterado para ExprLexer
    
    # Cria o stream de tokens gerado pelo lexer
    token_stream = CommonTokenStream(lexer)
    
    # Cria o parser e passa o fluxo de tokens
    parser = ExprParser(token_stream)  # Alterado para ExprParser
    
    # Tenta analisar o código, chamando a função de parsing inicial
    try:
        # Aqui, chamamos a regra de parsing inicial do seu parser
        # Caso o seu parser use a regra `programa` (dependendo do que você nomeou), você deve chamá-la
        tree = parser.programa()  # Ajuste conforme a regra inicial definida na sua gramática
        print("Código sintaticamente válido!")
        
    except Exception as e:
        print("Erro sintático:", e)

# Exemplo de código a ser testado
codigo_teste = """
@start
roar n as int;
roar linha as text;
roar i as int;
roar j as int:

leia(n);

if n < 1 then {
    roarout('Erro: n deve ser maior ou igual a 1!');
} else {
    i = 0;
    while i < n strike {
        linha = "1";
        j = 1;
        while j < i strike {
            linha = linha + " " + (i * (i - 1)) / 2;  
            j = j + 1;
        }
        roarout(linha);
        i = i + 1;
    }
}
@end

"""



# Chama a função de teste
test_expr_code(codigo_teste)
    