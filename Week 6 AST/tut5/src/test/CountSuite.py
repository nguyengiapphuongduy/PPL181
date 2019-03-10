import unittest
from TestUtils import TestCount
from AST import *

class CountSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """procedure main(); begin end"""
        expect = "12"
        self.assertTrue(TestCount.test(input,expect,300))

    def test_simple_function(self):
        """More complex program"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = "23"
        self.assertTrue(TestCount.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = "39"
        self.assertTrue(TestCount.test(input,expect,302))

    def test_question_3(self):
        """Simple funcdecl"""
        input = """
		function foo(): integer;
		begin end
		"""
        expect = "15"
        self.assertTrue(TestCount.test(input,expect,303))

    def test_question_4(self):
        """multiple stmt funcdecl"""
        input = """
		function foo(): integer;
		begin
		f();
		s();
		end
		"""
        expect = "27"
        self.assertTrue(TestCount.test(input,expect,304))