grammar Expr;

// Programa principal
programa
    : '@start' declaracao* comandos '@end'
    ;

// Declarações de variáveis
declaracao
    : 'roar' ID 'as' tipo ';'
    ;

// Tipos primitivos
tipo
    : 'int'
    | 'text'
    ;

// Comandos no programa (entrada, saída, controle de fluxo)
comandos
    : comando+
    ;

comando
    : atribuicao
    | entrada
    | saida
    | condicional
    | repeticao
    ;

// Atribuição de valor
atribuicao
    : ID '=' expressao ';'
    ;

// Comando de entrada
entrada
    : 'hunt' '(' ID ')' ';'
    ;

// Comando de saída
saida
    : 'roarout' '(' expressao (',' expressao)* ')' ';'
    ;

// Comando condicional
condicional
    : 'if' expressao 'then' bloco 'else' bloco
    ;

// Comando de repetição
repeticao
    : 'while' expressao 'strike' bloco
    ;

// Bloco de código (sequência de comandos)
bloco
    : '{' comando* '}'
    ;

// Expressões aritméticas e lógicas
expressao
    : expressao aritmetica_op expressao   # Aritmetica
    | expressao logico_op expressao        # Logica
    | '(' expressao ')'                   # Parens
    | INT                                  # Int
    | STRING                               # String
    | ID                                   # Var
    ;

// Operadores aritméticos (+, -, *, /)
aritmetica_op
    : '+' | '-' | '*' | '/'
    ;

// Operadores lógicos (&&, ||, !, ==)
logico_op
    : '&&' | '||' | '!' | '=='
    ;

// Identificadores
ID
    : [a-zA-Z_][a-zA-Z0-9_]*  
    ;

// Números inteiros
INT
    : [0-9]+
    ;

// Strings
STRING
    : '"' ( ~['"\r\n] | '\\' . )* '"'
    ;

// Espaços em branco e comentários
WS
    : [ \t\r\n]+ -> skip
    ;

COMMENT
    : '//' ~[\r\n]* -> skip
    ;
