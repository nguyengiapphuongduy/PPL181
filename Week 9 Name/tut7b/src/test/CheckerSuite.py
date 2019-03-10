import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *

class CheckerSuite(unittest.TestCase):
    # def test_undeclared_function(self):
        # """Simple program: int main() {} """
        # input = """procedure main(); begin foo();end"""
        # expect = "Undeclared Procedure: foo"
        # self.assertTrue(TestChecker.test(input,expect,400))

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

    def test_noerr(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id('a'),IntType())])
        expect = [Symbol('a',IntType())]
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_noerr1(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id('a'),IntType()),FuncDecl(Id('main'),[],[],[])])
        expect = [Symbol('a',IntType()),Symbol('main',MType([],VoidType()))]
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_noerr1(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id('a'),IntType()),VarDecl(Id('a'),IntType())])
        expect = 'Redeclared Variable: a'
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_noerr2(self):
        """Simple program: int main() {} """
        input = Program([FuncDecl(Id('foo'),[],[],[]),FuncDecl(Id('foo'),[],[],[])])
        expect = 'Redeclared Procedure: foo'
        self.assertTrue(TestChecker.test(input,expect,406))
