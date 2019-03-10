import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_00_program(self):
        """Simple blank program"""
        input = """procedure main(); begin end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_01_program(self):
        """Simple blank program: more begin end"""
        input = """procedure main(); begin begin begin end end end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_02_vardecl(self):
        """Simple declaration"""
        input = """var x,y,z:integer;"""
        expect = str(Program([VarDecl(Id('x'),IntType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),IntType())]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_03_vardecl(self):
        """Multiple variable declaration"""
        input = """var x,y: integer;
		z:BooLean;"""
        expect = str(Program([VarDecl(Id('x'),IntType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_04_vardecl(self):
        """Multiple variable declaration"""
        input = """var x,y: integer;
		var z:BooLean;"""
        expect = str(Program([VarDecl(Id('x'),IntType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),BoolType())]))
        self.assertTrue(TestAST.test(input,expect,304))

    def test_05_arraydecl(self):
        """Simple array declaration"""
        input = """var x,y:array[1 .. 2] of integer;"""
        expect = str(Program([VarDecl(Id('x'),ArrayType(1,2,IntType())),VarDecl(Id('y'),ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,305))

    def test_06_arraydecl(self):
        """Simple array declaration"""
        input = """var x:array[-1 .. -2] of integer;"""
        expect = str(Program([VarDecl(Id('x'),ArrayType(-1,-2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,306))

    def test_07_arraydecl(self):
        """Simple array declaration"""
        input = """var x:array[1 .. -2] of integer;"""
        expect = str(Program([VarDecl(Id('x'),ArrayType(1,-2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,307))

    def test_08_funcdecl(self):
        """Blank function declaration"""
        input = """function f():integer; begin end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,308))

    def test_09_funcdecl(self):
        """Add param"""
        input = """function f(x:boolEAN):integer; begin end"""
        expect = str(Program([FuncDecl(Id("f"),[VarDecl(Id('x'),BoolType())],[],[],IntType())]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10_funcdecl(self):
        """Add more param"""
        input = """function f1(x:boolEAN;y,z:integer):real; begin end"""
        expect = str(Program([FuncDecl(Id('f1'),[VarDecl(Id('x'),BoolType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),IntType())],[],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,310))

    def test_11_funcdecl(self):
        """Add local variable"""
        input = """function f1(x:boolEAN;y,z:integer):real;
		var s:string;
		begin end"""
        expect = str(Program([FuncDecl(Id('f1'),[VarDecl(Id('x'),BoolType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),IntType())],[VarDecl(Id('s'),StringType())],[],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12_funcdecl(self):
        """Add function body"""
        input = """function f1(x:boolEAN;y,z:integer):real;
		var s:string;
		begin
			thisisstatement();
		end"""
        expect = str(Program([FuncDecl(Id('f1'),[VarDecl(Id('x'),BoolType()),VarDecl(Id('y'),IntType()),VarDecl(Id('z'),IntType())],[VarDecl(Id('s'),StringType())],[CallStmt(Id('thisisstatement'),[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13_procdecl(self):
        """Blank procedure declaration"""
        input = """procedure f(); begin end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[])]))
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14_procdecl(self):
        """Add param"""
        input = """procedure f(x:real); begin end"""
        expect = str(Program([FuncDecl(Id("f"),[VarDecl(Id('x'),FloatType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15_procdecl(self):
        """Add more param"""
        input = """procedure f(x:real;y,z:booleaN); begin end"""
        expect = str(Program([FuncDecl(Id("f"),[VarDecl(Id('x'),FloatType()),VarDecl(Id('y'),BoolType()),VarDecl(Id('z'),BoolType())],[],[])]))
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16_procdecl(self):
        """Add local variable"""
        input = """procedure f(x:real;y,z:booleaN);
		var vari:array[1 .. 100] of boolean;
		begin end"""
        expect = str(Program([FuncDecl(Id("f"),[VarDecl(Id('x'),FloatType()),VarDecl(Id('y'),BoolType()),VarDecl(Id('z'),BoolType())],[VarDecl(Id('vari'),ArrayType(1,100,BoolType()))],[])]))
        self.assertTrue(TestAST.test(input,expect,316))

    def test_17_procdecl(self):
        """Add procedure body"""
        input = """procedure f(x:real;y,z:booleaN);
		var vari:array[1 .. 100] of boolean;
		begin
			foo(x+1);
		end"""
        expect = str(Program([FuncDecl(Id("f"),[VarDecl(Id('x'),FloatType()),VarDecl(Id('y'),BoolType()),VarDecl(Id('z'),BoolType())],[VarDecl(Id('vari'),ArrayType(1,100,BoolType()))],[CallStmt(Id('foo'),[BinaryOp('+',Id('x'),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,317))

    def test_18_if(self):
        """Blank if statement"""
        input = """function f():real; begin
		if (x) then
			begin
			end
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,318))

    def test_19_if(self):
        """Add statement"""
        input = """function f():real; begin
		if (x) then
			begin
				f(x);
			end
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[CallStmt(Id('f'),[Id('x')])],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20_if(self):
        """Add blank else"""
        input = """function f():real; begin
		if (x) then
			begin
				f(x);
			end
		else begin end
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[CallStmt(Id('f'),[Id('x')])],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,320))

    def test_21_if(self):
        """Add else statement"""
        input = """function f():real; begin
		if (x) then
			begin
				f(x);
			end
		else
			begin
				x:=1;
			end
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[CallStmt(Id('f'),[Id('x')])],[Assign(Id('x'),IntLiteral(1))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,321))

    def test_22_if(self):
        """Nested if"""
        input = """function f():real; begin
		if (x) then
			if (x) then
				begin end
			else goo();
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[If(Id('x'),[],[CallStmt(Id('goo'),[])])],[])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23_if(self):
        """Nested if"""
        input = """function f():real; begin
		if (x) then
			if (x) then
				begin end
			else begin end
		else goo();
		end"""
        expect = str(Program([FuncDecl(Id("f"),[],[],[If(Id('x'),[If(Id('x'),[],[])],[CallStmt(Id('goo'),[])])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,323))

    def test_24_while(self):
        """Blank while loop"""
        input = """procedure main();
		begin
			while (1) do begin end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[])])]))
        self.assertTrue(TestAST.test(input,expect,324))

    def test_25_while(self):
        """Add statement"""
        input = """procedure main();
		begin
			while (1) do a:=a+1;
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,325))

    def test_26_for(self):
        """Blank for loop"""
        input = """procedure main();
		begin
			for i:=a to b do begin end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id('i'),Id('a'),Id('b'),True,[])])]))
        self.assertTrue(TestAST.test(input,expect,326))

    def test_27_for(self):
        """Add statement"""
        input = """procedure main();
		begin
			for i:=a to b do foo(x);
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id('i'),Id('a'),Id('b'),True,[CallStmt(Id('foo'),[Id('x')])])])]))
        self.assertTrue(TestAST.test(input,expect,327))

    def test_28_break(self):
        """Add break"""
        input = """procedure main();
		begin
			while (1) do begin
				a:=a+1;
				break;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Break()])])]))
        self.assertTrue(TestAST.test(input,expect,328))

    def test_29_break(self):
        """Add more break"""
        input = """procedure main();
		begin
			while (1) do begin
				break; a:=a+1;
				break; break; break;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Break(),Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Break(),Break(),Break()])])]))
        self.assertTrue(TestAST.test(input,expect,329))

    def test_30_continue(self):
        """Add continue"""
        input = """procedure main();
		begin
			while (1) do begin
				a:=a+1;
				continue;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Continue()])])]))
        self.assertTrue(TestAST.test(input,expect,330))

    def test_31_continue(self):
        """Add more continue"""
        input = """procedure main();
		begin
			while (1) do begin
				continue; a:=a+1;
				continue;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Continue(),Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),Continue()])])]))

    def test_32_break_continue(self):
        """Add continue"""
        input = """procedure main();
		begin
			while (1) do begin
				a:=a+1;
				if (a>0) then break;
				else continue;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[While(IntLiteral(1),[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),If(BinaryOp('>',Id('a'),IntLiteral(0)),[Break()],[Continue()])])])]))
        self.assertTrue(TestAST.test(input,expect,332))

    def test_33_return(self):
        """Return in procedure"""
        input = """procedure main(); begin Return; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Return()])]))
        self.assertTrue(TestAST.test(input,expect,333))

    def test_34_return(self):
        """Return in function"""
        input = """function foo():boolean; begin Return; end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Return()],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,334))

    def test_35_return_exp(self):
        """Return expression"""
        input = """function foo():boolean; begin Return 1; end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[Return(IntLiteral(1))],BoolType())]))
        self.assertTrue(TestAST.test(input,expect,335))

    def test_36_with(self):
        """Blank with statement"""
        input = """procedure main();
		begin
			with a:boolean; do begin end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),BoolType())],[])])]))
        self.assertTrue(TestAST.test(input,expect,336))

    def test_37_with(self):
        """Add more vardecl"""
        input = """procedure main();
		begin
			with a:boolean;
			x:array[1 .. 2]of string; do begin end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),BoolType()),VarDecl(Id('x'),ArrayType(1,2,StringType()))],[])])]))
        self.assertTrue(TestAST.test(input,expect,337))

    def test_38_with(self):
        """Add statement"""
        input = """procedure main();
		begin
			with a:boolean;
			x:array[1 .. 2]of string;
			do begin
				x:=x+1;
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),BoolType()),VarDecl(Id('x'),ArrayType(1,2,StringType()))],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1)))])])]))
        self.assertTrue(TestAST.test(input,expect,338))

    def test_39_compstmt(self):
        """Add more statement"""
        input = """procedure main();
		begin
			with a:boolean;
			x:array[1 .. 2]of string;
			do begin
				x:=x+1;
				begin
					a:=TruE;
				end
			end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),BoolType()),VarDecl(Id('x'),ArrayType(1,2,StringType()))],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),Assign(Id('a'),BooleanLiteral(True))])])]))
        self.assertTrue(TestAST.test(input,expect,339))

    def test_40_compstmt(self):
        """Add more begin-end"""
        input = """procedure main();
		begin
			with a:boolean;
			x:array[1 .. 2]of string;
			do begin begin
				x:=x+1;
				begin begin
					a:=TruE;
				end end
			end end
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),BoolType()),VarDecl(Id('x'),ArrayType(1,2,StringType()))],[Assign(Id('x'),BinaryOp('+',Id('x'),IntLiteral(1))),Assign(Id('a'),BooleanLiteral(True))])])]))
        self.assertTrue(TestAST.test(input,expect,340))

    def test_41_call_statement(self):
        """Simple call"""
        input = """procedure main(); begin f(); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[])])]))
        self.assertTrue(TestAST.test(input,expect,341))

    def test_42_call_statement(self):
        """Full call"""
        input = """procedure main(); begin f(x*x,y,z); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('*',Id('x'),Id('x')),Id('y'),Id('z')])])]))
        self.assertTrue(TestAST.test(input,expect,342))

    def test_43_expr(self):
        """Blank expression"""
        input = """procedure main(); begin f(); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[])])]))
        self.assertTrue(TestAST.test(input,expect,343))

    def test_44_expr(self):
        """Add some expression: AND THEN, OR ELSE"""
        input = """procedure main(); begin f(1 and then 2 or else 3 or else 4); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('orelse',BinaryOp('orelse',BinaryOp('andthen',IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(4))])])]))
        self.assertTrue(TestAST.test(input,expect,344))

    def test_45_expr(self):
        """Left associative test"""
        input = """procedure main(); begin f(1+2-3); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('-',BinaryOp('+',IntLiteral(1),IntLiteral(2)),IntLiteral(3))])])]))
        self.assertTrue(TestAST.test(input,expect,345))

    def test_46_expr(self):
        """Precedence test"""
        input = """procedure main(); begin f(1+(2-3)); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('+',IntLiteral(1),BinaryOp('-',IntLiteral(2),IntLiteral(3)))])])]))
        self.assertTrue(TestAST.test(input,expect,346))

    def test_47_expr(self):
        """Precedence test"""
        input = """procedure main(); begin f(1+2/3); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('+',IntLiteral(1),BinaryOp('/',IntLiteral(2),IntLiteral(3)))])])]))
        self.assertTrue(TestAST.test(input,expect,347))

    def test_48_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1=2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('=',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,348))

    def test_49_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1<>2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('<>',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,349))

    def test_50_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1>2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('>',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,350))

    def test_51_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1<2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('<',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,351))

    def test_52_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1>=2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('>=',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,352))

    def test_53_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1<=2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('<=',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,353))

    def test_54_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1 OR 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('OR',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,354))

    def test_55_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1or 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('or',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,355))

    def test_56_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1 aND 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('aND',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,356))

    def test_57_expr(self):
        """Test boolean expression"""
        input = """procedure main(); begin f(1and 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('and',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,357))

    def test_58_expr(self):
        """DIV operator"""
        input = """procedure main(); begin f(1diV 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('diV',IntLiteral(1),IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,358))

    def test_59_expr(self):
        """MOD operator"""
        input = """procedure main(); begin f(1div 2mod 3); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BinaryOp('mod',BinaryOp('div',IntLiteral(1),IntLiteral(2)),IntLiteral(3))])])]))
        self.assertTrue(TestAST.test(input,expect,359))

    def test_60_expr(self):
        """NEGATION operator"""
        input = """procedure main(); begin f(-2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[UnaryOp('-',IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,360))

    def test_61_expr(self):
        """NOT operator"""
        input = """procedure main(); begin f(NOT 2); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[UnaryOp('NOT',IntLiteral(2))])])]))
        self.assertTrue(TestAST.test(input,expect,361))

    def test_62_expr(self):
        """Test brackets"""
        input = """procedure main(); begin f(((1))); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[IntLiteral(1)])])]))
        self.assertTrue(TestAST.test(input,expect,362))

    def test_63_expr(self):
        """Test invocation"""
        input = """procedure main(); begin f(f()); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[CallExpr(Id('f'),[])])])]))
        self.assertTrue(TestAST.test(input,expect,363))

    def test_64_expr(self):
        """Test invocation"""
        input = """procedure main(); begin f(f(str)); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[CallExpr(Id('f'),[Id('str')])])])]))
        self.assertTrue(TestAST.test(input,expect,364))

    def test_65_expr(self):
        """Test invocation"""
        input = """procedure main(); begin f(f(str),str); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[CallExpr(Id('f'),[Id('str')]),Id('str')])])]))
        self.assertTrue(TestAST.test(input,expect,365))

    def test_66_intlit(self):
        """Test integer literal"""
        input = """procedure main(); begin f(00001); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[IntLiteral(1)])])]))
        self.assertTrue(TestAST.test(input,expect,366))

    def test_67_intlit(self):
        """Test integer literal"""
        input = """procedure main(); begin f(01283471023747896341724); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[IntLiteral(1283471023747896341724)])])]))
        self.assertTrue(TestAST.test(input,expect,367))

    def test_68_boollit(self):
        """Test boolean literal"""
        input = """procedure main(); begin f(true,FALSE); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BooleanLiteral(True),BooleanLiteral(False)])])]))
        self.assertTrue(TestAST.test(input,expect,368))

    def test_69_boollit(self):
        """Test boolean literal"""
        input = """procedure main(); begin f(TruE,fAlSe); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[BooleanLiteral(True),BooleanLiteral(False)])])]))
        self.assertTrue(TestAST.test(input,expect,369))

    def test_70_floatlit(self):
        """Test float literal"""
        input = """procedure main(); begin f(.1); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[FloatLiteral(.1)])])]))
        self.assertTrue(TestAST.test(input,expect,370))

    def test_71_floatlit(self):
        """Test float literal"""
        input = """procedure main(); begin f(00.0001); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[FloatLiteral(0.0001)])])]))
        self.assertTrue(TestAST.test(input,expect,371))

    def test_72_floatlit(self):
        """Test float literal"""
        input = """procedure main(); begin f(1.2E1); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[FloatLiteral(1.2e1)])])]))
        self.assertTrue(TestAST.test(input,expect,372))

    def test_73_floatlit(self):
        """Test float literal"""
        input = """procedure main(); begin f(1e-1); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[FloatLiteral(0.1)])])]))
        self.assertTrue(TestAST.test(input,expect,373))

    def test_74_stringlit(self):
        """Test string literal"""
        input = """procedure main(); begin f("FUFUFUFU"); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[StringLiteral('FUFUFUFU')])])]))
        self.assertTrue(TestAST.test(input,expect,374))

    def test_75_index(self):
        """Index expression"""
        input = """procedure main(); begin f(a[1]); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[ArrayCell(Id('a'),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,375))

    def test_76_index(self):
        """Index expression"""
        input = """procedure main(); begin f(fu()[1]); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[ArrayCell(CallExpr(Id('fu'),[]),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,376))

    def test_77_index(self):
        """Index expression"""
        input = """procedure main(); begin f((1+a)[1]); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[ArrayCell(BinaryOp('+',IntLiteral(1),Id('a')),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,377))

    def test_78_index(self):
        """Index expression"""
        input = """procedure main(); begin f((1+a)[x][1]); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('f'),[ArrayCell(ArrayCell(BinaryOp('+',IntLiteral(1),Id('a')),Id('x')),IntLiteral(1))])])]))
        self.assertTrue(TestAST.test(input,expect,378))

    def test_79_assignment(self):
        """Simple assignment"""
        input = """procedure main(); begin a:=1; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('a'),IntLiteral(1))])]))
        self.assertTrue(TestAST.test(input,expect,379))

    def test_80_assignment(self):
        """Multiple assignment"""
        input = """procedure main(); begin a:=b:=1; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id("b"),IntLiteral(1)),Assign(Id("a"),Id("b"))])]))
        self.assertTrue(TestAST.test(input,expect,380))

    def test_81_assignment(self):
        """Add more complex assignment"""
        input = """procedure main(); begin a[-10]:=stfu()[0]:=c:=True or false; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('c'),BinaryOp('or',BooleanLiteral(True),BooleanLiteral(False))),Assign(ArrayCell(CallExpr(Id('stfu'),[]),IntLiteral(0)),Id('c')),Assign(ArrayCell(Id('a'),UnaryOp('-',IntLiteral(10))),ArrayCell(CallExpr(Id('stfu'),[]),IntLiteral(0)))])]))
        self.assertTrue(TestAST.test(input,expect,381))

    def test_82_for(self):
        """For to/downto"""
        input = """procedure main(); begin
		for x:=1 tO 10 do write(x);
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id('x'),IntLiteral(1),IntLiteral(10),True,[CallStmt(Id('write'),[Id('x')])])])]))
        self.assertTrue(TestAST.test(input,expect,382))

    def test_83_for(self):
        """For to/downto"""
        input = """procedure main(); begin
		for x:=1 dOwNto 10 do write(x);
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id('x'),IntLiteral(1),IntLiteral(10),False,[CallStmt(Id('write'),[Id('x')])])])]))
        self.assertTrue(TestAST.test(input,expect,383))

    def test_84_mixed(self):
        """Mixed expression"""
        input = """procedure main(); begin
		x:=1+1-2*3 div 4 mod 5/6;
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('x'),BinaryOp('-',BinaryOp('+',IntLiteral(1),IntLiteral(1)),BinaryOp('/',BinaryOp('mod',BinaryOp('div',BinaryOp('*',IntLiteral(2),IntLiteral(3)),IntLiteral(4)),IntLiteral(5)),IntLiteral(6))))])]))
        self.assertTrue(TestAST.test(input,expect,384))

    def test_85_mixed(self):
        """For loop, array cell"""
        input = """procedure main(); begin
		for asdfi := nnn downto x=n[1] do write(asdfi);
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[For(Id('asdfi'),Id('nnn'),BinaryOp('=',Id('x'),ArrayCell(Id('n'),IntLiteral(1))),False,[CallStmt(Id('write'),[Id('asdfi')])])])]))
        self.assertTrue(TestAST.test(input,expect,385))

    def test_86_expr(self):
        """Test expr"""
        input = """procedure main(); begin x:=a+-1; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('x'),BinaryOp('+',Id('a'),UnaryOp('-',IntLiteral(1))))])]))
        self.assertTrue(TestAST.test(input,expect,386))

    def test_87_randomly_begin_end(self):
        input = """procedure main(); begin
			begin
                begin
                end
                begin
                end
                a:=a+1;
            end
            fuckasdfthisjklassignment();
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('a'),BinaryOp('+',Id('a'),IntLiteral(1))),CallStmt(Id('fuckasdfthisjklassignment'),[])])]))
        self.assertTrue(TestAST.test(input,expect,387))

    def test_88_complex_program(self):
        """Mixed program from MP.pdf"""
        input = """
		var i:integer ;
        function f():integer ;
        begin
			return 200;
        end
        procedure main();
        var
			main:integer;
        begin
            main := f();
            putIntLn(main);
            with
                i:integer;
                main:integer;
                f:integer;
            do begin
                main := f := i := 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            end
            putIntLn(main);
        end
        var g:real;
		"""
        expect = str(Program([VarDecl(Id('i'),IntType()),FuncDecl(Id('f'),[],[],[Return(IntLiteral(200))],IntType()),FuncDecl(Id("main"),[],[VarDecl(Id('main'),IntType())],[Assign(Id('main'),CallExpr(Id('f'),[])),CallStmt(Id('putIntLn'),[Id('main')]),With([VarDecl(Id('i'),IntType()),VarDecl(Id('main'),IntType()),VarDecl(Id('f'),IntType())],[Assign(Id('i'),IntLiteral(100)),Assign(Id('f'),Id('i')),Assign(Id('main'),Id('f')),CallStmt(Id('putIntLn'),[Id('i')]),CallStmt(Id('putIntLn'),[Id('main')]),CallStmt(Id('putIntLn'),[Id('f')])]),CallStmt(Id('putIntLn'),[Id('main')])]),VarDecl(Id('g'),FloatType())]))
        self.assertTrue(TestAST.test(input,expect,388))

    def test_89_call_statement(self):
        """Call statement from MP.pdf"""
        input = """procedure main(); begin foo(3 , a+1, m(2)); end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[CallStmt(Id('foo'),[IntLiteral(3),BinaryOp('+',Id('a'),IntLiteral(1)),CallExpr(Id('m'),[IntLiteral(2)])])])]))
        self.assertTrue(TestAST.test(input,expect,389))

    def test_90_with(self):
        """With statement from MP.pdf"""
        input = """procedure main(); begin
		with a,b:integer; c:array [1 .. 2] of real; do d := c[a] + b;
		end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[With([VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),ArrayType(1,2,FloatType()))],[Assign(Id('d'),BinaryOp('+',ArrayCell(Id('c'),Id('a')),Id('b')))])])]))
        self.assertTrue(TestAST.test(input,expect,390))

    def test_91_assign(self):
        """Assign statement from MP.pdf"""
        input = """procedure main(); begin a := b[10] := foo()[3] := x := 1; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(Id('x'),IntLiteral(1)),Assign(ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(3)),Id('x')),Assign(ArrayCell(Id('b'),IntLiteral(10)),ArrayCell(CallExpr(Id('foo'),[]),IntLiteral(3))),Assign(Id('a'),ArrayCell(Id('b'),IntLiteral(10)))])]))
        self.assertTrue(TestAST.test(input,expect,391))

    def test_92_function_return(self):
        """Function return from MP.pdf"""
        input = """function foo(b:array [1 .. 2] of integer):array [2 .. 3] of real;
		var a:array [2 .. 3] of real;
		begin
			if (a=1) then return a; //CORRECT
			else return b; //WRONG
		end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id('b'),ArrayType(1,2,IntType()))],[VarDecl(Id('a'),ArrayType(2,3,FloatType()))],[If(BinaryOp('=',Id('a'),IntLiteral(1)),[Return(Id('a'))],[Return(Id('b'))])],ArrayType(2,3,FloatType()))]))
        self.assertTrue(TestAST.test(input,expect,392))

    def test_93_function_return(self):
        """Function return from MP.pdf"""
        input = """function foo():real; begin
		if (a=1) then return 2.3; //CORRECT
		else return 2;//CORRECT
		end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[If(BinaryOp('=',Id('a'),IntLiteral(1)),[Return(FloatLiteral(2.3))],[Return(IntLiteral(2))])],FloatType())]))
        self.assertTrue(TestAST.test(input,expect,393))

    def test_94_index_and_assign(self):
        """Index expression from MP.pdf"""
        input = """procedure main(); begin foo(2)[3+x] := a[b[2]] +3; end"""
        expect = str(Program([FuncDecl(Id("main"),[],[],[Assign(ArrayCell(CallExpr(Id('foo'),[IntLiteral(2)]),BinaryOp('+',IntLiteral(3),Id('x'))),BinaryOp('+',ArrayCell(Id('a'),ArrayCell(Id('b'),IntLiteral(2))),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,394))

    def test_95_function(self):
        """Function from MP.pdf"""
        input = """function foo(a,b:integer;c:real):array [1 .. 2] of integer;
		var x,y:real;
		begin end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),FloatType())],[VarDecl(Id('x'),FloatType()),VarDecl(Id('y'),FloatType())],[],ArrayType(1,2,IntType()))]))
        self.assertTrue(TestAST.test(input,expect,395))

    def test_96_procedure(self):
        """Procedure from MP.pdf"""
        input = """procedure foo(a,b:integer;c:real);
		var x,y:real;
		begin end"""
        expect = str(Program([FuncDecl(Id("foo"),[VarDecl(Id('a'),IntType()),VarDecl(Id('b'),IntType()),VarDecl(Id('c'),FloatType())],[VarDecl(Id('x'),FloatType()),VarDecl(Id('y'),FloatType())],[])]))
        self.assertTrue(TestAST.test(input,expect,396))

    def test_97_default(self):
        """Test function"""
        input = """function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,397))

    def test_98_default(self):
        """More complex program: call without parameter"""
        input = """procedure main (); begin
            getIntLn();
        end
        function foo ():INTEGER; begin
            putIntLn(4);
        end"""
        expect = str(Program([
                FuncDecl(Id("main"),[],[],[CallStmt(Id("getIntLn"),[])]),
                FuncDecl(Id("foo"),[],[],[CallStmt(Id("putIntLn"),[IntLiteral(4)])],IntType())]))
        self.assertTrue(TestAST.test(input,expect,398))

    def test_99_a_test_from_forum(self):
        """Nested if - assignment"""
        input = """procedure proc();
    begin
        if a > 3 then
            if a < 7 then 
                b := b + 2;
            else 
                b := "huhuhu";
    end"""
        expect = str(Program([FuncDecl(Id("proc"),[],[],[If(BinaryOp('>',Id('a'),IntLiteral(3)),[If(BinaryOp('<',Id('a'),IntLiteral(7)),[Assign(Id('b'),BinaryOp('+',Id('b'),IntLiteral(2)))],[Assign(Id('b'),StringLiteral('huhuhu'))])],[])])]))
        self.assertTrue(TestAST.test(input,expect,399))