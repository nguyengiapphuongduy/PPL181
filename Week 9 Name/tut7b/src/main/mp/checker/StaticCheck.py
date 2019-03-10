
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
        return 'MType(['+','.join(str(i) for i in self.partype)+']'+','+str(self.rettype)

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

    def visitProgram(self,ast, c):
        ls = [self.visit(x,c) for x in ast.decl]
        checklist = []
        for x in ls:
            if x.name in checklist:
                if type(x.mtype) is MType:
                    if type(x.mtype.rettype) is VoidType:
                        raise Redeclared(Procedure(),x.name)
                    else:
                        raise Redeclared(Function(),x.name)    
                else:
                    raise Redeclared(Variable(),x.name)
            else:
                checklist.append(x.name)
        return ls
        # ls = list(filter(lambda x: isinstance(x,VarDecl),[self.visit(x,c) for x in ast.decl]))
        # returnlist = []
        # for x in ls:
            # if x.variable.name is in returnlist:
                # raise Exception()
            # else:
                # returnlist.append(x.variable.name)
                # global_envi.append(Symbol(x.variable.name,x.varType))
        # return global_envi
        
    def visitFuncDecl(self,ast, c):
        return Symbol(ast.name.name,MType([x.variable.varType for x in ast.param],ast.returnType))
        #return list(map(lambda x: self.visit(x,(c,True)),ast.body)) 
    

    def visitCallStmt(self, ast, c): 
        at = [self.visit(x,(c[0],False)) for x in ast.param]
        
        res = self.lookup(ast.method.name,c[0],lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(),ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)            
        else:
            return res.mtype.rettype

    def visitIntLiteral(self,ast, c): 
        return IntType()

    def visitVarDecl(self,ast,c):
        return Symbol(ast.variable.name,ast.varType)
        
