from antlr4 import *
from antlr.SmallLexer import SmallLexer
from antlr.SmallParser import SmallParser
from antlr.SmallListener import SmallListener
import sys


# Listener para ver las declaraciones hola
class DeclareListener(SmallListener):
    def __init__(self):
        self.variables = {}
        self.functions = {}

    # Variables
    def enterVarDecl(self, ctx: SmallParser.VarDeclContext):
        var_type = ctx.type_().getText()
        for ident in ctx.ident_list().ident():
            var_name = ident.ID().getText()
            self.getVariables()[var_name] = var_type

    def getVariables(self):
        return self.variables

    # Funciones
    def enterFunction_decl(self, ctx: SmallParser.Function_declContext):
        func_name = ctx.ID().getText()
        return_type = ctx.type_().getText()
        params = [(param.type_().getText(), param.ID().getText()) for param in ctx.params().param()] if ctx.params() \
            else []
        self.functions[func_name] = (return_type, params)

    def getFunctions(self):
        return self.functions


# Listener para checar el tipo de dato
class TypecheckListener(SmallListener):
    def __init__(self, variables, functions):
        self.variables = variables
        self.functions = functions
        self.errors = []
        self.types = {}

    # Declaración de variables
    def enterAssign(self, ctx: SmallParser.AssignContext):
        var_name = ctx.expr(0).getText()
        if var_name not in self.variables:
            self.errors.append(f"Error: Variable '{var_name}' no declarada.")

    def enterVarInitStmt(self, ctx: SmallParser.VarInitStmtContext):
        var_name = ctx.ID().getText()
        var_type = ctx.type().getText()
        self.funTipo = ctx.type_().getText()
        if var_type != self.funTipo:
            self.errors.append(f"Error: Asignación de tipo incorrecto a la variable '{var_name}")

    # Declaración de funciones
    def enterFunctionCall(self, ctx: SmallParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        if func_name not in self.functions:
            self.errors.append(f"Error: Función '{func_name}' no declarada.")

    # Tipos de dato
    def exitInt(self, ctx: SmallParser.IntContext):
        self.types[ctx] = 'int'

    def exitFloat(self, ctx: SmallParser.FloatContext):
        self.types[ctx] = 'float'

    def exitString(self, ctx: SmallParser.StringContext):
        self.types[ctx] = 'string'

    def exitTrue(self, ctx: SmallParser.TrueContext):
        self.types[ctx] = 'boolean'

    def exitFalse(self, ctx: SmallParser.FalseContext):
        self.types[ctx] = 'boolean'

    # Tipos de dato en return
    def exitReturn(self, ctx: SmallParser.ReturnContext):
        tipo = self.types[ctx.expr()]
        if tipo != self.funTipo:
            raise Exception("Tipos incompatibles")

    # Tipos de dato en funciones
    def enterFunction_decl(self, ctx: SmallParser.Function_declContext):
        self.funTipo = ctx.type_().getText()

    # Tipos de dato en operaciones básicas
    def exitAdd(self, ctx: SmallParser.AddContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")

    def exitSub(self, ctx: SmallParser.AddContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")

    def exitMult(self, ctx: SmallParser.AddContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")

    def exitDiv(self, ctx: SmallParser.AddContext):
        left = self.types[ctx.expr(0)]
        right = self.types[ctx.expr(1)]

        if left == right:
            self.types[ctx] = left
        else:
            raise Exception("Tipos incompatibles")

    def getErrors(self):
        return self.errors



def main(argv):
    parser = SmallParser(CommonTokenStream(SmallLexer(FileStream("ejemplo3.txt"))))
    tree = parser.program()

    declarations = DeclareListener()
    walker = ParseTreeWalker()
    walker.walk(declarations, tree)

    typecheck = TypecheckListener(declarations.getVariables(), declarations.getFunctions())
    walker.walk(typecheck, tree)

    errors = typecheck.getErrors()
    if errors:
        for error in errors:
            print(error)
    else:
        print("No se encontraron errores semánticos.")


if __name__ == '__main__':
    main(sys.argv)
