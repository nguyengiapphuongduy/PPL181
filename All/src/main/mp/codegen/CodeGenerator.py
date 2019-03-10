'''
 *	 @author Nguyen Hua Phung
 *	 @version 1.0
 *	 23/10/2015
 *	 This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
	def __init__(self):
		self.libName = "io"

	def init(self):
		return [Symbol("getInt", MType([],IntType()), CName(self.libName)),
				Symbol("putInt", MType([IntType()],VoidType()), CName(self.libName)),
				Symbol("putIntLn", MType([IntType()],VoidType()), CName(self.libName)),
				Symbol("getFloat", MType([],FloatType()), CName(self.libName)),
				Symbol("putFloat", MType([FloatType()],VoidType()), CName(self.libName)),
				Symbol("putFloatLn", MType([FloatType()],VoidType()), CName(self.libName)),
				Symbol("putBool", MType([BoolType()],VoidType()), CName(self.libName)),
				Symbol("putBoolLn", MType([BoolType()],VoidType()), CName(self.libName)),
				Symbol("putString", MType([StringType()],VoidType()), CName(self.libName)),
				Symbol("putStringLn", MType([StringType()],VoidType()), CName(self.libName)),
				Symbol("putLn", MType([],VoidType()), CName(self.libName))]

	def gen(self, ast, dir_):
		#ast: AST
		#dir_: String
		gl = self.init()
		gc = CodeGenVisitor(ast, gl, dir_)
		gc.visit(ast, None)

class ArrayPointerType(Type):
	def __init__(self, ctype):
		#cname: String
		self.eleType = ctype

	def __str__(self):
		return "ArrayPointerType({0})".format(str(self.eleType))

	def accept(self, v, param):
		return None

class ClassType(Type):
	def __init__(self,cname):
		self.cname = cname

	def __str__(self):
		return "Class({0})".format(str(self.cname))

	def accept(self, v, param):
		return None
		
class SubBody():
	def __init__(self, frame, sym):
		#frame: Frame
		#sym: List[Symbol]
		self.frame = frame
		self.sym = sym

class Access():
	def __init__(self, frame, sym, isLeft, isFirst):
		#frame: Frame
		#sym: List[Symbol]
		#isLeft: Boolean
		#isFirst: Boolean
		self.frame = frame
		self.sym = sym
		self.isLeft = isLeft
		self.isFirst = isFirst

class Val(ABC):
	pass

class Index(Val):
	def __init__(self, value):
		#value: Int
		self.value = value

class CName(Val):
	def __init__(self, value):
		#value: String
		self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
	def __init__(self, astTree, env, dir_):
		#astTree: AST
		#env: List[Symbol]
		#dir_: File
		self.astTree = astTree
		self.env = env
		self.className = "MPClass"
		self.path = dir_
		self.emit = Emitter(self.path + "/" + self.className + ".j")

	def visitProgram(self, ast, ctxt):
		self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
		global_env = SubBody(None, self.env)
		functions = list(filter(lambda y: not type(y) is VarDecl, ast.decl))
		if len(functions) < len(ast.decl): self.emit.printout("\n")
		# static fields
		for x in ast.decl: global_env = self.visit(x, global_env)
		# default constructor
		self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(), None), ctxt, Frame("<init>", VoidType))
		# generate code for functions
		for x in functions: self.visit(x, SubBody("", global_env.sym))
		self.emit.emitEPILOG()
		return ctxt

	def visitVarDecl(self, ast, ctxt):
		frame = ctxt.frame
		if frame is None:
			self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, ast.varType, False, ""))
			return SubBody(frame, [Symbol(ast.variable.name, ast.varType, CName(self.className))] + ctxt.sym)
		else:
			value = frame.getNewIndex()
			self.emit.printout(self.emit.emitVAR(value, ast.variable.name, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
			return SubBody(frame, [Symbol(ast.variable.name, ast.varType, value)] + ctxt.sym)

	def visitFuncDecl(self, ast, ctxt):
		if ctxt.frame is None:
			return SubBody(None, [Symbol(ast.name.name, MType([x.varType for x in ast.param], ast.returnType), CName(self.className))] + ctxt.sym)
		else:
			self.genMETHOD(ast, ctxt.sym, Frame(ast.name, ast.returnType))

	def genMETHOD(self, ast, global_env, frame):
		#ast: FuncDecl
		isInit = ast.returnType is None
		isMain = ast.name.name.lower() == "main" and len(ast.param) == 0 and type(ast.returnType) is VoidType
		returnType = VoidType() if isInit else ast.returnType
		methodName = "<init>" if isInit else ast.name.name
		# main function uses java syntax
		intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in ast.param]
		mtype = MType(intype, returnType)
		self.emit.printout(self.emit.emitMETHOD("main" if isMain else methodName, mtype, not isInit, frame))
		frame.enterScope(True)

		# special methods
		if isInit:
			self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
			self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
			self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
		if isMain:
			self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))

		# Generate code for parameter declarations
		curr_env = SubBody(frame, global_env)
		for x in ast.param + ast.local: curr_env = self.visit(x, curr_env)
		# Visit body and generate code for statements
		self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
		for x in ast.body: self.visit(x, SubBody(frame, curr_env.sym))
		self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
		# handle the last areturn/ireturn/freturn
		if not type(returnType) is VoidType:
			frame.push()
			retcode = self.emit.emitRETURN(returnType, frame)
			self.emit.reversedremove(retcode)
		else:
			retcode = self.emit.emitRETURN(returnType, frame)
		self.emit.printout(retcode)
		# .end method
		self.emit.printout(self.emit.emitENDMETHOD(frame))
		frame.exitScope();

	def visitId(self, ast, ctxt):
		r = self.getSymbol(ast.name, ctxt.sym)
		frame = ctxt.frame
		if type(r.value) is CName: # static (global)
			if ctxt.isLeft:
				return self.emit.emitPUTSTATIC(r.value.value + '/' + r.name, r.mtype, frame), r.mtype
			else:
				return self.emit.emitGETSTATIC(r.value.value + '/' + r.name, r.mtype, frame), r.mtype
		else: # local
			if ctxt.isLeft:
				return self.emit.emitWRITEVAR(r.name, r.mtype, r.value, frame), r.mtype
			else:
				return self.emit.emitREADVAR(r.name, r.mtype, r.value, frame), r.mtype

	################################################################
	## Statements
	################################################################

	def visitAssign(self, ast, ctxt):
		exp_code, exp_type = self.visit(ast.exp, Access(ctxt.frame, ctxt.sym, False, True))
		lhs_code, lhs_type = self.visit(ast.lhs, Access(ctxt.frame, ctxt.sym, True, True))
		if type(exp_type) is IntType and type(lhs_type) is FloatType:
			exp_code += self.emit.emitI2F(ctxt.frame)
			exp_type = FloatType()
		self.emit.printout(exp_code + lhs_code)

	def visitCall(self, ast, ctxt):
		frame = ctxt.frame
		r = self.getSymbol(ast.method.name, ctxt.sym)
		out_ = ""
		for x in zip(ast.param, r.mtype.partype):
			xstr, xtype = self.visit(x[0], Access(frame, ctxt.sym, False, True))
			if type(xtype) is IntType and type(x[1]) is FloatType:
				xstr += self.emit.emitI2F(frame)
				xtype = FloatType()
			out_ += xstr
		out_ += self.emit.emitINVOKESTATIC(r.value.value + "/" + r.name, r.mtype, frame)
		return out_, r.mtype.rettype

	def visitCallStmt(self, ast, ctxt):
		self.emit.printout(self.visitCall(ast, ctxt)[0])

	def visitReturn(self, ast, ctxt):
		frame = ctxt.frame
		if not ast.expr is None:
			code, typ = self.visit(ast.expr, Access(frame, ctxt.sym, False, True))
			if type(typ) is IntType and type(frame.returnType) is FloatType:
				code += self.emit.emitI2F(frame)
				typ = FloatType()
			self.emit.printout(code)
		else:
			typ = VoidType()
		self.emit.printout(self.emit.emitRETURN(typ, frame))

	def visitWith(self, ast, ctxt):
		frame = ctxt.frame
		frame.enterScope(False)
		# with scope declarations
		curr_env = SubBody(ctxt.frame, ctxt.sym)
		for x in ast.decl: curr_env = self.visit(x, curr_env)
		# statements
		self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
		for x in ast.stmt: self.visit(x, curr_env)
		self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
		frame.exitScope()

	def visitIf(self, ast, ctxt):
		frame = ctxt.frame
		if len(ast.elseStmt) > 0:
			labelFalse = frame.getNewLabel()
			labelOut = frame.getNewLabel()
			# visit if expression
			exp_code = self.visit(ast.expr, Access(frame, ctxt.sym, False, True))[0]
			self.emit.printout(exp_code + self.emit.emitIFFALSE(labelFalse, frame))
			# visit true statements
			for x in ast.thenStmt: self.visit(x, ctxt)
			self.emit.printout(self.emit.emitGOTO(labelOut, frame))
			# visit false statements
			self.emit.printout(self.emit.emitLABEL(labelFalse, frame))
			for x in ast.elseStmt: self.visit(x, ctxt)
		else:
			labelOut = frame.getNewLabel()
			# visit if expression
			exp_code = self.visit(ast.expr, Access(frame, ctxt.sym, False, True))[0]
			self.emit.printout(exp_code + self.emit.emitIFFALSE(labelOut, frame))
			# visit true statements
			for x in ast.thenStmt: self.visit(x, ctxt)
		# labelOut
		self.emit.printout(self.emit.emitLABEL(labelOut, frame))

	def visitFor(self, ast, ctxt):
		frame = ctxt.frame
		frame.enterLoop()
		labelIn = frame.getNewLabel()
		labelContinue = frame.getContinueLabel()
		labelBreak = frame.getBreakLabel()
		# store first to i
		self.visit(Assign(ast.id, ast.expr1), ctxt)
		self.emit.printout(self.emit.emitLABEL(labelIn, frame))
		# compare i with expr2 to gen jump code
		rcode = self.visit(ast.id, Access(ctxt.frame, ctxt.sym, False, True))[0]
		expr2 = self.visit(ast.expr2, Access(ctxt.frame, ctxt.sym, False, True))[0]
		jumpcode = self.emit.emitIFICMPGT(labelBreak, frame) if ast.up else self.emit.emitIFICMPLT(labelBreak, frame)
		self.emit.printout(rcode + expr2 + jumpcode)
		# loop body
		for x in ast.loop: self.visit(x, ctxt)
		# continue label (i:=i+1)
		self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
		self.visit(Assign(ast.id, BinaryOp('+' if ast.up else '-', ast.id, IntLiteral(1))), ctxt)
		# goto loop and break label
		self.emit.printout(self.emit.emitGOTO(labelIn,frame) + self.emit.emitLABEL(labelBreak, frame))
		frame.exitLoop()

	def visitWhile(self, ast, ctxt):
		frame = ctxt.frame
		frame.enterLoop()
		labelContinue = frame.getContinueLabel()
		labelBreak = frame.getBreakLabel()
		# labelContinue and expression
		self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
		exp_code = self.visit(ast.exp, Access(frame, ctxt.sym, False, True))[0]
		self.emit.printout(exp_code + self.emit.emitIFFALSE(labelBreak, frame))
		# statements
		for x in ast.sl: self.visit(x, ctxt)
		self.emit.printout(self.emit.emitGOTO(labelContinue, frame))
		# labelBreak
		self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
		frame.exitLoop()

	def visitBreak(self, ast, ctxt):
		self.emit.printout(self.emit.emitGOTO(ctxt.frame.getBreakLabel(),ctxt.frame))

	def visitContinue(self, ast, ctxt):
		self.emit.printout(self.emit.emitGOTO(ctxt.frame.getContinueLabel(),ctxt.frame))

	################################################################
	## Expressions
	################################################################

	def visitCallExpr(self, ast, ctxt):
		return self.visitCall(ast, ctxt)

	def visitIntLiteral(self, ast, ctxt):
		frame = ctxt.frame
		return self.emit.emitPUSHICONST(ast.value, frame), IntType()

	def visitFloatLiteral(self, ast, ctxt):
		frame = ctxt.frame
		return self.emit.emitPUSHFCONST(str(float(ast.value)), frame), FloatType()

	def visitBooleanLiteral(self, ast, ctxt):
		frame = ctxt.frame
		return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()

	def visitStringLiteral(self, ast, ctxt):
		frame = ctxt.frame
		return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()

	def visitBinaryOp(self, ast, ctxt):
		frame = ctxt.frame
		lcode, ltype = self.visit(ast.left, ctxt)
		rcode, rtype = self.visit(ast.right, ctxt)
		if FloatType in (type(ltype), type(rtype)) or ast.op == '/':
			if type(ltype) is IntType:
				lcode += self.emit.emitI2F(frame)
				ltype = FloatType()
			if type(rtype) is IntType:
				rcode += self.emit.emitI2F(frame)
				rtype = FloatType()

		if ast.op in ('+', '-'):
			return lcode + rcode + self.emit.emitADDOP(ast.op, ltype, frame), ltype
		elif ast.op in ('*', '/'):
			return lcode + rcode + self.emit.emitMULOP(ast.op, ltype, frame), ltype
		elif ast.op.lower() == 'div':
			return lcode + rcode + self.emit.emitDIV(frame), IntType()
		elif ast.op.lower() == 'mod':
			return lcode + rcode + self.emit.emitMOD(frame), IntType()
		elif ast.op.lower() == 'and':
			return lcode + rcode + self.emit.emitANDOP(frame), BoolType()
		elif ast.op.lower() == 'or':
			return lcode + rcode + self.emit.emitOROP(frame), BoolType()
		elif ast.op.lower() in ('>', '>=', '<', '<=', '<>', '='):
			return lcode + rcode + self.emit.emitREOP(ast.op, ltype, frame), BoolType()
		elif ast.op in ('andthen', 'orelse'):
			return self.genShortCircuit(ast.op, lcode, rcode, frame)
		else:
			return

	def genShortCircuit(self, op, left, right, frame):
		res = ""
		labelBrk = frame.getNewLabel()
		labelOut = frame.getNewLabel()
		if op == 'andthen':
			res += left + self.emit.emitIFFALSE(labelBrk, frame)\
				+ right + self.emit.emitIFFALSE(labelBrk, frame)\
				+ self.emit.emitPUSHCONST("1", IntType(), frame)\
				+ self.emit.emitGOTO(labelOut, frame)\
				+ self.emit.emitLABEL(labelBrk, frame)\
				+ self.emit.emitPUSHCONST("0", IntType(), frame)\
				+ self.emit.emitLABEL(labelOut, frame)
		else:
			res += left + self.emit.emitIFTRUE(labelBrk, frame)\
				+ right + self.emit.emitIFTRUE(labelBrk, frame)\
				+ self.emit.emitPUSHCONST("0", IntType(), frame)\
				+ self.emit.emitGOTO(labelOut, frame)\
				+ self.emit.emitLABEL(labelBrk, frame)\
				+ self.emit.emitPUSHCONST("1", IntType(), frame)\
				+ self.emit.emitLABEL(labelOut, frame)
		return res, BoolType()

	def visitUnaryOp(self, ast, ctxt):
		code, typ = self.visit(ast.body, ctxt)
		if ast.op.lower() == 'not':
			return code + self.emit.emitNOT(ctxt.frame), BoolType()
		else:
			return code + self.emit.emitNEGOP(typ, ctxt.frame), typ

	def getSymbol(self, name, env):
		return self.lookup(name.lower(), env, lambda x: x.name.lower())
################################################################
## End of class CodeGenVisitor
################################################################




# print out frame for debugging
def printframe(frame):
	print("name:" + str(frame.name))
	print("returnType:" + str(frame.returnType))
	print("currLabel:" + str(frame.currentLabel))
	print("opStackSize:" + str(frame.currOpStackSize))
	print("maxOpStackSize:" + str(frame.maxOpStackSize))
	print("currIndex:" + str(frame.currIndex))
	print("maxIndex:" + str(frame.maxIndex))
	print("startLabel:" + str(frame.startLabel))
	print("endLabel:" + str(frame.endLabel))
	print("indexLocal:" + str(frame.indexLocal))
	print("conLabel:" + str(frame.conLabel))
	print("brkLabel:" + str(frame.brkLabel))
	input()

################################################################################################################################