
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

	# return Symbol of the Id in the environment if it is already declared
	def visitId(self,ast,env):
		if type(env) is tuple:
			r = None
			for e in env[::-1]:
				if r is None:
					r = self.lookup(ast.name,e,lambda x: x.name)
		else:
			r = self.lookup(ast.name,env,lambda x: x.name)
		if r is None: raise Undeclared(Identifier(),ast.name)
		else: return r.mtype

	def visitProgram(self,ast,c):
		g = c[:]
		for x in ast.decl:
			self.visit(x,(g,Variable()))
		for x in ast.decl:
			if type(x) is FuncDecl:
				self.visit(x,(g,Function()))
		return None

	def visitVarDecl(self,ast,env):
		res = Symbol(ast.variable.name,ast.varType)
		check = self.lookup(ast.variable.name,env[0],lambda x:x.name)
		if check is None:
			env[0].append(res)
			return res
		else:
			raise Redeclared(env[1],res.name)

	def visitFuncDecl(self,ast,env):
		# local_env = []
		# check = self.visit(ast.name,env[0])
		# param = [self.visit(x,(local_env,Parameter())).mtype for x in ast.param]
		# if check is None:
			# res = Symbol(ast.name.name,MType(param,ast.returnType))
			# env[0].append(res)
			# return res
		# elif type(ast.returnType) is VoidType:
			# raise Redeclared(Procedure(),ast.name.name)
		# else:
			# raise Redeclared(Function(),ast.name.name)
		local_env = []
		check = self.lookup(ast.name.name,env[0],lambda x:x.name)
		param = [self.visit(x,(local_env,Parameter())).mtype for x in ast.param]
		if check is None:
			res = Symbol(ast.name.name,MType(param,ast.returnType))
			env[0].append(res)
			return res
		elif type(env[1]) is Function:
			for x in ast.local:
				self.visit(x,(local_env,Variable()))
			retcheck = []
			for x in ast.body:
				r = self.visit(x,(env[0],local_env))
			return None
		elif type(ast.returnType) is VoidType:
			raise Redeclared(Procedure(),ast.name.name)
		else:
			raise Redeclared(Function(),ast.name.name)

	def visitCall(self,ast,env,kind):
		method = self.visit(ast.method,env)
		if method is None or type(method.mtype) != MType or ((type(method.mtype.rettype) is VoidType) if type(kind) is Function else not (type(method.mtype.rettype) is VoidType)):
			raise Undeclared(kind,ast.method.name)
		def_param = method.mtype.partype
		use_param = [self.visit(x,env) for x in ast.param]
		if len(def_param) != len(use_param):
			raise TypeMismatchInExpression(ast) if type(kind) is Function else TypeMismatchInStatement(ast)
		for i in range(0,len(def_param)):
			if self.typeCheck(def_param[i],use_param[i]) == False:
				raise TypeMismatchInExpression(ast) if type(kind) is Function else TypeMismatchInStatement(ast)
		return method.mtype.rettype

	def visitCallExpr(self,ast,env):
		self.visitCall(ast,env,Function())

	def visitCallStmt(self,ast,env):
		self.visitCall(ast,env,Procedure())

	def typeCheck(self,x,y):
		if type(x) == type(y):
			if type(x) is ArrayType and not (x.lower == y.lower and x.upper == y.upper and type(x.eleType) == type(y.eleType)):
				return False
		else:
			if not (type(x) is FloatType and type(y) is IntType):
				return False
		return True

	# def visitFor(self,ast,env):
		# idcheck = self.visit(ast.id,env[1:])
		# if idcheck is None:
			# raise Undeclared(Identifier(),ast.id.name)
		# elif not type(idcheck.mtype) is IntType:
			# raise TypeMismatchInStatement(ast)
		# e1 = self.visit(ast.expr1,env)
		# if not type(e1) is IntType:
			# raise TypeMismatchInStatement(ast)
		# e2 = self.visit(ast.expr1,env)
		# if not type(e2) is IntType:
			# raise TypeMismatchInStatement(ast)

	def visitIntLiteral(self,ast,env):
		return IntType()

	def visitFloatLiteral(self,ast,env):
		return FloatType()

	def visitBooleanLiteral(self,ast,env):
		return BoolType()

	def visitStringLiteral(self,ast,env):
		return StringType()

	def visitBinaryOp(self,ast,env):
		ltype = type(self.visit(ast.left,env))
		rtype = type(self.visit(ast.right,env))
		
		if (ltype is FloatType and rtype is IntType)\
		or (ltype is IntType and rtype is FloatType)\
		or (ltype is FloatType and rtype is FloatType):
			return FloatType()
		elif ltype is IntType and rtype is IntType:
			return IntType()
		
		raise TypeMismatchInExpression(ast)
