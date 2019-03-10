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
    
    def test_float_ast(self):
    	input = """procedure main(); begin
            putFloat(5.5);
        end"""
    	expect = "5.5"
    	self.assertTrue(TestCodeGen.test(input,expect,502))
    
    def test_bin_add(self):
    	input = """procedure main(); begin
            putInt(1 + 3);
        end"""
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_bin_mul(self):
    	input = """procedure main(); begin
            putInt(1 * 3);
        end"""
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,504))
    
    def test_bin_sub(self):
    	input = """procedure main(); begin
            putInt(1 - 3);
        end"""
    	expect = "-2"
    	self.assertTrue(TestCodeGen.test(input,expect,505))
    
    def test_bin_div(self):
    	input = """procedure main(); begin
            putFloat(1/2);
        end"""
    	expect = "0.5"
    	self.assertTrue(TestCodeGen.test(input,expect,506))
    
    def test_bin_addF(self):
    	input = """procedure main(); begin
            putFloat(1+2.1);
        end"""
    	expect = "3.1"
    	self.assertTrue(TestCodeGen.test(input,expect,507))
    
    def test_bin_subF(self):
    	input = """procedure main(); begin
            putFloat(1.0-4.1);
        end"""
    	expect = "-3.1"
    	self.assertTrue(TestCodeGen.test(input,expect,508))
    
    def test_bin_mulF(self):
    	input = """procedure main(); begin
            putFloat(1.1 * 4);
        end"""
    	expect = "4.4"
    	self.assertTrue(TestCodeGen.test(input,expect,509))
	
    def test_10(self):
    	input = """procedure main(); begin
            putIntLn(100 div 3);
			putInt(100 mod 3);
        end"""
    	expect = """33
1"""
    	self.assertTrue(TestCodeGen.test(input,expect,510))
	
    def test_11(self):
    	input = """procedure main(); begin
			putBool(1 > 2);
			putBool(1 < 2);
			putBool(1 >= 1);
			putBool(1 <= 2);
			putBool(1 <> 2);
			putBool(1 = 2);
        end"""
    	expect = """falsetruetruetruetruefalse"""
    	self.assertTrue(TestCodeGen.test(input,expect,511))
	
    def test_12(self):
    	input = """procedure main(); begin
			putBool(1.0 > 2.0);
			putBool(1 < 2.2);
			putBool(1.1 >= 1.11);
			putBool(1.1 >= 1.1);
			putBool(1.21 <= 1.2);
			putBool(1.2 <= 1.2);
			putBool(1.1 <> (1 + 0.1));
			putBool(1.2 = 1.2);
        end"""
    	expect = """falsetruefalsetruefalsetruefalsetrue"""
    	self.assertTrue(TestCodeGen.test(input,expect,512))
	
    def test_13(self):
    	input = """procedure main(); begin
			putBool((1.0 > 2.0 ) and (2.0 > 1.0));
			putBool((1.0 >= 1.0 ) and (2 > 1));
			putBool(false and tRue);
        end"""
    	expect = """falsetruefalse"""
    	self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
    	input = """procedure main(); begin
			putBool((1.0 > 2.0 ) or (2.0 > 1.0));
			putBool((1.0 >= 1.0 ) or (2 > 1));
			putBool(false or (tRue and false));
        end"""
    	expect = """truetruefalse"""
    	self.assertTrue(TestCodeGen.test(input,expect,514))
	
    def test_15(self):
    	input = """
		procedure notMain();
		begin
			putInt(12);
		end
		procedure main(); begin
			putINT(1);
			notMaiN();
        end"""
    	expect = """112"""
    	self.assertTrue(TestCodeGen.test(input,expect,515))
	
    def test_16(self):
    	input = """
		function notMain() : integer;
		begin
			putInt(12);
			return 1;
		end
		procedure main(); begin
			putINT(notMain());
			
        end"""
    	expect = """121"""
    	self.assertTrue(TestCodeGen.test(input,expect,516))
	
    def test_17(self):
    	input = """
		var a : integer;
		procedure main(); begin
			putINT(1);
			
        end"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,517))
	
    def test_18(self):
    	input = """
		var a , b: integer;
		c : real;
		d:boolean;
		e:String;
		procedure main(); begin
			putINT(1);
			
        end"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,518))
    
    def test_19(self):
    	input = """
		var a , b: integer;
		
		procedure main();
		var x,y : integer;
		b : boolean;
		begin
			putINT(1);
			
        end"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_20(self):
    	input = """
		var a , b: integer;
		procedure notMain( d : real);
		var e : integer;
		begin
			putFloat(9.9);
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		begin
			notMAIN(1.2);
			putINT(1);
        end"""
    	expect = """9.91"""
    	self.assertTrue(TestCodeGen.test(input,expect,520))
	
    def test_21(self):
    	input = """
		var a , b: integer;
		procedure notMain( d : integer);
		var e : integer;
		begin
			putFloat(9.9);
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			notMAIN(x);
			putINT(x);
        end"""
    	expect = """9.91"""
    	self.assertTrue(TestCodeGen.test(input,expect,521))
	
    def test_22(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer) : integer;
		var e : integer;
		begin
			putFloat(9.9);
			return d;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			putINT(notMAIN(x));
        end"""
    	expect = """9.91"""
    	self.assertTrue(TestCodeGen.test(input,expect,522))
	
    def test_23(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : integer;
		begin
			putFloat(e + f);
			return d;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 9.9 / 2;
			putINT(notMAIN(x,z,9.9/2));
        end"""
    	expect = """9.91"""
    	self.assertTrue(TestCodeGen.test(input,expect,523))
	
    def test_24(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : integer;
		begin
			putFloat(e + f);
			return d;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 1;
			//putINT(notMAIN(x,1,8.9));
			putFLOAT(z);
        end"""
    	expect = """1.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_25(self):
    	input = """
		var a , b: integer;
		r : real;
		procedure main();
		
		begin
			a := 100;
			//r := 1.0;
			putINT(a);
			//putFLOAT(r + a);
        end"""
    	expect = """100"""
    	self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_26(self):
    	input = """
		var a , b: integer;
		r : real;
		procedure main();
		
		begin
			a := 1;
			r := 1;
			putINT(a);
			putFLOAT(r + a);
        end"""
    	expect = """12.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_27(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : integer;
		begin
			putFloat(e + f);
			return d;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			putINT(notMAIN(x,1,z));
			putFLOAT(z);
        end"""
    	expect = """9.918.9"""
    	self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_28(self):
    	input = """
		var a , b: integer;
		procedure notMain( d : integer ;e,f :real);
		begin
			putFloat(e + f);
			return ;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			notMAIN(x,1,z);
			putFLOAT(z);
        end"""
    	expect = """9.98.9"""
    	self.assertTrue(TestCodeGen.test(input,expect,528))
	
    def test_29(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : real;
		begin
			putFloat(e + f);
			return 1.0;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			z := z + notMAIN(x,1,z);
			putFLOAT(z);
        end"""
    	expect = """9.99.9"""
    	self.assertTrue(TestCodeGen.test(input,expect,529))
	
    def test_30(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : real;
		begin
			putFloat(e + f);
			return 1;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			z := z + notMAIN(x,1,z);
			putFLOAT(z);
        end"""
    	expect = """9.99.9"""
    	self.assertTrue(TestCodeGen.test(input,expect,530))
	
    def test_31(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :real) : real;
		begin
			putFloat(e + f);
			return d;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			z := z + notMAIN(x,1,z);
			putFLOAT(z);
        end"""
    	expect = """9.99.9"""
    	self.assertTrue(TestCodeGen.test(input,expect,531))
	
    def test_32(self):
    	input = """
		var a , b: integer;
		function notMain( d : integer ;e,f :boolean) : boolean;
		begin
			putBool(e and f);
			return d > 1.2;
		end
		procedure main();
		var x,y : integer;
		b : boolean;
		z : real;
		begin
			x := 1;
			z := 8.9;
			b := true;
			putBool(notMAIN(x,z=1,b));
        end"""
    	expect = """falsefalse"""
    	self.assertTrue(TestCodeGen.test(input,expect,532))
	
    def test_33(self):
    	input = """
		var a , b: booLEAN;
		r : reAl;
		procedure main();
		
		begin
			a := (1 > 0) or true;
			b := a;
			r := 1;
			putBool(a);
			putbool(b);
			putBOOL(a and b);
			putbool(a or b);
			putbool((r = 1) and b);
        end"""
    	expect = """truetruetruetruetrue"""
    	self.assertTrue(TestCodeGen.test(input,expect,533))
	
    def test_34(self):
    	input = """
		var 
		r : reAl;
		procedure main();
		
		begin
			
			r := 1;
			putFloat(-r);
			
        end"""
    	expect = """-1.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,534))
	
    def test_35(self):
    	input = """
		
		procedure main();
		var 
		r : reAl;
		a : integer;
		begin
			a:=-2;
			r := 1;
			putFloat(--r);
			putInt(-a);
			putInt(-----1);
        end"""
    	expect = """1.02-1"""
    	self.assertTrue(TestCodeGen.test(input,expect,535))
	
    def test_36(self):
    	input = """
		
		procedure main();
		var 
		b : boolean;
		a : integer;
		begin
			a:=-2;
			b := false;
			putBool(not b);
			putBool( -a >= 2 );
			putBool(not not not not b);
			putBool( not not (-a >= 2) );
        end"""
    	expect = """truetruefalsetrue"""
    	self.assertTrue(TestCodeGen.test(input,expect,536))
	
    def test_37(self):
    	input = """
		procedure main();
		begin
			putInt(12);
			notmain();
        end
		procedure notmain();
		begin
			putInt(12);
        end
		"""
    	expect = """1212"""
    	self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_38(self):
    	input = """
		
		procedure main();
		begin
			a:= 3;
			b:=4;
			putInt(12);
			notmain(a,b);
			notmain2();
        end
		procedure notmain(a ,b: integer);
		begin
			putInt(a * b);
        end
		var
		a,b:integer;
		procedure notmain2();
		begin
			putInt(12);
        end
		"""
    	expect = """121212"""
    	self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_39(self):
    	input = """
		
		procedure main();
		begin
			with a:integer ; do
			a:=1;
			putInt(1);
        end
		
		"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,539))
	
    def test_40(self):
    	input = """
		
		procedure main();
		begin
			with a:integer ; do
			begin
				a:=1;
				putInt(a + 1);
			end
        end
		
		"""
    	expect = """2"""
    	self.assertTrue(TestCodeGen.test(input,expect,540))
	
    def test_41(self):
    	input = """
		
		procedure main();
		var a : integer;
		begin
			a:=2;
			with a:integer ; do
			begin
				a:=1;
				putInt(a);
			end
			putInt(A);
        end
		
		"""
    	expect = """12"""
    	self.assertTrue(TestCodeGen.test(input,expect,541))
	
    def test_42(self):
    	input = """
		
		procedure main();
		var a ,b: integer;
		begin
			a:=2;
			b:=4;
			with a:integer ;c:real; do
			begin
				a:=1;
				c:=b;
				putInt(a);
				putFloat(c + a);
			end
			putInt(A);
        end
		
		"""
    	expect = """15.02"""
    	self.assertTrue(TestCodeGen.test(input,expect,542))
	
    def test_43(self):
    	input = """
		
		procedure main();
		var a ,b: integer;
		begin
			a:=2;
			b:=4;
			with a:boolean ;c:boolean; do
			begin
				a:=true;
				c:=false;
				putbool(a and then c);
				putbool(c and then a);
				putbool(c or else a);
				putbool(a or else c);
			end
			putInt(A);
        end
		
		"""
    	expect = """falsefalsetruetrue2"""
    	self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_44(self):
    	input = """
		
		procedure main();
		var a ,b: integer;
		begin
			if 1 > 2 then putInt(0);
			putInt(1);
        end
		
		"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_45(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			if 1 < 2 then putInt(0);
			putInt(1);
        end
		
		"""
    	expect = """01"""
    	self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_46(self):
    	input = """
		
		procedure main();
		var a ,b: integer;
		begin
			if 1 > 2 then putInt(0);
			else putInt(2);
			putInt(1);
        end
		
		"""
    	expect = """21"""
    	self.assertTrue(TestCodeGen.test(input,expect,546))
	
    def test_47(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			a := 2;
			if a = 2.0 then 
			begin 
				putInt(0);
				b:=1;
			end
			else begin 
				putInt(2);
				b:=2;
			end
			putInt(1 + b);
        end
		
		"""
    	expect = """02"""
    	self.assertTrue(TestCodeGen.test(input,expect,547))
	
    def test_48(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			a:=0;
			while a < 10 do
			begin
				a:=a+1;
				putInt(a);
			end
        end
		
		"""
    	expect = """12345678910"""
    	self.assertTrue(TestCodeGen.test(input,expect,548))
	
    def test_49(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=1 to 10 do
				putInt(a);
        end
		
		"""
    	expect = """12345678910"""
    	self.assertTrue(TestCodeGen.test(input,expect,549))
	
    def test_50(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=10 downto 1 do
				putInt(a);
        end
		
		"""
    	expect = """10987654321"""
    	self.assertTrue(TestCodeGen.test(input,expect,550))
	
    def test_51(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=10 downto 1 do
				if a < 2 then continue;
				else putint(a);
        end
		
		"""
    	expect = """1098765432"""
    	self.assertTrue(TestCodeGen.test(input,expect,551))
	
    def test_52(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=1 to 10 do
				if a < 4 then continue;
				else putint(a);
        end
		
		"""
    	expect = """45678910"""
    	self.assertTrue(TestCodeGen.test(input,expect,552))
	
    def test_53(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=10 downto 1 do
				if a < 5 then break;
				else putint(a);
        end
		
		"""
    	expect = """1098765"""
    	self.assertTrue(TestCodeGen.test(input,expect,553))
	
    def test_54(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=1 to 10 do
				if a > 7 then break;
				else putint(a);
        end
		
		"""
    	expect = """1234567"""
    	self.assertTrue(TestCodeGen.test(input,expect,554))
	
    def test_55(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			a:=0;
			while a < 10 do
			begin
				a:=a+1;
				if (a > 2) and (a < 7) then continue;
				else
				putInt(a);
			end
        end
		
		"""
    	expect = """1278910"""
    	self.assertTrue(TestCodeGen.test(input,expect,555))
	
    def test_56(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			a:=0;
			while a < 10 do
			begin
				a:=a+1;
				if  (a > 7) then break;
				else
				putInt(a);
			end
        end
		
		"""
    	expect = """1234567"""
    	self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_57(self):
    	input = """
		procedure main();
		var a ,b,c: real;
		begin
			a:=b:=c:=3;
			putFloat(a+b+c);
        end
		
		"""
    	expect = """9.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,557))
	
    def test_58(self):
    	input = """
		procedure notmain();
		begin
			
		end
		procedure main();
		var a ,b,c: real;
		begin
			notmain();
			a:=b:=c:=3;
			putFloat(a+b+c);
        end
		
		"""
    	expect = """9.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_59(self):
    	input = """
		procedure main();
                    var a,b : integer;
                    Begin
						a:=b:=1;
                        if (a=b) then begin
                            a:=a+1;
                            b:=b+1;
                        end
                        else a:=b;
						putint(a);
						putint(b);
                    end
		
		"""
    	expect = """22"""
    	self.assertTrue(TestCodeGen.test(input,expect,559))
    def test_60(self):
    	input = """
		procedure notmain(i : integer);
		begin
			putIntln(i);
		end
		procedure main();
                    var a,b,c,d : integer;
                    Begin
						a:=2;
						b:=1;
                        if (a=b) then notMain(2);
                        else begin 
                            a:=b;
                            c:=d:=1;
							notMain(a);
							notMain(c);
                        end
                    end
		"""
    	expect = """1\n1\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_61(self):
    	input = """
		procedure notmain(i : integer);
		begin
			putIntln(i);
		end
		procedure main();
                    var a,b,c,d : integer;
                    Begin
						a:=2;
						b:=2;
                        if (a=b) then 
						begin
							a:=b*100 div 8;
							notMain(a);
							notMain(b);
						end
                        else begin 
                            a:=b;
                            c:=d:=1;
							notMain(a);
							notMain(c);
                        end
                    end
		"""
    	expect = """25\n2\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_62(self):
    	input = """
		procedure main();
                    var a : Boolean ;
                    Begin
						a := trUe;
                        if true then
                        if false then a:=true;
                        else a:=NoT True;
						putBoolLn(a);
                    end
		"""
    	expect = """false\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_63(self):
    	input = """
		var i : real;
			n: integer;
		procedure main();
                    Begin
						n:=40;
						i:=1;
                        while i<n do i := i+ I;
						putFloatln(i);
                    end
		"""
    	expect = """64.0\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,563))
    def test_64(self):
    	input = """
		var n : real;
		procedure main();
		var i:integer;
                    Begin
						n:=10.0;
						i:=1;
                        while i<n do 
                        begin 
                            putint(i);
                            i := i+ 1;
                        end
                    end
		"""
    	expect = """123456789"""
    	self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_65(self):
    	input = """
		procedure main();
		var i,n:integer;
                    Begin
						i:=0;
						n:=10;
                        while i<=n do 
                        begin 
                            if i mod 2 = 0 then
                            putInt(i);
                            i := i+1;
                        end
                    end
		"""
    	expect = """0246810"""
    	self.assertTrue(TestCodeGen.test(input,expect,565))
    def test_66(self):
    	input = """
		procedure main();
		var a,b:real;
            Begin
				a:=1;
				b:=2;
                if a>b then 
                    while a<5 do a:=a+1;
                else while b<5 do b:=b+1;
				putFloat(a);
				putFloat(b);
            end
		"""
    	expect = """1.05.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,566))
    def test_67(self):
    	input = """
		procedure main();
		var a : integer;
            Begin
			a:=4;           
                while a<5 do if a>3 then begin putint(4); a:=10;end else putint(123);
            end
		"""
    	expect = """4"""
    	self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_68(self):
    	input = """
		procedure notmain(i,j : integer);
		begin
			putint(i*j);
		end
		procedure main();
		var i,n : integer;
                    Begin
						n:=-3;
                        for i := 1 downto n do begin
                            notmain(i,i);
                        end
                    end
		"""
    	expect = """10149"""
    	self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_69(self):
    	input = """
		procedure notmain(i,j : integer);
		begin
			putint(i*j);
		end
		procedure main();
		var i,n : integer;
                Begin
					n :=3;
                    if n>5 then
                    for i := 1 to n do
                        notmain(i,i);
                    else for i := 10 downto n do
                        notmain(i,i);
                end
		"""
    	expect = """1008164493625169"""
    	self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_70(self):
    	input = """
		procedure notmain(i,j : integer);
		begin
			putint(i*j);
		end
		procedure main();
		var i,n : integer;
                    Begin
						n:=2;
                        while n>0 do begin
                        for i := 1 to n do
                            notmain(i,i);
						n:=n-1; end
                    end
		"""
    	expect = """141"""
    	self.assertTrue(TestCodeGen.test(input,expect,570))
    def test_71(self):
    	input = """
		procedure notmain(i,j : integer);
		begin
			putint(i*j);
		end
		procedure main();
		var a,i,n : integer;
                    Begin
						a:=n:=1;
                        for i := 1 to n do
                            while(a=a)do
							begin
                            	notmain(i,i);
								break;
							end
                    end
		"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_72(self):
    	input = """
		procedure notmain(i,j : integer);
		begin
			putint(i*j);
		end
		procedure main();
		var i,n:integer;
                    Begin
						i:=n:=5;
                        for i := -1 to n+1 do
                            
                            notmain(i,1);
                    end
		"""
    	expect = """-10123456"""
    	self.assertTrue(TestCodeGen.test(input,expect,572))
    def test_73(self):
    	input = """
		procedure main();
		var n,m,i : integer;
                Begin
					n:=3;
					m:=1;
                    for i := -n to -m do begin
                        if (i>-2) then begin
                        putint(-i);
						brEak;
						end
                        else begin putint(i);ConTiNue; end
                    EnD
	            end
		"""
    	expect = """-3-21"""
    	self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_74(self):
    	input = """
		procedure main();
                    Begin
                        return;
                    end
		"""
    	expect = """"""
    	self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_75(self):
    	input = """
		function foo(i : integer):integer;
                    Begin
						if i=0 then return 0;
                        return foo(i-1) + i;
                    end
		procedure main();
                    Begin
						putInt(foo(2+2+2+2+2));
                        return;
                    end
		"""
    	expect = """55"""
    	self.assertTrue(TestCodeGen.test(input,expect,575))
    def test_76(self):
    	input = """
		function foo(a,b:real;c:boolean):boolean;
                    Begin
                        return (A>=b) and c;
                    end
		procedure main();
                    Begin
						putBool(foo(1+1,1.0+0.1,true));
						putBool(foo(1+1,1.0+0.1,not true));
                        return;
                    end
		"""
    	expect = """truefalse"""
    	self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_77(self):
    	input = """
		function foo(a,b:real;c:boolean):real;
                    Begin
						if c then
                        return (A - b);
						else return a+B;
                    end
		procedure main();
                    Begin
						putFloat(foo(1+1,1.0+0.1,true));
						putFloat(foo(1+1,1.0+0.1,not true));
                        return;
                    end
		"""
    	expect = """0.93.1"""
    	self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_78(self):
    	input = """
		procedure main();
            Begin
                putString("hello world !!!");
            end
		"""
    	expect = """hello world !!!"""
    	self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_79(self):
    	input = """
		procedure main();
                Begin
                    with a,b:integer; do
                    begin
						b:=2;
                        a:=b+5;
                        putint(a);
                        putint(A+b);
                    end
                end
		"""
    	expect = """79"""
    	self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_80(self):
    	input = """
		procedure main();
                    Begin
                        with a,b:integer; do
						begin
							b:=1080;
							a:=b mOD 1000;
                        	if true then
							putint(a);
						end
                    end
		"""
    	expect = """80"""
    	self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_81(self):
    	input = """
		procedure main();
                    Begin
                    if true then 
                        with a_:string;a,b:integer; do putint(1);
                    else with _a:string;a,b:integer; do putint(2);
                    end
		"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_82(self):
    	input = """
		procedure main();
		var i:integer;
                    Begin
                    for i:= 2 to 3 do
                        with a,b:integer; do 
						begin
							b:=i;
							a:=b*b;
							putint(a);
						end
                    end
		"""
    	expect = """49"""
    	self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_83(self):
    	input = """
		procedure main();
                    Begin
                        with i,b:integer; do 
						for i:= 7 to 9 do putint(i);
                    end
		"""
    	expect = """789"""
    	self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_84(self):
    	input = """
		procedure main();
                    Begin
                        with n:integer; do begin
							n:=7 ;

                        	while (n>=7) and (n<=9) do begin putint(n); n:=n+1; end
						end
                    end
		"""
    	expect = """789"""
    	self.assertTrue(TestCodeGen.test(input,expect,584))
	
    def test_85(self):
    	input = """
		procedure main();
		var n : integer;
                    Begin
						n:=7 ;

                        	while (n>=7) and (n<=9) do begin
                        with n:integer; do begin
							n:=9;
							begin putint(n); n:=n+1; end
						end n:=n+1; end
                    end
		"""
    	expect = """999"""
    	self.assertTrue(TestCodeGen.test(input,expect,585))
    def test_86(self):
    	input = """
		procedure main();
                    Begin
                        begin
                        end
                    end
		"""
    	expect = """"""
    	self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_87(self):
    	input = """
		function gt(i : integer): integer;
        begin
            if i <= 1 then return 1;
            else
            retuRn i*gt(i-1);
        end
		procedure main();
		var a:integer;
                    Begin
						a:=10;
                        putint(gt(a));
                    end
		"""
    	expect = """3628800"""
    	self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_88(self):
    	input = """
		procedure main();
        var i,n :integer;
        begin
            n:=10;
			putStringln("so le < 10 la:");
            for i:=0 to n do if not (i mod 2 = 0) then begin putint(i); putString(" "); end
        end
		"""
    	expect = """so le < 10 la:\n1 3 5 7 9 """
    	self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_89(self):
    	input = """
		function cv(a,b : real):real;
        begin
            return a+a+b+b;
        end
        procedure main();
        var a,b :real;
        begin
            a:=12;
			b:=0.01;
			putString("cv hcn la: ");
            putFloat(cv(a,b));
        end
		"""
    	expect = """cv hcn la: 24.02"""
    	self.assertTrue(TestCodeGen.test(input,expect,589))
    def test_90(self):
    	input = """
		procedure main();
        var a,b :integer;
        begin
            a:=1;
			b:=2;
            if a=b then putFloat(1);
            else putFloat(a/b);
			putFloat(1);
        end
		"""
    	expect = """0.51.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,590))
    def test_91(self):
    	input = """
		Function UCLN(a,b:integer):integer;
        begin
            if a mod b = 0 then return b;
            else return UCLN(b,(a mod b));
        end
		procedure main();
        var a,b :integer;
        begin
            a:=123;
			b:=321;
            
			putINT(UCLN(b,a));
        end
		"""
    	expect = """3"""
    	self.assertTrue(TestCodeGen.test(input,expect,591))
    def test_92(self):
    	input = """
		Function sum(n:integer):integer;
        var sum :integer;
        begin
			sum:=0;
            with i:integer; do
            for i:= 0 to n do sum := sum + i;
            return sum; 
        end
		procedure main();
        var a :integer;
        begin
            a:=123;
            
			putINT(SUM(a));
        end
		"""
    	expect = """7626"""
    	self.assertTrue(TestCodeGen.test(input,expect,592))
    def test_93(self):
    	input = """
		procedure main();
        var a,b :real;
        begin
            a:=b:=10000.01;
            if a= 0 then putString("ptvn");
            else putFloat(-b/a);
			a:=b:=0;
            if a= 0 then putString("ptvn");
            else putFloat(-b/a);
        end
		"""
    	expect = """-1.0ptvn"""
    	self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_94(self):
    	input = """
		Function tbc(n:integer):real;
        var sum :integer;
        begin
			sum:=0;
            with i:integer; do
            for i:= 0 to n do sum := sum + i;
            return sum/n; 
        end
		procedure main();
        var a,b :real;
        begin
            
            putFloat(tbc(10));
        end
		"""
    	expect = """5.5"""
    	self.assertTrue(TestCodeGen.test(input,expect,594))
    def test_95(self):
    	input = """
		var i :integer;
        function f (): integer;
        begin 
            return 200;
        end
        procedure main();
        var 
        main: integer; 
        begin 
            main := f (); 
            putIntLn(main); 
            with i :integer; 
            main:integer; 
            f :integer;
            do begin  
                main := f := i := 100; 
                putIntLn( i ); 
                putIntLn(main); 
                putIntLn(f ); 
            end  
            putIntLn(main);  
        end 
        var g: real ;
		"""
    	expect = """200\n100\n100\n100\n200\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,595))
    def test_96(self):
    	input = """
		
        procedure main();
		Var 
            i,j : integer;
        BEGIN
              
             FOR i:= 1 TO 10 DO
             Begin
              FOR j:=1 TO i DO putString("*");
			  PutLN();
            End
        END
		"""
    	expect = """*
**
***
****
*****
******
*******
********
*********
**********
"""
    	self.assertTrue(TestCodeGen.test(input,expect,596))
    def test_97(self):
    	input = """
		
        procedure main();
		Var 
            i,j : integer;
        BEGIN
              
            i:=10;
            FOR j:=1 TO i DO 
			with i :integer; do
			begin putString("*");
			break;
			end
			
            
        END
		"""
    	expect = """*"""
    	self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_98(self):
    	input = """
		
        procedure main();
		Var 
            i,j : integer;
        BEGIN
              
            i:=10;
            FOR j:=1 TO i DO 
			while (j <> i) do
			begin putString("*");
			break;
			end
			
            
        END
		"""
    	expect = """*********"""
    	self.assertTrue(TestCodeGen.test(input,expect,598))
    def test_99(self):
    	input = """
        procedure main();
        BEGIN
            notmain("*********");
        END
		procedure notmain(a:string);
		begin
			putString(a);
		end
		"""
    	expect = """*********"""
    	self.assertTrue(TestCodeGen.test(input,expect,599))
    