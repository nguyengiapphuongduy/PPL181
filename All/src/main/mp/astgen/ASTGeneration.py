from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

def flatten(lst):
    ret = []
    for x in lst:
        ret += flatten(x) if isinstance(x,list) else [x]
    return ret

def tobool(str):
    return str.capitalize() == 'True'

class ASTGeneration(MPVisitor):
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return Program(flatten([self.visit(x) for x in ctx.decl()]))

    def visitDecl(self, ctx:MPParser.DeclContext):
        return self.visit(ctx.getChild(0))

    def visitVarDeclare(self, ctx:MPParser.VarDeclareContext):
        return flatten([self.visit(x) for x in ctx.varDeclareOne()])

    def visitVarDeclareOne(self, ctx:MPParser.VarDeclareOneContext):
        return [VarDecl(x, self.visit(ctx.mptype())) for x in self.visit(ctx.idlist())]

    def visitIdlist(self, ctx:MPParser.IdlistContext):
        return [Id(x.getText()) for x in ctx.ID()]

    def visitMptype(self, ctx:MPParser.MptypeContext):
        return self.visit(ctx.getChild(0))

    def visitPrimtype(self, ctx:MPParser.PrimtypeContext):
        if ctx.INTEGER(): return IntType()
        elif ctx.REAL(): return FloatType()
        elif ctx.BOOLEAN(): return BoolType()
        else: return StringType()

    ####arraytype: ARRAY LSB MINUS? INTLIT DOTDOT MINUS? INTLIT RSB OF primtype;
    def visitArraytype(self, ctx:MPParser.ArraytypeContext):
        if len(ctx.MINUS()) == 1:
            if ctx.getChild(2).getText() == '-':
                lower = -int(ctx.INTLIT(0).getText())
                upper = int(ctx.INTLIT(1).getText())
            else:
                lower = int(ctx.INTLIT(0).getText())
                upper = -int(ctx.INTLIT(1).getText())
        elif len(ctx.MINUS()) == 2:
            lower = -int(ctx.INTLIT(0).getText())
            upper = -int(ctx.INTLIT(1).getText())
        else:
            lower = int(ctx.INTLIT(0).getText())
            upper = int(ctx.INTLIT(1).getText())
        return ArrayType(lower, upper, self.visit(ctx.primtype()))

    def visitFuncDeclare(self, ctx:MPParser.FuncDeclareContext):
        name = Id(ctx.ID().getText())
        param = flatten([self.visit(x) for x in ctx.varDeclareOne()])
        local = flatten([self.visit(x) for x in ctx.varDeclare()])
        body = self.visit(ctx.compStmt())
        returnType = self.visit(ctx.mptype())
        return [FuncDecl(name, param, local, body, returnType)]

    def visitProcDeclare(self, ctx:MPParser.ProcDeclareContext):
        name = Id(ctx.ID().getText())
        param = flatten([self.visit(x) for x in ctx.varDeclareOne()])
        local = flatten([self.visit(x) for x in ctx.varDeclare()])
        body = self.visit(ctx.compStmt())
        return [FuncDecl(name, param, local, body)]

    def visitCompStmt(self, ctx:MPParser.CompStmtContext):
        return self.visit(ctx.listOfStmt())

    def visitListOfStmt(self, ctx:MPParser.ListOfStmtContext):
        return flatten([self.visit(x) for x in ctx.statement()])

    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # assignment: (lhs ':=')+ expr SEMI;
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        # loop from (size - 4) to 0 with step == -2
        return [Assign(self.visit(ctx.getChild(x)), self.visit(ctx.getChild(x + 2))) for x in range(ctx.getChildCount() - 4, -1, -2)]

    def visitLhs(self, ctx:MPParser.LhsContext):
        return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.indexExpr())

    def visitIfStmt(self, ctx:MPParser.IfStmtContext):
        if ctx.ELSE():
            return If(self.visit(ctx.expr()), flatten([self.visit(ctx.statement(0))]), flatten([self.visit(ctx.statement(1))]))
        else:
            return If(self.visit(ctx.expr()), flatten([self.visit(ctx.statement(0))]))

    def visitWhileStmt(self, ctx:MPParser.WhileStmtContext):
        return While(self.visit(ctx.expr()), flatten([self.visit(ctx.statement())]))

    def visitForStmt(self, ctx:MPParser.ForStmtContext):
        return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), (True if ctx.TO() else False), flatten([self.visit(ctx.statement())]))

    def visitBreakStmt(self, ctx:MPParser.BreakStmtContext):
        return Break()

    def visitContStmt(self, ctx:MPParser.ContStmtContext):
        return Continue()

    def visitRetStmt(self, ctx:MPParser.RetStmtContext):
        return (Return(self.visit(ctx.expr())) if ctx.expr() else Return())

    def visitWithStmt(self, ctx:MPParser.WithStmtContext):
        return With(flatten([self.visit(x) for x in ctx.varDeclareOne()]), flatten([self.visit(ctx.statement())]))

    def visitCallStmt(self, ctx:MPParser.WithStmtContext):
        return CallStmt(Id(ctx.ID().getText()), self.visit(ctx.expList()))

    def visitExpr(self, ctx:MPParser.ExprContext):
        if ctx.AND():
            return BinaryOp("andthen", self.visit(ctx.expr()), self.visit(ctx.exp1()))
        elif ctx.OR():
            return BinaryOp("orelse", self.visit(ctx.expr()), self.visit(ctx.exp1()))
        else:
            return self.visit(ctx.exp1())

    def visitExp1(self, ctx:MPParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExp2(self, ctx:MPParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExp3(self, ctx:MPParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitExp4(self, ctx:MPParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.exp4()))

    def visitExp5(self, ctx:MPParser.Exp5Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expr())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.invoke():
            return self.visit(ctx.invoke())
        elif ctx.indexExpr():
            return self.visit(ctx.indexExpr())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.REALLIT():
            return FloatLiteral(float(ctx.REALLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(tobool(ctx.BOOLLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())

    def visitIndexExpr(self, ctx:MPParser.IndexExprContext):
        if ctx.getChildCount() == 6:
            return ArrayCell(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        elif ctx.ID():
            return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.expr(0)))
        elif ctx.invoke():
            return ArrayCell(self.visit(ctx.invoke()), self.visit(ctx.expr(0)))
        elif ctx.indexExpr():
            return ArrayCell(self.visit(ctx.indexExpr()), self.visit(ctx.expr(0)))
        elif ctx.INTLIT():
            return ArrayCell(IntLiteral(int(ctx.INTLIT().getText())), self.visit(ctx.expr(0)))
        elif ctx.REALLIT():
            return ArrayCell(FloatLiteral(float(ctx.REALLIT().getText())), self.visit(ctx.expr(0)))
        elif ctx.BOOLLIT():
            return ArrayCell(BooleanLiteral(tobool(ctx.BOOLLIT().getText())), self.visit(ctx.expr(0)))
        elif ctx.STRINGLIT():
            return ArrayCell(StringLiteral(ctx.STRINGLIT().getText()), self.visit(ctx.expr(0)))

    def visitInvoke(self, ctx:MPParser.InvokeContext):
        return CallExpr(Id(ctx.ID().getText()), self.visit(ctx.expList()))

    def visitExpList(self, ctx:MPParser.ExpListContext):
        return flatten([self.visit(x) for x in ctx.expr()])
