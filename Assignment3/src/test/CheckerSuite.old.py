import unittest
from TestUtils import TestChecker
from AST import *
# from StaticError import *

class CheckerSuite(unittest.TestCase):
	def test_0_redeclared(self):
		"""Redeclared Variable"""
		input = """var x:integer;
		procedure main(); begin end
		var x:boolean;"""
		expect = "Redeclared Variable: x"
		#expect = Redeclared(Variable(),'x')
		self.assertTrue(TestChecker.test(input,expect,400))

	def test_1_redeclared(self):
		"""Redeclared Procedure"""
		input = """var x:integer;
		procedure main(); begin end
		procedure main(x:boolean); begin end"""
		expect = "Redeclared Procedure: main"
		self.assertTrue(TestChecker.test(input,expect,401))

	def test_2_redeclared(self):
		"""Redeclared Parameter"""
		input = """var x,y:integer;
		procedure main(); begin end
		procedure p(x:boolean;x:integer); begin end"""
		expect = "Redeclared Parameter: x"
		self.assertTrue(TestChecker.test(input,expect,402))

	def test_3_redeclared(self):
		"""Parameter with the same name (i) in different scope is ok"""
		input = """var i:integer;
		procedure main(); begin end
		procedure p(i:boolean); begin with y:real;y:real; do begin end end
		"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,403))

	def test_4_redeclared(self):
		"""Redeclared Function"""
		input = """var x,y:integer;
		procedure main(); begin end
		procedure p(i:boolean); begin end
		function p(x:integer):real; begin return 1; end"""
		expect = "Redeclared Function: p"
		self.assertTrue(TestChecker.test(input,expect,404))

	def test_5_undeclared(self):
		"""Undeclared Identifier"""
		input = """var x,y:integer;
		procedure main(); begin a:=1; end"""
		expect = "Undeclared Identifier: a"
		self.assertTrue(TestChecker.test(input,expect,405))

	def test_6_undeclared(self):
		"""Undeclared Identifier"""
		input = """var x,y:integer;
		procedure main(); var a:integer; begin end
		procedure fu(); begin a:=0; end"""
		expect = "Undeclared Identifier: a"
		self.assertTrue(TestChecker.test(input,expect,406))

	def test_7_undeclared(self):
		"""Undeclared Procedure"""
		input = """var x,y:integer;
		procedure main(); var a:integer; begin f(); end
		procedure fu(); begin end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,407))

	def test_8_type_mismatch_in_expression(self):
		"""Type mismatch in Call Expression"""
		input = """var x,y:integer;
		function foo(a:real;b:boolean):real; begin return 1; end
		procedure main(); var x:real; begin x:=foo(1,2); {error} end"""
		expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(1),IntLiteral(2)])"
		self.assertTrue(TestChecker.test(input,expect,408))

	def test_9_call_expression(self):
		"""Call Expression is OK"""
		input = """var x,y:integer;
		function foo(a:real;b:boolean):real; begin return 1; end
		procedure main(); var x:real; begin x:=foo(1,false); {OK} end
		procedure f(); var y:integer; y:real; begin end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,409))

	def test_10_global_scope(self):
		"""Global scope have effect on entire program"""
		input = """var x,y:integer;
		procedure main(); var x:real; begin x:=foo(1,false); {OK} end
		function foo(a:real;b:boolean):real; begin return 1e2; end
		procedure f(); var y:integer; y:real; begin end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,410))

	def test_11_funcdecl(self):
		"""Use parameter in function"""
		input = """var x,y:integer;
		procedure main(); var x:real; begin x:=y(1,false); {error} end"""
		expect = "Undeclared Function: y"
		self.assertTrue(TestChecker.test(input,expect,411))

	def test_12_funcdecl(self):
		"""Function and Variable have the same name"""
		input = """var x,y:integer;
		procedure main(); var x:real; begin x:=y(1,false); end
		function y(a:integer;b:boolean):integer; begin return 1; end"""
		expect = "Redeclared Function: y"
		self.assertTrue(TestChecker.test(input,expect,412))

	def test_13_funcdecl(self):
		"""Function and its Parameter have the same name is OK"""
		input = """var x:integer;
		procedure main(); var x:real; begin x:=y(1,2); end
		function y(x:integer;y:boolean):integer; {OK} begin return 1; end"""
		expect = "Type Mismatch In Expression: CallExpr(Id(y),[IntLiteral(1),IntLiteral(2)])"
		self.assertTrue(TestChecker.test(input,expect,413))

	def test_14_procdecl(self):
		"""Need a variable but just found a procedure"""
		input = """var x:integer;
		procedure main(); var x:real; begin y(1,true); y:=1; end
		procedure y(x:integer;y:boolean); begin end"""
		expect = "Undeclared Identifier: y"
		self.assertTrue(TestChecker.test(input,expect,414))

	def test_15_function(self):
		"""Function return type"""
		input = """var x:integer;
		procedure main(); var x:real; begin x:=y(1,true); y:=1; end
		function y(x:integer;y:boolean):integer; begin return 1; end"""
		expect = "Undeclared Identifier: y"
		self.assertTrue(TestChecker.test(input,expect,415))

	def test_16_block_scope(self):
		"""Correct Block Scope"""
		input = """var x:integer;y:boolean;
		procedure main(); var x:boolean; begin
		with x,y:integer;z:array[1 .. 2]of real; do
		begin x:=1;y:=2;z[1]:=3; end
		y:=100; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(y),IntLiteral(100))"
		self.assertTrue(TestChecker.test(input,expect,416))

	def test_17_block_scope(self):
		"""Correct Block Scope"""
		input = """var x:integer;y:boolean;
		procedure main(); var x:boolean; begin
		with x,y:integer;z:array[1 .. 2]of real; do
		begin x:=1;y:=2;z[1]:=3; end
		x:=100; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),IntLiteral(100))"
		self.assertTrue(TestChecker.test(input,expect,417))

	def test_18_block_scope(self):
		"""Nested With Statement"""
		input = """var x:integer;y:boolean;
		procedure main(); var x:boolean; begin
		with x,y:integer;z:array[1 .. 2]of real; do
		begin x:=1;y:=2;z[1]:=3;
		x:=1.1; end end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),FloatLiteral(1.1))"
		self.assertTrue(TestChecker.test(input,expect,418))

	def test_19_block_scope(self):
		"""Nested With Statement"""
		input = """var x:integer;y:boolean;
		procedure main(); var x:boolean; begin
		with x,y:integer;z:array[1 .. 2]of real; do
		begin x:=1;y:=2;z[1]:=3;
		with x:real; do x:=1.1; end
		x:=100; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),IntLiteral(100))"
		self.assertTrue(TestChecker.test(input,expect,419))

	def test_20_return(self):
		"""Wrong return"""
		input = """procedure main(); var x:integer; begin x:=foo();end
		function foo():integer; begin return true; end"""
		expect = "Type Mismatch In Statement: Return(Some(BooleanLiteral(True)))"
		self.assertTrue(TestChecker.test(input,expect,420))

	def test_21_return(self):
		"""Return type mismatch"""
		input = """procedure main(); var x:integer; begin x:=foo();end
		function foo():boolean; begin return true; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Id(foo),[]))"
		self.assertTrue(TestChecker.test(input,expect,421))

	def test_22_function_not_return(self):
		"""Missing return"""
		input = """procedure main(); var x:integer; begin x:=foo();end
		function foo():integer; begin end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,422))

	def test_23_function_not_return(self):
		"""Missing return"""
		input = """procedure main(); var x:integer; begin x:=foo();end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin end
		a:=foo();
		end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,423))

	def test_24_return(self):
		"""Wrong return"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin end
		a:=foo(); return;
		end"""
		expect = "Type Mismatch In Statement: Return(None)"
		self.assertTrue(TestChecker.test(input,expect,424))

	def test_25_return(self):
		"""Wrong return"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin with c:boolean; do return; end
		end"""
		expect = "Type Mismatch In Statement: Return(None)"
		self.assertTrue(TestChecker.test(input,expect,425))

	def test_26_return(self):
		"""Wrong return"""
		input = """procedure main(); var x:boolean; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin with c:boolean; do return 1; end
		end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),CallExpr(Id(foo),[]))"
		self.assertTrue(TestChecker.test(input,expect,426))

	def test_27_if(self):
		"""If expression type check"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin if a>0 then a:=0; else b:=0; end
		end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,427))

	def test_28_if(self):
		"""If return type check"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin if a>0 then return; else return 0; end
		end"""
		expect = "Type Mismatch In Statement: Return(None)"
		self.assertTrue(TestChecker.test(input,expect,428))

	def test_29_if(self):
		"""Return in if flow"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin if a>0 then return 1; else b:=0; end
		end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,429))

	def test_30_if(self):
		"""Return in if flow"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		with a:integer;b:real; do begin if a>0 then a:=1; else return 0; end
		end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,430))

	def test_31_if(self):
		"""Return in if flow"""
		input = """procedure main(); var x:integer; begin x:=foo(); end
		function foo():integer; var a:real; begin
		if a>0 then return 0;
		end"""
		expect = "Function foo Not Return"
		self.assertTrue(TestChecker.test(input,expect,431))

	def test_32_if(self):
		"""Return in if flow"""
		input = """function foo():integer; var a:real; begin
		with a:integer;b:real; do begin if a=0 then return 1; else return a; end
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,432))

	def test_33_while(self):
		"""Normal While statement"""
		input = """function foo():integer; var a:real; begin
		while a > 0 do a:=-1;
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,433))

	def test_34_break(self):
		"""Test break in while"""
		input = """function foo():integer; var a:real; begin
		while a > 0 do
		with a:integer;b:boolean; do begin b:=true; break; end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,434))

	def test_35_break(self):
		"""Break not in loop"""
		input = """function foo():integer; var a:real; begin
		while a > 0 do
		with a:integer;b:boolean; do begin b:=true; break; end
		break; return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Break Not In Loop"
		self.assertTrue(TestChecker.test(input,expect,435))

	def test_36_for(self):
		"""Normal For statement"""
		input = """function foo():integer; var a:integer; begin
		for a:=1 to 2 do
		with a:integer;b:boolean; do begin b:=true; break; end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,436))

	def test_37_for(self):
		"""Identifier type mismatch in for statement"""
		input = """function foo():integer; var a:real; begin
		for a:=1 to 2 do
		with a:integer;b:boolean; do begin b:=true; break; end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Type Mismatch In Statement: For(Id(a)IntLiteral(1),IntLiteral(2),True,[With([VarDecl(Id(a),IntType),VarDecl(Id(b),BoolType)],[AssignStmt(Id(b),BooleanLiteral(True)),Break])])"
		self.assertTrue(TestChecker.test(input,expect,437))

	def test_38_for(self):
		"""Normal For statement"""
		input = """function foo():integer; var a:integer; begin
		for a:=-1 to -2 do
		with a:integer;b:boolean; do begin b:=true; break; end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,438))

	def test_39_for(self):
		"""Expression type mismatch in For statement"""
		input = """function foo():integer; var a:integer; begin
		for a:=1+1.5 to -2 do begin end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Type Mismatch In Statement: For(Id(a)BinaryOp(+,IntLiteral(1),FloatLiteral(1.5)),UnaryOp(-,IntLiteral(2)),True,[])"
		self.assertTrue(TestChecker.test(input,expect,439))

	def test_40_for(self):
		"""Expression type mismatch in For statement"""
		input = """function foo():integer; var a:integer; begin
		for a:=false to 1 do begin end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Type Mismatch In Statement: For(Id(a)BooleanLiteral(False),IntLiteral(1),True,[])"
		self.assertTrue(TestChecker.test(input,expect,440))

	def test_41_while(self):
		"""Expression type mismatch in While statement"""
		input = """function foo():integer; var a:integer; begin
		while(1) do begin end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Type Mismatch In Statement: While(IntLiteral(1),[])"
		self.assertTrue(TestChecker.test(input,expect,441))

	def test_42_while(self):
		"""Expression type mismatch in While statement"""
		input = """function foo():integer; var a:integer; begin
		while(1+true) do begin end
		return 1;
		end
		procedure main(); var x:integer; begin x:=foo(); foo(); end"""
		expect = "Type Mismatch In Expression: BinaryOp(+,IntLiteral(1),BooleanLiteral(True))"
		self.assertTrue(TestChecker.test(input,expect,442))

	def test_43_default_test_in_pdf(self):
		"""Default test in MP.pdf. Add CallStmt foo for error checking"""
		input = """var i:integer; function f():integer;
		begin return 200; end
		procedure main(); var main:integer;
		begin
			main:=f(); putIntLn(main);
			with
				i:integer;
				main:integer;
				f:integer;
			do begin
				main:=f:=i:=100;
				putIntLn(i);
				putIntLn(main);
				putIntLn(f);
			end
			putIntLn(main); foo();
		end var g:real;"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,443))

	def test_44_assign_statement(self):
		"""Assign Statement"""
		input = """var x,y:integer;
		procedure main(); var a:integer; begin x:=true; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),BooleanLiteral(True))"
		self.assertTrue(TestChecker.test(input,expect,444))

	def test_45_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		procedure main(); var x:real; begin x:=1;
		with y:integer;y:real; do begin end end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,445))

	def test_46_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		procedure main(); var x:array[1 .. 3]of real; begin x[1]:=1;
		with y:integer;y:real; do begin end end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,446))

	def test_47_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		function f(): array[1 .. 3] of real;
		var a: array[1 .. 3] of real;
		begin a[2]:=1.1; return a; end
		procedure main(); var x:array[1 .. 3]of real;
		begin f()[1]:=x[1]:=1; with y:real;y:real; do begin end end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,447))

	def test_48_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		function f(): array[1 .. 3] of real;
		var a: array[1 .. 2] of real;
		begin a[2]:=1.1; return a; end
		procedure main(); var x:array[1 .. 3]of real;
		begin f()[1]:=x[1]:=1; end"""
		expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
		self.assertTrue(TestChecker.test(input,expect,448))

	def test_49_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		function f(): array[1 .. 2] of real;
		var a: array[1 .. 3] of real;
		begin a[2]:=1.1; return a; end
		procedure main(); var x:array[1 .. 3]of real;
		begin f()[1]:=x[1]:=1; end"""
		expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
		self.assertTrue(TestChecker.test(input,expect,449))

	def test_50_assign_statement(self):
		"""Assign Statement is OK"""
		input = """var x,y:integer;
		function f(): array[1 .. 3] of real;
		var a: array[1 .. 3] of real;
		begin a[2]:=1.1; return a; end
		procedure main(); var x:array[1 .. 2]of real;
		begin f()[1]:=x[1]:=1; with y:real;y:real; do begin end end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,450))

	def test_51_parameter_in_function(self):
		"""Parameter type check"""
		input = """var x,y:real;
		function f(x:array[1 .. 2] of real):real;
		begin return x[2]; end
		procedure main(); var x:array[1 .. 2]of real;
		begin x[1]:=y:=f(x); with y:real;y:real; do begin end end"""
		expect = "Redeclared Variable: y"
		self.assertTrue(TestChecker.test(input,expect,451))

	def test_52_parameter_in_function(self):
		"""Parameter type check"""
		input = """var x,y:real;
		function f(x:array[1 .. 2] of real):real;
		begin return x[2]; end
		procedure main(); var x:array[1 .. 3]of real;
		begin x[1]:=y:=f(x); with y:real;y:real; do begin end end"""
		expect = "Type Mismatch In Expression: CallExpr(Id(f),[Id(x)])"
		self.assertTrue(TestChecker.test(input,expect,452))

	def test_53_expressions(self):
		"""Expression type check: /"""
		input = """procedure main(); var x:integer;
		begin x:=-1+2*3/4; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),BinaryOp(+,UnaryOp(-,IntLiteral(1)),BinaryOp(/,BinaryOp(*,IntLiteral(2),IntLiteral(3)),IntLiteral(4))))"
		self.assertTrue(TestChecker.test(input,expect,453))

	def test_54_expressions(self):
		"""Expression type check: *-+"""
		input = """procedure main(); var x:integer;
		begin x:=-1+2*3; y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,454))

	def test_55_expressions(self):
		"""Expression type check: >"""
		input = """procedure main(); var x:boolean;
		begin x:=-1+2*3>0; y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,455))

	def test_56_expressions(self):
		"""Expression type check: *"""
		input = """procedure main(); var x:integer;
		begin x:=2*3.0; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),BinaryOp(*,IntLiteral(2),FloatLiteral(3.0)))"
		self.assertTrue(TestChecker.test(input,expect,456))

	def test_57_expressions(self):
		"""Expression type check: div"""
		input = """procedure main(); var x:integer;
		begin x:=5 div 3; y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,457))

	def test_58_expressions(self):
		"""Expression type check: mod"""
		input = """procedure main(); var x:integer;
		begin x:=7561 mod 52; y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,458))

	def test_59_expressions(self):
		"""Expression type check: -"""
		input = """procedure main(); var x:integer;
		begin x:=-1.0; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),UnaryOp(-,FloatLiteral(1.0)))"
		self.assertTrue(TestChecker.test(input,expect,459))

	def test_60_expressions(self):
		"""Expression type check: not"""
		input = """procedure main(); var x:boolean;
		begin x:=not (1>0); y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,460))

	def test_61_expressions(self):
		"""Expression type check: mod"""
		input = """procedure main(); var x:integer;
		begin x:=7. moD 3; end"""
		expect = "Type Mismatch In Expression: BinaryOp(moD,FloatLiteral(7.0),IntLiteral(3))"
		self.assertTrue(TestChecker.test(input,expect,461))

	def test_62_expressions(self):
		"""Expression type check: and or"""
		input = """procedure main(); var x:boolean;
		begin x:=not (1>0) and true or (0=0); y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,462))

	def test_63_expressions(self):
		"""Expression type check: andthen orelse"""
		input = """procedure main(); var x:boolean; y:real;
		begin x:=not (1>0) and then (y>.0) or else (true or false); y(); end"""
		expect = "Undeclared Procedure: y"
		self.assertTrue(TestChecker.test(input,expect,463))

	def test_64_string_type(self):
		"""String Type"""
		input = """procedure main(); var x:string;
		begin x:="error"; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),StringLiteral(error))"
		self.assertTrue(TestChecker.test(input,expect,464))

	def test_65_array_type(self):
		"""Array Type"""
		input = """procedure main(); var x,y:array[0 .. 100]of boolean;
		begin x:=y; end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(x),Id(y))"
		self.assertTrue(TestChecker.test(input,expect,465))

	def test_66_function_not_return(self):
		"""Return but not in all paths of If Statement"""
		input = """procedure main(); var x:integer;
		begin x:=fu(); end
		function fu():integer;
		begin with a:real; do
		with a:boolean; do if(true)then return 1;end"""
		expect = "Function fu Not Return"
		self.assertTrue(TestChecker.test(input,expect,466))

	def test_67_function_not_return(self):
		"""Return but in while loop"""
		input = """procedure main(); var x:integer;
		begin x:=fu(); end
		function fu():integer;
		begin with a:real; do
		with a:boolean; do while(true)do return 1;end"""
		expect = "Function fu Not Return"
		self.assertTrue(TestChecker.test(input,expect,467))

	def test_68_function_not_return(self):
		"""Return but in for loop"""
		input = """procedure main(); var x:integer;
		begin x:=fu(); end
		function fu():integer;
		begin with a:boolean; do
		with a:integer; do for a:=-5 to 5 do return 1;end"""
		expect = "Function fu Not Return"
		self.assertTrue(TestChecker.test(input,expect,468))

	def test_69_function_not_return(self):
		"""Nested If"""
		input = """procedure main(); var x:integer;
		begin x:=fu(); end
		function fu():integer;
		begin with a:real; do with a:boolean;b,c:real; do
		if(true)then
			if(b>c)then
				return -5;
		else return 6;
		end"""
		expect = "Function fu Not Return"
		self.assertTrue(TestChecker.test(input,expect,469))

	def test_70_function_not_return(self):
		"""Returned"""
		input = """procedure main(); var x:integer;
		begin x:=fu(); end
		function fu():integer;
		begin with a:real; do with a:boolean;b,c:integer; do
		if(a)then begin
			if(b>c)then
				return -5;
			return b;
		end
		else return 6;
		end
		function fuuu():integer; begin end"""
		expect = "Function fuuu Not Return"
		self.assertTrue(TestChecker.test(input,expect,470))

	def test_71_break(self):
		"""Break in loop"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do with x:integer; do break;
		end foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,471))

	def test_72_break(self):
		"""More complex nested with"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then break;
			with x:integer; do break;
		end{with} end{with} foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,472))

	def test_73_break(self):
		"""More complex nested With-If"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then break;
			with x:integer; do if (x=0) then break; else return;
		end{with} end{while} foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,473))

	def test_74_break(self):
		"""More complex nested With-If"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then break;
			with x:integer; do if (x=0) then return;
		end{with} break; end{while} break; end"""
		expect = "Break Not In Loop"
		self.assertTrue(TestChecker.test(input,expect,474))

	def test_75_continue(self):
		"""Continue in loop"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do with x:integer; do continue;
		end foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,475))

	def test_76_continue(self):
		"""More complex nested with"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then continue;
			with x:integer; do continue;
		end{with} end{with} foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,476))

	def test_77_continue(self):
		"""More complex nested With-If"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then continue;
			with x:integer; do if (x=0) then continue; else return;
		end{with} end{while} foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,477))

	def test_78_continue(self):
		"""More complex nested With-If"""
		input = """procedure main(); var x:integer;
		begin while(true)do begin
		with x:integer; do with x:real; do begin
			if (x>0) then continue;
			with x:integer; do if (x=0) then return;
		end{with} continue; end{while} continue; end"""
		expect = "Continue Not In Loop"
		self.assertTrue(TestChecker.test(input,expect,478))

	def test_79_index_expr(self):
		"""Index Expression"""
		input = """procedure main(); var a:real;x:integer;
		begin a:=x[1]; end"""
		expect = "Type Mismatch In Expression: ArrayCell(Id(x),IntLiteral(1))"
		self.assertTrue(TestChecker.test(input,expect,479))

	def test_80_index_expr(self):
		"""Index Expression"""
		input = """procedure main(); var a:real;x:array[1 .. 10]of integer;
		begin a:=x[1.]; end"""
		expect = "Type Mismatch In Expression: ArrayCell(Id(x),FloatLiteral(1.0))"
		self.assertTrue(TestChecker.test(input,expect,480))

	def test_81_index_expr(self):
		"""Index Expression"""
		input = """procedure main(); var a:real;x:array[1 .. 10]of integer;
		begin a:=x[sq(2)]; end
		function sq(m:real):real; begin return m*m; end"""
		expect = "Type Mismatch In Expression: ArrayCell(Id(x),CallExpr(Id(sq),[IntLiteral(2)]))"
		self.assertTrue(TestChecker.test(input,expect,481))

	def test_82_index_expr(self):
		"""Index Expression"""
		input = """procedure MaiN(); var a:real;x:array[1 .. 10]of real;
		begin a:=x[sq(2)]; fuc(); end
		function sq(m:integer):integer; begin return m*m; end"""
		expect = "Undeclared Procedure: fuc"
		self.assertTrue(TestChecker.test(input,expect,482))

	def test_83_index_expr(self):
		"""Index Expression"""
		input = """function func(): array[1 .. 10] of real;
		var x: array[1 .. 10] of real; i:integer;
		begin for i:=1 to 10 do x[i]:=i*2; return x; end
		function sq(m:integer):integer; begin return m*m; end
		procedure main(); var a:real;
		begin a:=func()[sq(2)]; fuc(); end"""
		expect = "Undeclared Procedure: fuc"
		self.assertTrue(TestChecker.test(input,expect,483))

	def test_84_entry_point(self):
		"""Identifier MAIN not found"""
		input = """procedure mainn(); var a:real;x:array[1 .. 10]of real;
		begin a:=x[sq(2)]; end
		function sq(m:integer):integer; begin return m*m; end"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,484))

	def test_85_entry_point(self):
		"""Found main but have parameters"""
		input = """procedure main(pa:boolean); var a:real;x:array[1 .. 10]of real;
		begin a:=x[sq(2)]; fuc(); end
		function sq(m:integer):integer; begin return m*m; end"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,485))

	def test_86_entry_point(self):
		"""Found main with no params but it was a function"""
		input = """function main():boolean; begin return true; end"""
		expect = "No entry point"
		self.assertTrue(TestChecker.test(input,expect,486))

	def test_87_entry_point(self):
		"""Have void main but redeclared"""
		input = """function MAIN():boolean; begin return true; end
		procedure main(); begin end"""
		expect = "Redeclared Procedure: main"
		self.assertTrue(TestChecker.test(input,expect,487))

	def test_88_builtin(self):
		"""Built-in functions Int"""
		input = """var r: real; procedure main(); begin r:=getInt(); f(); end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,488))

	def test_89_builtin(self):
		"""Built-in functions Int"""
		input = """procedure main(); begin putInt(10); f(); end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,489))

	def test_90_builtin(self):
		"""Built-in functions Float"""
		input = """var i:integer; procedure main(); begin i:=getFloat(); end"""
		expect = "Type Mismatch In Statement: AssignStmt(Id(i),CallExpr(Id(getFloat),[]))"
		self.assertTrue(TestChecker.test(input,expect,490))

	def test_91_builtin(self):
		"""Built-in function Float"""
		input = """procedure main(); begin putFloat(10); putfloat(.1); f(); end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,491))

	def test_92_builtin(self):
		"""Built-in function Bool"""
		input = """procedure main(); var a:real;
		begin a:=1; putBOOL(false); putBool(a>0); f(); end"""
		expect = "Undeclared Procedure: f"
		self.assertTrue(TestChecker.test(input,expect,492))

	def test_93_builtin(self):
		"""String as Parameter"""
		input = """procedure main(); begin putstring("1234"); end"""
		expect = "Type Mismatch In Statement: CallStmt(Id(putstring),[StringLiteral(1234)])"
		self.assertTrue(TestChecker.test(input,expect,493))

	def test_94_misc(self):
		"""A test from BKeL"""
		input = """var a:integer;procedure foo1();
		begin putIntLn(4); end
		procedure main();
		begin a := foo1 + 1; end"""
		expect = "Undeclared Identifier: foo1"
		self.assertTrue(TestChecker.test(input,expect,494))

	def test_95_misc(self):
		"""Return in If Else"""
		input = """function f(): boolean;
		var a,b,c,d:integer;
		begin
			if a > b then
				if c > d then
					return True;
				else
					return False;
			else
				with f: integer; do
					return True;
		end
		procedure main(); var x:boolean; begin x:=f(); foo(); end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,495))

	def test_96_default_test_undeclared_function(self):
		"""Simple program: int main() {} """
		input = """procedure main(); begin foo();end"""
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,496))

	def test_97_default_test_diff_numofparam_stmt(self):
		"""More complex program"""
		input = """procedure main (); begin
			putIntLn();
		end"""
		expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[])"
		self.assertTrue(TestChecker.test(input,expect,497))

	def test_98_default_test_undeclared_function_use_ast(self):
		"""Simple program: int main() {} """
		input = Program([FuncDecl(Id("main"),[],[],[
			CallStmt(Id("foo"),[])])])
		expect = "Undeclared Procedure: foo"
		self.assertTrue(TestChecker.test(input,expect,498))

	def test_99_function_or_procedure(self):
		"""Call a function but just found a procedure"""
		input = """procedure foo();begin return; end
		procedure main();var a:integer;
		begin a:=foo(); end"""
		expect = "Undeclared Function: foo"
		self.assertTrue(TestChecker.test(input,expect,499))
