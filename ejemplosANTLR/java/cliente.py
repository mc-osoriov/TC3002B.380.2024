from antlr4 import *
from antlr.Java8Lexer import Java8Lexer
from antlr.Java8Parser import Java8Parser
from antlr.Java8ParserListener import Java8ParserListener

import sys

class ClassNameListener(Java8ParserListener):
    def enterNormalClassDeclaration(self, ctx: Java8Parser.NormalClassDeclarationContext):
        print(ctx.Identifier().getText())

    def exitSumadditiveExpression(self, ctx: Java8Parser.SumadditiveExpressionContext):
        if ctx.additiveExpression().tipo == ctx.multiplicativeExpression().tipo:
            ctx.tipo = ctx.additiveExpression().tipo
        else:
            raise Exception('Tipos inválidos')

    def enterIntegerLit(self, ctx:Java8Parser.IntegerLitContext):
        ctx.tipo = 'I'

    def exitTimesmultiplicativeExpression(self, ctx:Java8Parser.TimesmultiplicativeExpressionContext):
        if ctx.multiplicativeExpression().tipo == ctx.unaryExpression().tipo:
            ctx.tipo = ctx.additiveExpression().tipo
        else:
            raise Exception('Tipos inválidos')

def main(argv):
    parser = Java8Parser(CommonTokenStream(Java8Lexer(FileStream("prueba2.txt"))))
    tree = parser.compilationUnit()
    #declarations = DeclareListener()

    walker = ParseTreeWalker()
    walker.walk(ClassNameListener(), tree)

    #typecheck = TypecheckListener(declarations.getTypes())
    #walker.walk(typecheck, tree)


if __name__ == '__main__':
    main(sys.argv)
