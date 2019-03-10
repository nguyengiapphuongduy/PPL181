from Utils import *
from StaticCheck import *
from StaticError import *
from MachineCode import JasminCode
from CodeGenError import *
import CodeGenerator as cgen

class Emitter():
	def __init__(self, filename):
		self.filename = filename
		self.buff = list()
		self.jvm = JasminCode()

	def getJVMType(self, inType):
		typeIn = type(inType)
		if typeIn is IntType:
			return "I"
		elif typeIn is FloatType:
			return "F"
		elif typeIn is BoolType:
			return "Z"
		elif typeIn is cgen.StringType:
			return "Ljava/lang/String;"
		elif typeIn is VoidType:
			return "V"
		elif typeIn is cgen.ArrayPointerType:
			return "[" + self.getJVMType(inType.eleType)
		elif typeIn is MType:
			return "(" + "".join(list(map(lambda x: self.getJVMType(x), inType.partype))) + ")" + self.getJVMType(inType.rettype)
		elif typeIn is cgen.ClassType:
			return "L" + inType.cname + ";"
		else:
			raise IllegalOperandException(str(inType))

	# def getFullType(inType):
		# typeIn = type(inType)
		# if typeIn is IntType:
			# return "int"
		# elif typeIn is cgen.StringType:
			# return "java/lang/String"
		# elif typeIn is VoidType:
			# return "void"

	def emitPUSHICONST(self, in_, frame):
		#in: Int or Sring
		#frame: Frame
		if type(in_) is int:
			frame.push();
			i = in_
			if i >= -1 and i <=5:
				return self.jvm.emitICONST(i)
			elif i >= -128 and i <= 127:
				return self.jvm.emitBIPUSH(i)
			elif i >= -32768 and i <= 32767:
				return self.jvm.emitSIPUSH(i)
			else:
				return self.jvm.emitLDC(str(i))
		elif type(in_) is str:
			if in_.lower() == "true":
				return self.emitPUSHICONST(1, frame)
			elif in_.lower() == "false":
				return self.emitPUSHICONST(0, frame)
			else:
				return self.emitPUSHICONST(int(in_), frame)

	def emitPUSHFCONST(self, in_, frame):
		#in_: String
		#frame: Frame
		f = float(in_)
		frame.push()
		if f in (0.0, 1.0, 2.0):
			rst = "{0:.1f}".format(f)
			return self.jvm.emitFCONST(rst)
		else:
			return self.jvm.emitLDC(in_)

	# generate code to push a constant onto the operand stack.
	# @param in_: the lexeme (String) of the constant
	# @param typ: the type of the constant
	def emitPUSHCONST(self, in_, typ, frame):
		#in_: String
		#typ: Type
		#frame: Frame
		if type(typ) is IntType:
			return self.emitPUSHICONST(in_, frame)
		elif type(typ) is StringType:
			frame.push()
			return self.jvm.emitLDC('"' + in_ + '"')
		else:
			raise IllegalOperandException(in_)


	################################################################
	#	Unary Operators
	################################################################

	# generate ineg, fneg.
	# @param in_: the type of the operands.
	# ..., value -> ..., result
	def emitNEGOP(self, in_, frame):
		if type(in_) is IntType:
			return self.jvm.emitINEG()
		else:
			return self.jvm.emitFNEG()

	def emitNOT(self, frame):
		label1 = frame.getNewLabel()
		label2 = frame.getNewLabel()
		result = list()
		result.append(self.emitIFTRUE(label1, frame))
		result.append(self.emitPUSHICONST("true", frame))
		result.append(self.emitGOTO(label2, frame))
		result.append(self.emitLABEL(label1, frame))
		result.append(self.emitPUSHICONST("false", frame))
		result.append(self.emitLABEL(label2, frame))
		return ''.join(result)

	################################################################
	## Binary Operators
	################################################################

	# generate iadd, isub, fadd or fsub.
	# @param lexeme: the lexeme (String) of the operator.
	# @param in_: the type of the operands.
	# ..., value1, value2 -> result
	def emitADDOP(self, lexeme, in_, frame):
		frame.pop()
		if lexeme == "+":
			if type(in_) is IntType:
				return self.jvm.emitIADD()
			else:
				return self.jvm.emitFADD()
		else:
			if type(in_) is IntType:
				return self.jvm.emitISUB()
			else:
				return self.jvm.emitFSUB()

	# generate imul, idiv, fmul or fdiv.
	# @param lexeme: the lexeme (String) of the operator.
	# @param in_: the type of the operands.
	# ..., value1, value2 -> result
	def emitMULOP(self, lexeme, in_, frame):
		frame.pop()
		if lexeme == "*":
			if type(in_) is IntType:
				return self.jvm.emitIMUL()
			else:
				return self.jvm.emitFMUL()
		else:
			if type(in_) is IntType:
				return self.jvm.emitIDIV()
			else:
				return self.jvm.emitFDIV()

	def emitDIV(self, frame):
		#frame: Frame
		frame.pop()
		return self.jvm.emitIDIV()

	def emitMOD(self, frame):
		#frame: Frame
		frame.pop()
		return self.jvm.emitIREM()

	def emitANDOP(self, frame):
		#frame: Frame
		frame.pop()
		return self.jvm.emitIAND()

	def emitOROP(self, frame):
		#frame: Frame
		frame.pop()
		return self.jvm.emitIOR()

	def emitREOP(self, op, in_, frame):
		#op: String
		#in_: Type
		#frame: Frame
		#..., value1, value2 -> ..., result
		result = list()
		labelFalse = frame.getNewLabel()
		labelOut = frame.getNewLabel()
		frame.pop()
		frame.pop()

		if type(in_) is IntType:
			if op == ">":
				result.append(self.jvm.emitIFICMPLE(labelFalse))
			elif op == ">=":
				result.append(self.jvm.emitIFICMPLT(labelFalse))
			elif op == "<":
				result.append(self.jvm.emitIFICMPGE(labelFalse))
			elif op == "<=":
				result.append(self.jvm.emitIFICMPGT(labelFalse))
			elif op == "<>":
				result.append(self.jvm.emitIFICMPEQ(labelFalse))
			elif op == "=":
				result.append(self.jvm.emitIFICMPNE(labelFalse))
		else:
			result.append(self.jvm.emitFCMPL())
			if op == ">":
				result.append(self.jvm.emitIFLE(labelFalse))
			elif op == ">=":
				result.append(self.jvm.emitIFLT(labelFalse))
			elif op == "<":
				result.append(self.jvm.emitIFGE(labelFalse))
			elif op == "<=":
				result.append(self.jvm.emitIFGT(labelFalse))
			elif op == "<>":
				result.append(self.jvm.emitIFEQ(labelFalse))
			elif op == "=":
				result.append(self.jvm.emitIFNE(labelFalse))

		result.append(self.emitPUSHCONST("1", IntType(), frame))
		result.append(self.emitGOTO(labelOut, frame))
		result.append(self.emitLABEL(labelFalse, frame))
		result.append(self.emitPUSHCONST("0", IntType(), frame))
		result.append(self.emitLABEL(labelOut, frame))
		frame.pop() # only "1" or "0"

		return ''.join(result)

	# def emitRELOP(self, op, in_, trueLabel, falseLabel, frame):
		# #op: String
		# #in_: Type
		# #trueLabel: Int
		# #falseLabel: Int
		# #frame: Frame
		# #..., value1, value2 -> ..., result
		# result = list()

		# frame.pop()
		# frame.pop()
		# if op == ">":
			# result.append(self.jvm.emitIFICMPLE(falseLabel))
		# elif op == ">=":
			# result.append(self.jvm.emitIFICMPLT(falseLabel))
		# elif op == "<":
			# result.append(self.jvm.emitIFICMPGE(falseLabel))
		# elif op == "<=":
			# result.append(self.jvm.emitIFICMPGT(falseLabel))
		# elif op == "<>":
			# result.append(self.jvm.emitIFICMPEQ(falseLabel))
		# elif op == "=":
			# result.append(self.jvm.emitIFICMPNE(falseLabel))
		# result.append(self.jvm.emitGOTO(trueLabel))
		# return ''.join(result)

	################################################################
	## Labeling and Jumping
	################################################################

	# generate code to jump to label if the value on top of operand stack is true
	# ifgt label
	# @param label: the label (Int) where the execution continues if the value on top of stack is true
	def emitIFTRUE(self, label, frame):
		frame.pop()
		return self.jvm.emitIFGT(label)

	# generate code to jump to label if the value on top of operand stack is false
	# ifle label
	# @param label: the label (Int) where the execution continues if the value on top of stack is false
	def emitIFFALSE(self, label, frame):
		frame.pop()
		return self.jvm.emitIFLE(label)

	# ..., value1, value2 -> ...
	# generate code to jump to label if value1 > value2
	# label: Int
	def emitIFICMPGT(self, label, frame):
		frame.pop()
		frame.pop()
		return self.jvm.emitIFICMPGT(label)

	# ..., value1, value2 -> ...
	# generate code to jump to label if value1 < value2
	# label: Int
	def emitIFICMPLT(self, label, frame):
		frame.pop()
		frame.pop()
		return self.jvm.emitIFICMPLT(label)

	# @return code goto Label<label>
	# @param label: Int
	def emitGOTO(self, label, frame):
		return self.jvm.emitGOTO(str(label))

	# @return code Label<label>
	# @param label: Int
	def emitLABEL(self, label, frame):
		return self.jvm.emitLABEL(label)

	################################################################
	## No Arrays
	################################################################

	# def emitALOAD(self, in_, frame):
		# #in_: Type
		# #frame: Frame
		# #..., arrayref, index, value -> ...
		
		# frame.pop()
		# if type(in_) is IntType:
			# return self.jvm.emitIALOAD()
		# elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
			# return self.jvm.emitAALOAD()
		# else:
			# raise IllegalOperandException(str(in_))

	# def emitASTORE(self, in_, frame):
		# #in_: Type
		# #frame: Frame
		# #..., arrayref, index, value -> ...
		
		# frame.pop()
		# frame.pop()
		# frame.pop()
		# if type(in_) is IntType:
			# return self.jvm.emitIASTORE()
		# elif type(in_) is cgen.ArrayPointerType or type(in_) is cgen.ClassType or type(in_) is StringType:
			# return self.jvm.emitAASTORE()
		# else:
			# raise IllegalOperandException(str(in_))

	################################################################
	## Declarations
	################################################################

	# generate the var directive for a local variable.
	# @param in_: Int the index of the local variable.
	# @param varName: String the name of the local variable.
	# @param inType: Type the type of the local variable.
	# @param fromLabel: Int the starting label of the scope where the variable is active.
	# @param toLabel: Int the ending label of the scope where the variable is active.
	def emitVAR(self, in_, varName, inType, fromLabel, toLabel, frame):
		return self.jvm.emitVAR(in_, varName, self.getJVMType(inType), fromLabel, toLabel)

	# generate the field (static) directive for a class mutable or immutable attribute.
	# @param lexeme: the name of the attribute.
	# @param in_: the type of the attribute.
	# @param isFinal: true in case of constant, false otherwise
	def emitATTRIBUTE(self, lexeme, in_, isFinal, value):
		return self.jvm.emitSTATICFIELD(lexeme, self.getJVMType(in_), False)

	# iload, fload, aload
	# push a value to stack
	def emitREADVAR(self, name, inType, index, frame):
		frame.push()
		if type(inType) in (IntType, BoolType):
			return self.jvm.emitILOAD(index)
		elif type(inType) is FloatType:
			return self.jvm.emitFLOAD(index)
		elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
			return self.jvm.emitALOAD(index)
		else:
			raise IllegalOperandException(name)

	# istore, fstore, astore
	# pop a value from stack
	def emitWRITEVAR(self, name, inType, index, frame):
		frame.pop()
		if type(inType) in (IntType, BoolType):
			return self.jvm.emitISTORE(index)
		elif type(inType) is FloatType:
			return self.jvm.emitFSTORE(index)
		elif type(inType) is cgen.ArrayPointerType or type(inType) is cgen.ClassType or type(inType) is StringType:
			return self.jvm.emitASTORE(index)
		else:
			raise IllegalOperandException(name)

	# getstatic
	# push a value to stack
	def emitGETSTATIC(self, lexeme, in_, frame):
		frame.push()
		return self.jvm.emitGETSTATIC(lexeme, self.getJVMType(in_))

	# putstatic
	# pop a value from stack
	def emitPUTSTATIC(self, lexeme, in_, frame):
		frame.pop()
		return self.jvm.emitPUTSTATIC(lexeme, self.getJVMType(in_))

	# def emitGETFIELD(self, lexeme, in_, frame):
		# frame.push()
		# return self.jvm.emitGETFIELD(lexeme, self.getJVMType(in_))

	# def emitPUTFIELD(self, lexeme, in_, frame):
		# frame.pop()
		# return self.jvm.emitPUTFIELD(lexeme, self.getJVMType(in_))

	################################################################
	## Functions
	################################################################

	# generate code to invoke a static method
	# @param lexeme the qualified name of the method(i.e., class-name/method-name)
	# @param in_ the type descriptor of the method.
	def emitINVOKESTATIC(self, lexeme, in_, frame):
		mtype = in_
		list(map(lambda x: frame.pop(), mtype.partype))
		if not type(mtype.rettype) is VoidType:
			frame.push()
		return self.jvm.emitINVOKESTATIC(lexeme, self.getJVMType(in_))

	# return, ireturn, freturn
	def emitRETURN(self, in_, frame):
		if type(in_) in (IntType, BoolType):
			frame.pop()
			return self.jvm.emitIRETURN()
		elif type(in_) is FloatType:
			frame.pop()
			return self.jvm.emitFRETURN()
		elif type(in_) is StringType:
			frame.pop()
			return self.jvm.emitARETURN()
		elif type(in_) is VoidType:
			return self.jvm.emitRETURN()
		else:
			raise IllegalOperandException(str(in_))

	# remove the last occurrence of "ele" in the list "buff"
	def reversedremove(self, ele):
		if ele in self.buff:
			del self.buff[-self.buff[::-1].index(ele) - 1]

