import unittest
from TestUtils import TestCodeGen
from AST import *

#Nguyen Hoai Danh - 1610391
class CheckCodeGenSuite(unittest.TestCase):
    def test_int1(self):
        
        input = """
        var a: integer;c: real;
        procedure main(); 
        var c: real;
        begin putInt(-100); end
        procedure main1(d,e,f:real); 
        var c: real;
        begin  end
      
        """
        expect = "-100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast2(self):
    	input = Program([
    		FuncDecl(Id("main"),[],[],[
    			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_float3(self):
        
        input = """procedure main(); begin putFloat(100.3); end"""
        expect = "100.3"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_bool4(self):
        
        input = """procedure main(); begin putBool(TRUE); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_string5(self):
        
        input = """procedure main(); begin PUTSTRINGLN("hello"); end"""
        expect = "hello\n"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test6(self):
        
        input = """procedure main(); begin putInt(1); end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test7(self):
        
        input = """procedure main(); begin putInt(1+2); end"""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test8(self):
        
        input = """procedure main(); begin putInt(1-2); end"""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test9(self):
        
        input = """procedure main(); begin putInt(-1-2); end"""
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test10(self):
        
        input = """procedure main(); begin putfloat(-1.2-2.2); end"""
        expect = "-3.4"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test11(self):
        
        input = """procedure main(); begin putfloat(4-1.5-0.5); end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))
  
    def test13(self):
        
        input = """procedure main(); begin putfloat(4/2); end"""
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test14(self):
        
        input = """procedure main(); begin putint(4 div 2); end"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    
    def test15(self):
        
        input = """procedure main(); begin putint(4 mod 2); end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test12(self):
        
        input = """procedure main(); begin putBool(true or true); end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test16(self):
        
        input = """procedure main(); begin putBool((true or true) and then false); end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,515))
    
    def test18(self):
        
        input = """procedure main(); begin putfloat(-1.2--1.2); end"""
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test17(self):
        
        input = """procedure main(); begin putBool( not not  ((true or true) and then false) ); end"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))
    def test18(self):
        
        input = """var c: boolean;
        procedure main(); 
        begin 
        c:=true;
        putBool(c); 
        end"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test19(self):
        
        input = """var c: real;
        procedure main(); 
        begin 
        c:=1;
        putfloat(c/c); 
        end"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test20(self):
        
        input = """var c,d: real;
        function aaa():integer;
        begin return 4; 
        end
        procedure main(); 
        begin 
        c:=1+3;
        d:=aaa();
        putfloat(d/aaa()); 
        end"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test21(self):
        
        input = """var c,d: real;
        function aaa():string;
        begin return "4"; 
        end
        procedure main(); 
        begin 
        c:=1+3;
        putstring(aaa()); 
        end"""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test22(self):
        
        input = """var c,d: real;
        function aaa():integer;
        begin return 4; 
        end
        procedure main(); 
        begin 
        c:=1+3;
        d:=c:=aaa();
        putfloat(d/aaa()); 
        end"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test23(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        d:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            end
        putint(c);
        end"""
        expect = "6"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test24(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        d:=9;
        c:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            end
        putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    
    
    
    def test26(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:integer;
        begin 
        d:=0;
        c:=0;
        for i:=0 to 0 do 
            begin 
            c:=c+i;
           
            end
        putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    
    def test26(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=0;
        while d<=3 do 
            begin 
            c:=c+d;
            d:=d+1;
            break;
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test27(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=2;
        while d<=3 do 
            begin 
            break;
            c:=c+d;
            d:=d+1;
            break;
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test27(self):
        
        input = """var c,d: integer;
        procedure main(); 
        var i:real;
        begin 
        c:=7;
        d:=2;
        while d<=3 do 
            begin 
            d:=d+1;
            continue;
            
            end
        putint(c);
        end"""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test28(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        if d<c then 
        putint(d); else putint(c);
        end"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test29(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        if d<c then c:=c+1; else c:=c-1-2;
        putint(c);
        end"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test30(self):
        
        input = """var d,c: integer;
        procedure main(); 
        begin 
        d:=2; c:=9;
        while d<>0 do
        begin
        if d<c then c:=c+1; else c:=c-1-2;
        d:=d-1;
        end
        putint(c);
        end"""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,531))
    def test31(self):
        
        input = """
        var d,a: integer;
        function aaa(x:real;y:real): real;
        begin  
            return 2.0; 
        end
        var c:real;
        procedure main1(c:real);
        begin end
        procedure main(); 
        var a:real;
        begin 
        main1(2.0);
        a:=2; c:=2;
        with a:integer; do begin a:=4;  with a:real ; do begin a:=3;  end end
        a:=aaa(2.0,2.0);
        putfloat(2.0);
        end

        
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test32(self):
        
        input = """
        procedure main(); 
        begin 
            putLN();
        end
        """
        expect = "\n"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    def test33(self):
        
        input = """
        procedure main(); 
        begin 
            putfloat(-1e2);
        end
        """
        expect = "-100.0"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test34(self):
        
        input = """
        procedure main(); 
        var r:real;
        begin 
            r:=0+12345-12345.0;
            putfloat(r);
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test35(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       
        begin 
            putstringln(a());
        end
        """
        expect = "helo\n"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test36(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       
        begin 
             putInt(2+1);
        end
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test37(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       
        begin 
             putInt(111*111);
        end
        """
        expect=str(111*111)
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test38(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       
        begin 
             putfloat(121/11);
        end
        """
        expect=str(11.0)
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test39(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       
        begin 
             putInt(12 mod 11);
        end
        """
        expect=str(1)
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    def test41(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       var    a:integer;
        begin 
        a:=1;
             putInt(a-1);
        end
        """
        expect=str(0)
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test42(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       var    a,b:integer;
        begin 
        a:=1; b:=-10;
             putInt(a+b);
        end
        """
        expect=str(-9)
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test43(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
       var    a,b:integer;
        begin 
        a:=1; b:=-10;
             putbool(a-21>b);
        end
        """
        expect="false"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test44(self):
        
        input = """
        function a():real; begin return 1; end
        function b():real; begin return 2; end
        procedure main(); 
       
        begin 
      
             putfloat(a()+b());
        end
        """
        expect="3.0"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test45(self):
        
        input = """
        function a():real; begin return 1; end
        function b():real; begin return 2; end
        procedure main(); 
       
        begin 
      
             putbool(a()=b());
        end
        """
        expect="false"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test46(self):
        
        input = """
        function a():real; begin return 1; end
        function b():real; begin return 2; end
        procedure main(); 
       
        begin 
      
             putBool(33.33=33.33);
        end
        """
        expect="true"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test47(self):
        
        input = """
        function a():real; begin return 1; end
        function b():real; begin return 2; end
        procedure main(); 
       
        begin 
      
             putBool(33.33<>33.33);
        end
        """
        expect="false"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test48(self):
        
        input = """
        var i : integer ;
        function f (): integer ;
        begin
            return 200;
        end
        procedure main ();
        var
             main : integer ;
        begin
            main := f ();
            putIntLn(main );
            with
            i : integer ;
            main : integer ;
            f : integer ;
            do 
            begin
                main := f := i := 100;
                putIntLn( i );
                putIntLn(main );
                putIntLn( f );
            end
            putIntLn(main );
        end
        var g : real ;
        """
        expect="200\n100\n100\n100\n200\n"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test49(self):
        
        input = """
        procedure main(); 
        var a:integer;
        begin 
             
          a := 3;
           putInt(a); a := a + 1; while (a < 6) do begin putInt(a); a := a + 1; end
        end
        """
        expect="345"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    

    def test51(self):
        
        input = """
        function isPrime(n:integer):boolean;
        var a,b,i:integer;
        begin  
            i:=1;
            
          return true;
        end
        procedure main(); 
        var a:integer;
        begin 
             
          if (isPrime(11)) then putStringLn("Is Prime!");
          else putStringLn("Is Not Prime!");
        end
        """
        expect="Is Prime!\n"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test52(self):
        
        input = """
        function isPrime(n:integer):boolean;
        var a,b,i:integer;
        begin  
            i:=1;
            
          return true;
        end
        procedure main(); 
        var a:integer;
        begin 
           a := 1;
      if (a >= 0) then
        if (a > 5) then putString("lon hon 5");
        else putString("be hon 5 lon hon -1");
      else 
        if (a < -5) then  putString("be hon -5");
        else putString("lon hon -5 be hon 0");  
        end
        """
        expect="be hon 5 lon hon -1"
        self.assertTrue(TestCodeGen.test(input,expect,553))
    def test53(self):
        
        input = """
        function isPrime(n:integer):boolean;
        var a,b,i:integer;
        begin  
            i:=1;
            
          return true;
        end
        procedure main(); 
        var a:integer;
        begin 
         a := --(-1 + 2 * -4 + 6);
      if (a >= 0)then
        if (a > 5)then putString("lon hon 5");
        else putString("be hon 5 lon hon -1");
      else 
        if (a < -5)then putString("be hon -5");
        else putString("lon hon -5 be hon 0");  
        end
        """
        expect="lon hon -5 be hon 0"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test54(self):
        
        input = """
        function foo(n:integer):boolean;
        var a,b,i:integer;
        begin  
            begin begin end begin begin begin return true; end end end end
          
        end
        procedure main(); 
        var a:integer;
        begin 
        
            putbool(foo(1));
        end
        """
        expect="true"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    def test55(self):
        
        input = """
       
        procedure main(); 
        var b:integer;
        begin 
        b:=1;
        while(true) do begin b := 2; break; end
        putIntLn(b);
        end
        """
        expect="2\n"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test56(self):
        
        input = """
        function giaithua(n:integer):integer;
        begin
            if n=1 then return 1;
            return 2; 
        end
        procedure main(); 
        begin 
            putint(giaithua(3));
            
        end
        """
        expect="2"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test51(self):
        
        input = """
       
        procedure main(); 
        var a:integer;
        begin 
        putbool(true);
              return;  
        
        end
        """
        expect="true"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test25(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
         for i:=c+1 to 3 do 
        begin 
        putint(i);
        end
        for i:=3 downto c +1 do 
        begin 
        putint(i);
        end
        
        end"""
        expect = "123321"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test50(self):
        
        input = """
        function foo(n:integer):integer;
        var a,b:integer;
        begin  a:=12;
                b:=12;
                
                if(n>1)
                    then return n* foo(n-1);
                else      return 1;  
                return 2;
        end
        procedure main(); 
        var i:integer;
        begin 
          putint(foo(3));
          
        end
        """
        expect="6"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test57(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        
        for i:=9 downto 1 do 
        begin 
        
        putint(i);
        end
        
        end"""
        expect = "987654321"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    def test58(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if i mod 2 =0 then putint(i);
        end
        end"""
        expect = "8642"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test59(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i div 2)mod 2 =0 then putint(i);
        end
        end"""
        expect = "98541"
        self.assertTrue(TestCodeGen.test(input,expect,559))
    def test60(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i =3) then continue;
            putint(i);
        end
        end"""
        expect = "98765421"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test61(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=0;
        for i:=9 downto 1 do 
        begin 
            if (i =3) then break;
            putint(i);
        end
        end"""
        expect = "987654"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test62(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            c:=c*2;
            
        end putint(c);
        end"""
        expect = "512"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test63(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            c:=c-1;c:=c+1;
           c  := --------c * 2;
        end putint(c);
        end"""
        expect = "512"
        self.assertTrue(TestCodeGen.test(input,expect,563))
    def test64(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
           if i mod 2 =0 then c:=c+1;
           else c:=c-1;
        end putint(c);
        end"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test65(self):
        
        input = """var c: integer;
        procedure main(); 
        var i:integer;
        begin 
        i:=1;c:=1;
        for i:=1 to 9 do 
        begin 
            while i<>9 do begin i:=9; with a:integer; do putint(c); end
        end 
        
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test66(self):
        
        input = """
        procedure main(); 
        begin 
        end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,566))
    def test67(self):
        
        input = """
        procedure main(); 
        begin 
            if  true then 
                if true then putint(1);
                else  putint(2);
            else  putint(3);
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test68(self):
        
        input = """
        procedure main1(); 
        begin 
            if  true then 
               return;
            else  return;
        end
        procedure main(); 
        begin 
        main1();
            if  true then 
               return;
            else  return;
        end"""
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test69(self):
        
        input = """
        procedure main2(); 
        begin 
          
               return;
           
        end
        function main1():integer; 
        begin 
            if  true then 
               return 1;
            else  
            return 2;
            
        end
        procedure main(); 
        begin 
        main2();
            if  not true then 
               return;
            else  
            putint(main1());
        end"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test70(self):
        
        input = """
        procedure main(); 
        var i,j:integer;
        begin 
        i:=7; j:=2;
            putfloatln(9/3.0);
             putfloatln(9.0/3.0);
             putfloatln(9.0/3);
            putfloatln(6/3+ 1.5/3);
             putfloatln(i /(j+5));
        end"""
        expect = "3.0\n3.0\n3.0\n2.5\n1.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    def test40(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure main(); 
        begin 
             putfloat(1+2*3-1/1);
        end
        """
        expect=str(6.0)
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test71(self):
        
        input = """
        function a():string; begin return "helo"; end
        procedure foo(a : integer);
        begin
        a:=123;
        end
     
        procedure main(); 
        var a:integer;
        begin 
            
            a:=1;
        foo(a);
        putINT(a);
             
        end
        """
        expect="1"
        self.assertTrue(TestCodeGen.test(input,expect,571))
    def test_72(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,572))
	
    def test_73(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,573))
	
    def test_54(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,574))
	
    def test_75(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,575))
	
    def test_76(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,576))
	
    def test_77(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_78(self):
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
    	self.assertTrue(TestCodeGen.test(input,expect,578))
	
    def test_79(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=1 to 10 do
				putInt(a);
        end
		
		"""
    	expect = """12345678910"""
    	self.assertTrue(TestCodeGen.test(input,expect,579))
	
    def test_80(self):
    	input = """
		procedure main();
		var a ,b: integer;
		begin
			for a:=10 downto 1 do
				putInt(a);
        end
		
		"""
    	expect = """10987654321"""
    	self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_81(self):
    	input = """
        function fibonacy(n : integer):integer;
        begin
        
        if (n<=1)  then return n;
        else return fibonacy(n-1)+fibonacy(n-2);
        end
		procedure main();
		var a ,b: integer;
		begin
			
				putInt(fibonacy(21));
        end
		
		"""
    	expect = """10946"""
    	self.assertTrue(TestCodeGen.test(input,expect,581))    
    def test_82(self):
    	input = """
        
		procedure main();
		var a ,b: integer; out:boolean;
		begin
			out:=false;
				while not out do begin
                      
                      for a:=1 downto -10 do
                        begin   
                        putint(a);
                        if a=-5 then begin out:=true; break; end
                        end
                

                end
        end
		
		"""
    	expect = """10-1-2-3-4-5"""
    	self.assertTrue(TestCodeGen.test(input,expect,582))    
    def test_83(self):
    	input = """
        
		procedure main();
		var a ,b,c: integer; out:boolean;
		begin
			    
           
              for b:=1 downto 0 do        
                 for c:=10 downto 0 do         
                    putint(c);
        end
		
		"""
    	expect = """109876543210109876543210"""
    	self.assertTrue(TestCodeGen.test(input,expect,583))   
    def test_84(self):
    	input = """
        var a ,b,c: integer; out:boolean;
		procedure main();
		
		begin
        a:=1;
			  with a ,b,c: integer; do 
              begin a:=2; with a ,b,c: integer; do begin a:=3; putint(a);end end
        end
		
		"""
    	expect = """3"""
    	self.assertTrue(TestCodeGen.test(input,expect,584)) 
    def test_85(self):
    	input = """
        var a ,b,c: integer; out:boolean;
		procedure main();
		 var a ,b,c: integer; out:boolean;
		begin
        a:=1;
                for b:=1 to 3 do
			  with a ,b,c: integer; do 
              begin a:=2; b:=3; putint(a+b); end
        end
		
		"""
    	expect = """555"""
    	self.assertTrue(TestCodeGen.test(input,expect,585)) 
    def test_86(self):
    	input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin return 1.2;return 1.3; end
        procedure main();
		begin
                c:=a:=foo(1)+foo(foo(foo(foo(foo(1)))));
                putfloatln(c/2);putFloatln(a/2);
        end
		
		"""
    	expect = """1.2\n1.2\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,586)) 
    def test_87(self):
    	input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin
                c:=1;
                if c<>3 then 
                    if c<0 then 
                    putfloatln(c/2);
                    else c:=foo(0);
                putfloatln(c);
        end
		
		"""
    	expect = """1.3\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,587)) 
    def test_88(self):
    	input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin c:=0;
               while true do begin c:=3; if c=3 then break; else continue; end
                if c<>3 then begin end
                else while c=3 do begin putfloat(c);c:=c-1; break; end
        end
		
		"""
    	expect = """3.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,588)) 
    def test_89(self):
    	input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin   c:=foo(1------------------------------------3);
               putfloatLN(c/c); 
                return;

        end
		
		"""
    	expect = """1.0\n"""
    	self.assertTrue(TestCodeGen.test(input,expect,589)) 
    def test_90(self):
    	input = """
        var a ,b,c: real; out:boolean;
		function foo(c:integer): boolean;
        begin if c mod 2 =0 then return TRUE; else return FaLSE; end
        procedure main();
		begin   out:=foo(1024);
               if out then putstring("so chan");

            else putstring("so 0 chan");
        end
		
		"""
    	expect = """so chan"""
    	self.assertTrue(TestCodeGen.test(input,expect,590)) 
    def test_91(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                putfloat(1/2/2);
        end
		
		"""
    	expect = """0.25"""
    	self.assertTrue(TestCodeGen.test(input,expect,591)) 
    def test_92(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                c:=1.2/2.4; 
                b:=1;
                while true do
                begin putfloat(c+0.5); b:=b+1; if b=4 then break; end
        end
		
		"""
    	expect = """1.01.01.0"""
    	self.assertTrue(TestCodeGen.test(input,expect,592)) 
    def test_93(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure MAIN();
		begin  
               putstring("test");
                     return;
        end   
		
		"""
    	expect = """test"""
    	self.assertTrue(TestCodeGen.test(input,expect,593)) 
    def test_94(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                     return;
        end   
		procedure main1();
		begin  
                 putint(123);
                     return;
        end
        procedure main2();
		begin  
                 putint(1234);
                     return;
        end
		"""
    	expect = """1231234"""
    	self.assertTrue(TestCodeGen.test(input,expect,594)) 

    def test_95(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                 putint(1);
                     return;
        end   
		procedure main1();
		begin  
                 while false do
                     return;
        end
        procedure main2();
		begin  
                
                     return;
        end
		"""
    	expect = """1"""
    	self.assertTrue(TestCodeGen.test(input,expect,595)) 

    def test_96(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                 putbool(true);
                     return;
        end   
		procedure main1();
        var i:integer;
		begin  
                for i:=1 to 10 do
                     return;
        end
        procedure main2();
		begin  
                 
                     return;
        end
		"""
    	expect = """true"""
    	self.assertTrue(TestCodeGen.test(input,expect,596)) 

    def test_97(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
               if true then
                     return;
        end   
	
		"""
    	expect = """"""
    	self.assertTrue(TestCodeGen.test(input,expect,597)) 

    def test_98(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
        c:=400;
                if c=400/1 then putstring("chia het cho 4");
                  else if c = 200 then    return;
        end   
		
		"""
    	expect = """chia het cho 4"""
    	self.assertTrue(TestCodeGen.test(input,expect,598)) 
    def test_99(self):
    	input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                     return;
        end   
		procedure main1();
		begin  
                 putint(123);
                     return;
        end
        procedure main2();
		begin  
                 putint(1234);
                     return;
        end
		"""
    	expect = """1231234"""
    	self.assertTrue(TestCodeGen.test(input,expect,599)) 

    def test_100(self):
    	input = """
        
		function foo(a:real):boolean;
        begin putint(2); return true; end
        function foo1():boolean;
        begin putfloat(2/0); return true; end
        procedure MAIN();
		begin  
        
             if true or  foo(1) then begin   end
             if true or else  foo(1) then begin   end
             if false and  foo(1) then begin   end
             if false and then   foo(1) then begin   end

            if false and then foo1()  then begin   end
            if 1>2 then putstring("xong");
             if 1.0>2.3 then putstring("roi");
              if 1>2.8 then putstring("nha");
               if 1.21>2 then putstring("may");
                if 1.212122>1.2121223 then putstring("may");
               putstring("xong");
        end   
		
		"""
    	expect = "22xong"
    	self.assertTrue(TestCodeGen.test(input,expect,600)) 