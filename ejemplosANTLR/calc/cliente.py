from antlr4 import *
from antlr.ExprLexer import ExprLexer
from antlr.ExprParser  import ExprParser
from antlr.ExprListener import ExprListener
import sys

r = []
def cast(x): return lambda: int(x)
def mult(x, y): return lambda: x()*y()
def div(x, y): return lambda: x()/y()
def add(x, y): return lambda: x()+y()
def sub(x, y): return lambda: x()-y()

class Compiler(ExprListener):
    def exitMult(self, ctx):         
        r.append(mult(r.pop(), r.pop()))

    def exitAdd(self, ctx):         
        r.append(add(r.pop(), r.pop()))

    def exitDiv(self, ctx):
        y = r.pop()
        x = r.pop()
        r.append(div(x, y))

    def exitSub(self, ctx):         
        y = r.pop()
        x = r.pop()
        r.append(sub(x, y))

    def exitInt(self, ctx):
        r.append(cast(ctx.INT().getText()))

class Interpreter(ExprListener):
    def __init__(self):
        self.stack = []

    def exitMult(self, ctx):
        self.stack.append(self.stack.pop() * self.stack.pop())

    def exitAdd(self, ctx):
        self.stack.append(self.stack.pop() + self.stack.pop())

    def exitDiv(self, ctx):
        y = self.stack.pop()
        x = self.stack.pop()
        self.stack.append(x / y)

    def exitSub(self, ctx):
        y = self.stack.pop()
        x = self.stack.pop()
        self.stack.append(x - y)

    def exitInt(self, ctx):
        self.stack.append(int(ctx.INT().getText()))

def main(argv):
    input = FileStream(argv)
    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)

    tree = parser.prog()
    compiler = Compiler()
    interpreter = Interpreter()

    walker = ParseTreeWalker()

    print("Compilador: ")
    walker.walk(compiler, tree)
    print (r[0])
    print (r[0]())

    print("Intérprete: ")

    walker.walk(interpreter, tree)
    print(interpreter.stack.pop())

if __name__ == '__main__':
    main("ejemplo.txt")
