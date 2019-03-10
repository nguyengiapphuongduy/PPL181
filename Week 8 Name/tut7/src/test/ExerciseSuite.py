import unittest
from TestUtils import TestExercise
from AST import *
from Visitor import *

class ExerciseSuite(unittest.TestCase):
    def test_simple_program(self):
        input = Program([VarDecl('a',IntType()),FuncDecl(Id("main"),[],[],[])])
        expect = [VarDecl('a',IntType())]
        self.assertTrue(TestExercise.check(input,expect))
