
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype
    
    def __str__(self):
        return 'MType['+','.join(str(i) for i in self.partype)+'],'+str(self.rettype)

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol('+self.name+','+str(self.mtype)+')'

class StaticChecker(BaseVisitor,Utils):

    global_envi = [Symbol("getInt",MType([],IntType())),
                   Symbol("putIntLn",MType([IntType()],VoidType()))]


    def __init__(self,ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self,ast,c):
        glb = c.copy()
        return [self.visit(x,glb) for x in ast.decl]

    def visitFuncDecl(self,ast,c):
        y = Symbol(ast.name.name,MType([x.varType for x in ast.param],ast.returnType))
        r = self.lookup(y.name,c,lambda z:z.name)
        if r == None:
            c.append(y)
        elif r.mtype == VoidType:
            raise Redeclared(Procedure(),r.name)
        elif r.mtype == MType:
            raise Redeclared(Function(),r.name)
        else:
            raise Redeclared(Variable(),r.name)


    # def visitCallStmt(self,ast,c):
        # at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        # res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        # if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            # raise Undeclared(Procedure(),ast.method.name)
        # elif len(res.mtype.partype) != len(at):
            # raise TypeMismatchInStatement(ast)
        # else:
            # return res.mtype.rettype

    # def visitIntLiteral(self,ast,c):
        # return IntType()

    def visitVarDecl(self,ast,c):
        r = self.lookup(ast.variable.name,c,lambda x:x.name)
        if r == None:
            c.append(Symbol(ast.variable.name,ast.varType))
        elif r.mtype == VoidType:
            raise Redeclared(Procedure(),r.name)
        elif r.mtype == MType:
            raise Redeclared(Function(),r.name)
        else:
            raise Redeclared(Variable(),r.name)
            
        return c[-1]