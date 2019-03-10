# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#decl.
    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDeclare.
    def visitVarDeclare(self, ctx:MPParser.VarDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varDeclareOne.
    def visitVarDeclareOne(self, ctx:MPParser.VarDeclareOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idlist.
    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcDeclare.
    def visitFuncDeclare(self, ctx:MPParser.FuncDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procDeclare.
    def visitProcDeclare(self, ctx:MPParser.ProcDeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expr.
    def visitExpr(self, ctx:MPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexExpr.
    def visitIndexExpr(self, ctx:MPParser.IndexExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#invoke.
    def visitInvoke(self, ctx:MPParser.InvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expList.
    def visitExpList(self, ctx:MPParser.ExpListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compStmt.
    def visitCompStmt(self, ctx:MPParser.CompStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listOfStmt.
    def visitListOfStmt(self, ctx:MPParser.ListOfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifStmt.
    def visitIfStmt(self, ctx:MPParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whileStmt.
    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forStmt.
    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakStmt.
    def visitBreakStmt(self, ctx:MPParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#contStmt.
    def visitContStmt(self, ctx:MPParser.ContStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#retStmt.
    def visitRetStmt(self, ctx:MPParser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withStmt.
    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callStmt.
    def visitCallStmt(self, ctx:MPParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#mptype.
    def visitMptype(self, ctx:MPParser.MptypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#primtype.
    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraytype.
    def visitArraytype(self, ctx:MPParser.ArraytypeContext):
        return self.visitChildren(ctx)



del MPParser