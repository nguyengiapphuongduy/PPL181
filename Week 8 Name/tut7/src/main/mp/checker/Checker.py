from AST import *
from Visitor import *

class Checker(BaseVisitor):
    def visitProgram(self, ast):
        return list(filter(lambda x: isinstance(x,type(VarDecl('a',IntType(1))))),ast)