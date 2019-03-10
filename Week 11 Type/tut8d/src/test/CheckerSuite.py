import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *

class CheckerSuite(unittest.TestCase):
	def test_undeclared_function(self):
		"""Simple program: int main() {} """
		input = """var x: integer; procedure main(); begin x:=1;end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,400))

	# def test_diff_numofparam_stmt(self):
		# """More complex program"""
		# input = """procedure main (); begin
			# putIntLn();
		# end"""
		# expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
		# self.assertTrue(TestChecker.test(input,expect,401))

	# def test_undeclared_function_use_ast(self):
		# """Simple program: int main() {} """
		# input = Program([FuncDecl(Id("main"),[],[],[
			# CallStmt(Id("foo"),[])])])
		# expect = "Undeclared Procedure: foo"
		# self.assertTrue(TestChecker.test(input,expect,402))

	# def test_diff_numofparam_expr_use_ast(self):
		# """More complex program"""
		# input = Program([
				# FuncDecl(Id("main"),[],[],[
					# CallStmt(Id("putIntLn"),[])])])
						
		# expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
		# self.assertTrue(TestChecker.test(input,expect,403))

	# def test_redecl1(self):
		# """Simple program: int main() {} """
		# input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('a'),IntType())])
		# expect = 'Redeclared Variable: a'
		# self.assertTrue(TestChecker.test(input,expect,402))

	# def test_redecl2(self):
		# """Simple program: int main() {} """
		# input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('main'),IntType()),FuncDecl(Id('main'),[],[],[])])
		# expect = 'Redeclared Procedure: main'
		# self.assertTrue(TestChecker.test(input,expect,403))

	# def test_redecl2(self):
		# """Simple program: int main() {} """
		# input = """"""
		# expect = 'Redeclared Procedure: main'
		# self.assertTrue(TestChecker.test(input,expect,403))