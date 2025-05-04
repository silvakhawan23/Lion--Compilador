from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from graphviz import Digraph
import sys

class ASTVisualizer(ParseTreeListener):
    def __init__(self):
        self.graph = Digraph('AST', format='png')
        self.count = 0
        self.stack = []

    def get_id(self):
        self.count += 1
        return f"node{self.count}"

    def enterEveryRule(self, ctx):
        label = ExprParser.ruleNames[ctx.getRuleIndex()]
        node_id = self.get_id()
        self.graph.node(node_id, label)
        if self.stack:
            self.graph.edge(self.stack[-1], node_id)
        self.stack.append(node_id)

    def exitEveryRule(self, ctx):
        self.stack.pop()

    def visitTerminal(self, node):
        token_text = node.getText()
        node_id = self.get_id()
        self.graph.node(node_id, token_text)
        if self.stack:
            self.graph.edge(self.stack[-1], node_id)

def main():
    input_file = 'teste.lion'  # ou input.txt se preferir
    input_stream = FileStream(input_file, encoding="utf-8")

    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    
    try:
        tree = parser.program()
    except Exception as e:
        print(str(e))
        return

    visualizer = ASTVisualizer()
    walker = ParseTreeWalker()
    walker.walk(visualizer, tree)

    visualizer.graph.render('ast', view=False)  # Gera ast.dot e ast.png
    print("AST gerada como 'ast.dot' e 'ast.png'")

if __name__ == '__main__':
    main()
