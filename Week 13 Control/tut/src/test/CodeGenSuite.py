import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin putInt(100); end"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_float(self):
        """Test Float"""
        input = """procedure main(); begin putFloat(1.1); end"""
        expect = "1.1"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_bin_op_float_add_float(self):
        input = """procedure main(); begin putFloat(3.0+2.0); end"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_bin_op_int_sub_int(self):
        input = """procedure main(); begin putInt(3-2); end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_bin_op_float_add_int(self):
        input = """procedure main(); begin putFloat(3.0+2); end"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_bin_op_int_sub_float(self):
        input = """procedure main(); begin putFloat(3.0-2); end"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_bin_op_float_div_int(self):
        input = """procedure main(); begin putFloat(3.0/2); end"""
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_bin_op_int_div_int(self):
        input = """procedure main(); begin putFloat(4/2); end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,508))
