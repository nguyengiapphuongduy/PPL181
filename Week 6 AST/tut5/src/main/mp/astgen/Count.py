from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class Count(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return 2 + sum([self.visit(x) for x in ctx.decl()])

    def visitDecl(self,ctx:MPParser.DeclContext):
        return 1 + self.visit(ctx.getChild(0))
    
    def visitFuncdecl(self,ctx:MPParser.FuncdeclContext):
        return 7 + self.visit(ctx.mtype()) + self.visit(ctx.body())

    def visitProcdecl(self,ctx:MPParser.ProcdeclContext):
        return 6 + self.visit(ctx.body())

    def visitBody(self,ctx:MPParser.BodyContext):
        return 3 + sum([self.visit(x) for x in ctx.stmt()]) #(self.visit(ctx.stmt()) if ctx.stmt() else 0)
  
    def visitStmt(self,ctx:MPParser.StmtContext):
        return 2 + self.visit(ctx.funcall())

    def visitFuncall(self,ctx:MPParser.FuncallContext):
        return 4 + (self.visit(ctx.exp()) if ctx.exp() else 0)

    def visitExp(self,ctx:MPParser.ExpContext):
        return 2

    def visitMtype(self,ctx:MPParser.MtypeContext):
        return 2