################################################################################################################################

	''' generate code to invoke a special method
	*	@param lexeme the qualified name of the method(i.e., class-name/method-name)
	*	@param in the type descriptor of the method.
	'''
	def emitINVOKESPECIAL(self, frame, lexeme=None, in_=None):
		#lexeme: String
		#in_: Type
		#frame: Frame

		if not lexeme is None and not in_ is None:
			typ = in_
			list(map(lambda x: frame.pop(), typ.partype))
			frame.pop()
			if not type(typ.rettype) is VoidType:
				frame.push()
			return self.jvm.emitINVOKESPECIAL(lexeme, self.getJVMType(in_))
		elif lexeme is None and in_ is None:
			frame.pop()
			return self.jvm.emitINVOKESPECIAL()

	''' generate code to invoke a virtual method
	* @param lexeme the qualified name of the method(i.e., class-name/method-name)
	* @param in the type descriptor of the method.
	'''
	def emitINVOKEVIRTUAL(self, lexeme, in_, frame):
		#lexeme: String
		#in_: Type
		#frame: Frame

		typ = in_
		list(map(lambda x: frame.pop(), typ.partype))
		frame.pop()
		if not type(typ) is VoidType:
			frame.push()
		return self.jvm.emitINVOKEVIRTUAL(lexeme, self.getJVMType(in_))


	'''	  generate the method directive for a function.
	*	@param lexeme the qualified name of the method(i.e., class-name/method-name).
	*	@param in the type descriptor of the method.
	*	@param isStatic <code>true</code> if the method is static; <code>false</code> otherwise.
	'''

	def emitMETHOD(self, lexeme, in_, isStatic, frame):
		#lexeme: String
		#in_: Type
		#isStatic: Boolean
		#frame: Frame

		return self.jvm.emitMETHOD(lexeme, self.getJVMType(in_), isStatic)

	'''	  generate the end directive for a function.
	'''
	def emitENDMETHOD(self, frame):
		#frame: Frame

		buffer = list()
		buffer.append(self.jvm.emitLIMITSTACK(frame.getMaxOpStackSize()))
		buffer.append(self.jvm.emitLIMITLOCAL(frame.getMaxIndex()))
		buffer.append(self.jvm.emitENDMETHOD())
		return ''.join(buffer)

	def getConst(self, ast):
		#ast: Literal
		if type(ast) is IntLiteral:
			return (str(ast.value), IntType())

	'''	  generate code to initialize a local array variable.<p>
	*	@param index the index of the local variable.
	*	@param in the type of the local array variable.
	'''

	'''	  generate code to initialize local array variables.
	*	@param in the list of symbol entries corresponding to local array variable.	   
	'''

	'''	  generate code to duplicate the value on the top of the operand stack.<p>
	*	Stack:<p>
	*	Before: ...,value1<p>
	*	After:	...,value1,value1<p>
	'''
	def emitDUP(self, frame):
		#frame: Frame

		frame.push()
		return self.jvm.emitDUP()

	def emitPOP(self, frame):
		#frame: Frame

		frame.pop()
		return self.jvm.emitPOP()

	'''	  generate code to exchange an integer on top of stack to a floating-point number.
	'''
	def emitI2F(self, frame):
		#frame: Frame

		return self.jvm.emitI2F()

	''' generate some starting directives for a class.<p>
	*	.source MPC.CLASSNAME.java<p>
	*	.class public MPC.CLASSNAME<p>
	*	.super java/lang/Object<p>
	'''
	def emitPROLOG(self, name, parent):
		#name: String
		#parent: String

		result = list()
		result.append(self.jvm.emitSOURCE(name + ".java"))
		result.append(self.jvm.emitCLASS("public " + name))
		result.append(self.jvm.emitSUPER("java/land/Object" if parent == "" else parent))
		return ''.join(result)

	def emitLIMITSTACK(self, num):
		#num: Int
		return self.jvm.emitLIMITSTACK(num)

	def emitLIMITLOCAL(self, num):
		#num: Int
		return self.jvm.emitLIMITLOCAL(num)

	def emitEPILOG(self):
		file = open(self.filename, "w")
		file.write(''.join(self.buff))
		file.close()

	def printout(self, in_):
		self.buff.append(in_)

	def clearBuff(self):
		self.buff.clear()
