'''
*   Author: NGUYEN MINH THAM
*   MSSV: 1613166
*	Version: 1:49 30/11/2018 (v2.0)
'''

import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

    def test_binary_expression_1(self):
        """test binary: + --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putFloatLn(10.0 + 2); // float + int
                    putIntLn(10 + 2); // int + int
                    putFloatLn(10.0 + 2.0); // float + float
                    putFloat(10 + 2.0); // int + float

                END
            """
        expect = "12.0\n12\n12.0\n12.0"
        self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_binary_expression_2(self):
        """test binary: -  --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putFloatLn(10.0 - 2); // float + int
                    putIntLn(10 - 2); // int + int
                    putFloatLn(10.0 - 2.0); // float + float
                    putFloat(10 - 2.0); // int + float                
                END
            """
        expect = "8.0\n8\n8.0\n8.0"
        self.assertTrue(TestCodeGen.test(input,expect,502))


    def test_binary_expression_3(self):
        """test binary: * --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putFloatLn(10.0 * 2); 
                    putFloatLn(10.0 * 2.0); 
                    putIntLn(10 * 2); 
                    putFloat(10 * 2.0); 
                END
            """
        expect = "20.0\n20.0\n20\n20.0"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_binary_expression_4(self):
        """test binary: / --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    putFloatLn(11 / 2.0); 
                    putFloatLn(11.0 / 2.0); 
                    putFloatLn(11.0 / 2); 
                    putFloat(11 / 2); 
                END
            """
        expect = "5.5\n5.5\n5.5\n5.5"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_binary_expression_5(self):
        """test binary: / --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putFloat(10 / 2); 
                END
            """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_binary_expression_6(self):
        """test binary: div --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putIntLn(9 DIV 2); 
                    putIntLn(19 DIV 2); 
                    putIntLn(10 DIV 2); 
                    putIntLn(21 DIV 2); 
                END
            """
        expect = "4\n9\n5\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_binary_expression_7(self):
        """test binary: mod --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putIntLn(9 MOD 2); 
                    putIntLn(12 MOD 2); 
                    putInt(4 MOD 5);                     
                END
            """
        expect = "1\n0\n4"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_binary_expression_8(self):
        """test binary: and --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if (9 > 4) and (5 > 6) then
                        putString("Then Statement");
                    else
                        putString("Minh Tham");
                END
            """
        expect = "Minh Tham"
        self.assertTrue(TestCodeGen.test(input,expect,508))     

    def test_binary_expression_9(self):
        """test binary: or --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if (9 > 4) or (5 > 6) then
                        putString("Tham");
                    else
                        putString("Minh Tham");
                END
            """
        expect = "Tham"
        self.assertTrue(TestCodeGen.test(input,expect,509))    

    def test_binary_expression_10(self):
        """test binary: > --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 > 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 > 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,510))   

    def test_binary_expression_11(self):
        """test binary: > --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 > 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 > 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,511))  

    def test_binary_expression_12(self):
        """test binary: >= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 >= 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 >= 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,512))   

    def test_binary_expression_13(self):
        """test binary: >= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 >= 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 >= 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,513))  

    def test_binary_expression_14(self):
        """test binary: < --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 < 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 < 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroELSE\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,514))   

    def test_binary_expression_15(self):
        """test binary: < --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 < 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 < 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroELSE\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,515))  

    def test_binary_expression_16(self):
        """test binary: <= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 <= 9 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 <= 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,516))   

    def test_binary_expression_17(self):
        """test binary: <= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 <= 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 <= 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroELSE\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,517))  

    def test_binary_expression_18(self):
        """test binary: <= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 = 9 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 = 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,518))   

    def test_binary_expression_19(self):
        """test binary: <= --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 = 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 = 9.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroELSE\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,519))  

    def test_binary_expression_20(self):
        """test binary: <> --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9 <> 9 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9.0 <> 10.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroELSE\nZeroTHEN"
        self.assertTrue(TestCodeGen.test(input,expect,520))   

    def test_binary_expression_21(self):
        """test binary: <> --ZERO--"""
        input = """
            PROCEDURE main(); 
                BEGIN 
                    if 9.0 <> 6 then
                        putStringLn("ZeroTHEN");
                    else
                        putStringLn("ZeroELSE");
                    if 9 <> 9.0 then
                        putString("ZeroTHEN");
                    else
                        putString("ZeroELSE");                        
                END
            """
        expect = "ZeroTHEN\nZeroELSE"
        self.assertTrue(TestCodeGen.test(input,expect,521))  

    def test_binary_expression_22(self):
        """test binary: and then --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 10;
                    if 5 < 2 and then 7 < 6 //expr1 fail and expr2 fail
                    then 
                        putIntLn(a);
                    else
                        putStringLn("Minh Tham");

                    if 5 > 2 and then 7 < 6 //expr1 true and expr2 fail
                    then 
                        putString("Minh Tham");                      
                    else
                        putInt(a);
                END
            """
        expect = "Minh Tham\n10"
        self.assertTrue(TestCodeGen.test(input,expect,522))     

    def test_binary_expression_23(self):
        """test binary: and then --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 10;
                    if 5 < 2 and then 7 > 6 //expr1 fail and expr2 true
                    then 
                        putIntLn(a);
                    else
                        putStringLn("Minh Tham");
                        
                    if 5 > 2 and then 7 > 6  //expr1 true and expr2 true
                    then 
                        putInt(a);
                    else
                        putStringLn("Minh Tham");                        
                END
            """
        expect = "Minh Tham\n10"
        self.assertTrue(TestCodeGen.test(input,expect,523))   

    def test_binary_expression_24(self):
        """test binary: and then --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 10;
                    if 5 < 2 or else 7 < 6 //expr1 fail and expr2 fail
                    then 
                        putIntLn(a);
                    else
                        putStringLn("Minh Tham");

                    if 5 > 2 or else 7 < 6 //expr1 true and expr2 fail
                    then 
                        putString("Minh Tham");                      
                    else
                        putInt(a);
                END
            """
        expect = "Minh Tham\nMinh Tham"
        self.assertTrue(TestCodeGen.test(input,expect,524))     

    def test_binary_expression_25(self):
        """test binary: and then --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 10;
                    if 5 < 2 or else 7 > 6 //expr1 fail and expr2 true
                    then 
                        putIntLn(a);
                    else
                        putStringLn("Minh Tham");
                        
                    if 5 > 2 or else 7 > 6  //expr1 true and expr2 true
                    then 
                        putInt(a);
                    else
                        putStringLn("Minh Tham");                        
                END
            """
        expect = "10\n10"
        self.assertTrue(TestCodeGen.test(input,expect,525)) 

    def test_unary_expression_1(self):
        """test unary: not --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : boolean;
                BEGIN 
                    a := true;
                    putBool(not a);
                    a := false;
                    putBool(not a);
                END
            """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,526))   

    def test_unary_expression_2(self):
        """test unary: - --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a :=  - 2;
                    putIntLn(a);
                    a := 3 + - 4;
                    putInt(a);
                END
            """
        expect = "-2\n-1"
        self.assertTrue(TestCodeGen.test(input,expect,527))  

    def test_type_coercions_1(self):
        """test type coercions: in assignment statement --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR real1 : real;
                BEGIN 
                    real1 :=  10.0;
                    putFloatLn(real1);
                    real1 :=  10;
                    putFloat(real1);
                END
            """
        expect = "10.0\n10.0"
        self.assertTrue(TestCodeGen.test(input,expect,528))  

    def test_type_coercions_2(self):
        """test type coercions: in call statement --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR real1 : real;
                BEGIN 
                    putFloatLn(10.0);
                    putFloat(10);
                END
            """
        expect = "10.0\n10.0"
        self.assertTrue(TestCodeGen.test(input,expect,529))  

    def test_type_coercions_3(self):
        """test type coercions: in call statement --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR int1 : integer;
                    real1 : integer;
                    real2 : integer;
                    int2 : integer;
                BEGIN 
                    int1 := 2;
                    real1 := 0;
                    real2 := 1;
                    int2 := 9;
                    callTest(int1, real1, "Chuc mung nam moi", real2, int2);
                END
            PROCEDURE callTest(int1: integer; real1: real; str1: string; real2: real; int2: integer);
                BEGIN   
                    putStringLn(str1);
                    putFloatLn(int1);
                    putFloatLn(real1);
                    putFloatLn(real2);
                    putFloat(int2);
                END
            """
        expect = "Chuc mung nam moi\n2.0\n0.0\n1.0\n9.0"
        self.assertTrue(TestCodeGen.test(input,expect,530))  

    def test_type_coercions_4(self):
        """test type coercions: in call expresion --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR int1 : integer;
                    real1 : integer;
                    real2 : integer;
                    int2 : integer;
                BEGIN 
                    int1 := 2;
                    real1 := 0;
                    real2 := 1;
                    int2 := 9;
                    int1 := callTest(int1, real1, "Chuc mung nam moi", real2, int2);
                END
            FUNCTION callTest(int1: integer; real1: real; str1: string; real2: real; int2: integer): integer;
                BEGIN   
                    putStringLn(str1);
                    putFloatLn(int1);
                    putFloatLn(real1);
                    putFloatLn(real2);
                    putFloat(int2);
                    return int1;
                END
            """
        expect = "Chuc mung nam moi\n2.0\n0.0\n1.0\n9.0"
        self.assertTrue(TestCodeGen.test(input,expect,531))  

    def test_type_coercions_5(self):
        """test type coercions: in return statement --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR real1 : real;
                BEGIN 
                    real1 := callTest(2019);
                    putStringLn("Chuc mung nam moi");
                    putFloat(real1);
                END
            FUNCTION callTest(int1: integer): real;
                BEGIN   
                    int1 := 2019;
                    return int1;
                END
            """
        expect = "Chuc mung nam moi\n2019.0"
        self.assertTrue(TestCodeGen.test(input,expect,532))  

    def test_push_constant_1(self):
        """test push constant onto the stack: push integer > (2^15 - 1) --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putInt(40000 + 50000); 
                END
            """
        expect = "90000"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_push_constant_2(self):
        """test push constant onto the stack: push integer > (2^15 - 1) --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putFloatLn(2.987654 + 1); 
                    putFloat(40000.987654 + 50000); 
                END
            """
        expect = "3.987654\n90000.984"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_var_decl_1(self):
        """test var declaration --ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    putStringLn("Toi ten la"); 
                    foo();
                END
            PROCEDURE foo(); 
                VAR a : integer;
                    b : real;
                BEGIN 
                    putString("Nguyen Minh Tham"); 
                END
            """
        expect = "Toi ten la\nNguyen Minh Tham"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_var_decl_2(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    r1 := 2018;
                    putInt(r1);
                END
            """
        expect = "2018"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_var_decl_3(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 2018;
                    putInt(a);
                END
            """
        expect = "2018"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_var_decl_4(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 2018;
                    WITH b : integer;
                    DO
                    BEGIN
                        b := a +  1;
                        putString("Chuc Mung Nam Moi ");
                        putInt(b);
                    END
                END
            """
        expect = """Chuc Mung Nam Moi 2019"""
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_var_decl_5(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    inName(2019);
                END
            PROCEDURE inName(b: integer); 
                BEGIN 
                    putString("Chuc Mung nam Moi ");
                    putInt(b); 
                END                
            """
        expect = """Chuc Mung nam Moi 2019"""
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_var_decl_6(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    gl1 := 2019;
                    inName(gl1);
                END
            var gl1: integer;
            PROCEDURE inName(b: real); 
                BEGIN 
                    putString("Chuc Mung nam Moi ");
                    putFloat(b); 
                END   
            var gl2: real;
            """
        expect = """Chuc Mung nam Moi 2019.0"""
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_var_decl_7(self):
        """test var declaration --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    gl1 := 2019;
                    gl2 := not false;
                    inName(gl1);
                END
            var gl1: integer;
            PROCEDURE inName(b: real); 
                BEGIN 
                    putString("Chuc Mung nam Moi ");
                    putFloatLn(b);
                    putBool(gl2); 
                END   
            var gl2: boolean;
            """
        expect = """Chuc Mung nam Moi 2019.0\ntrue"""
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_call_expr_1(self):
        """test call expression --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    putFloat(foo(2));
                END          
            FUNCTION foo(in1:integer):real;
            BEGIN
                return in1;
            END    
            """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_call_expr_2(self):
        """test call expression --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    putFloat(foo(2.2));
                END          
            FUNCTION foo(in1:real):real;
            BEGIN
                return in1*in1;
            END    
            """
        expect = """4.84"""
        self.assertTrue(TestCodeGen.test(input,expect,542))        

    def test_call_expr_3(self):
        """test call expression --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    putInt(foo(5));
                END          
            FUNCTION foo(in1:integer):integer;
            BEGIN
                putString("Minh Tham ");
                return in1*2;
            END    
            """
        expect = """Minh Tham 10"""
        self.assertTrue(TestCodeGen.test(input,expect,543))  

    def test_call_expr_4(self):
        """test call expression --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    putBool(foo(false));
                END          
            FUNCTION foo(in1:boolean):boolean;
            BEGIN
                putString("Minh Tham ");
                return not in1;
            END    
            """
        expect = """Minh Tham true"""
        self.assertTrue(TestCodeGen.test(input,expect,544))  

    def test_call_expr_5(self):
        """test call expression --ZERO--"""
        input = """
            VAR r1: integer;
            PROCEDURE main(); 
                BEGIN 
                    putString(foo("Minh Tham"));
                END          
            FUNCTION foo(in1:string):string;
            BEGIN
                putString("Toi la ");
                return in1;
            END    
            """
        expect = """Toi la Minh Tham"""
        self.assertTrue(TestCodeGen.test(input,expect,545)) 

    def test_if_statement_1(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a > 4 then
                        putIntLn(10);
                    else
                        putIntLn(20);
                    putString("Thanh Cong");
                END
            """
        expect = "10\nThanh Cong"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_if_statement_2(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 3;
                    if a > 4 then
                        putIntLn(5);
                    else
                        putIntLn(10);
                    putString("Thanh Cong");
                END
            """
        expect = "10\nThanh Cong"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_if_statement_3(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 3;
                    if a > 4 then
                        putIntLn(5);
                    putString("Thanh Cong");
                END
            """
        expect = "Thanh Cong"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_if_statement_4(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a > 4 then
                        putIntLn(5);
                    putString("Thanh Cong");
                END
            """
        expect = "5\nThanh Cong"
        self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_if_statement_5(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a = 5 then
                        putIntLn(5);
                    putString("Thanh Cong");
                END
            """
        expect = "5\nThanh Cong"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_if_statement_6(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a = 5 then
                    BEGIN
                        putStringLn("Minh Tham zero");
                        while (a < 9) do
                        begin
                            putInt(a);
                            a := a + 1;
                        end
                    END
                END
            """
        expect = "Minh Tham zero\n5678"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_if_statement_7(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a = 5 then
                    BEGIN
                        putStringLn("Minh Tham zero");
                        IF a > 5 then 
                            putString("Then statement");
                        else
                            putString("10");
                    END
                END
            """
        expect = "Minh Tham zero\n10"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_if_statement_8(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a = 5 then
                        BEGIN
                            putStringLn("Minh Tham zero");
                            IF a > 5 then 
                                putString("Then statement");
                            else
                                putString("10");
                        END
                    else
                        putString("else statement");
                    putString(" ZERO");
                    
                END
            """
        expect = "Minh Tham zero\n10 ZERO"
        self.assertTrue(TestCodeGen.test(input, expect,553))

    def test_if_statement_9(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a > 5 then
                        BEGIN
                            putStringLn("Minh Tham zero");
                            IF a > 5 then 
                                putString("Then statement");
                            else
                                putString("10");
                        END
                    else
                        BEGIN
                            putStringLn("Minh Tham zero");
                            IF a > 5 then 
                                putString("Then statement");
                            else
                                putString("10");
                        END
                    putString(" ZERO");
                    
                END
            """
        expect = "Minh Tham zero\n10 ZERO"
        self.assertTrue(TestCodeGen.test(input, expect,554))

    def test_if_statement_10(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    if a > 5 then
                        BEGIN
                            putStringLn("Minh Tham zero");
                            IF a > 5 then 
                                putString("Then statement");
                            else
                                putString("10");
                            putString(" ZERO");
                        END
                    else
                        BEGIN
                            putStringLn("Minh Tham zero");
                            IF a > 5 then 
                                putString("Then statement");
                            else
                                putString("10");
                            putString(" ZERO");
                        END
                    putString(" ZERO");
                    
                END
            """
        expect = "Minh Tham zero\n10 ZERO ZERO"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_while_statement_1(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    while (a < 9) do
                    begin
                        putInt(a);
                        a := a + 1;
                    end
                END
            """
        expect = "5678"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_while_statement_2(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    while (a < 9) do
                    begin
                        putInt(a);
                        a := a + 1;
                        break;
                    end
                END
            """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_while_statement_3(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    while (a < 9) do
                    begin
                        putInt(a);
                        a := a + 1;
                        continue;
                        putString("CONTINUE");
                    end
                END
            """
        expect = "5678"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_while_statement_4(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    while (a < 9) do
                    begin
                        putFloat(a);
                        a := a + 1;
                        continue;
                        putString("CONTINUE");
                    end
                END
            """
        expect = "5.06.07.08.0"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_while_statement_5(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    b := 10;
                    test(a);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloat(b);
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    while (a < 9) do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        else
                            break;
                        a := a + 1;
                    end
                END
            VAR b : real;
            """
        expect = "5\nGia tri b = 10.0\n5\nGia tri b = 20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_while_statement_6(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    b := 10;
                    test(a);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloat(b);
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    while (a < 9) do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        else
                            begin
                                a := a + 1;                
                                continue;
                            end
                        a := a + 1;                
                        
                    end
                END
            VAR b : real;
            """
        expect = "5\nGia tri b = 10.0\n5\n6\n7\n8\nGia tri b = 20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_for_statement_1(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    a := 5;
                    for a := 1 to 10 do
                        putInt(a);
                END
            """
        expect = "12345678910"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_for_statement_2(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 to 15 do
                        putInt(a);
                END
            """
        expect = "101112131415"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_for_statement_3(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 to 15 do
                    BEGIN
                        putInt(a);
                        continue;
                        putString("Continue");
                    END
                END
            """
        expect = "101112131415"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_for_statement_4(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 to 15 do
                    BEGIN
                        putInt(a);
                        break;
                        putString("Continue");
                    END
                END
            """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    
    def test_for_statement_5(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 downto -1 do
                        putInt(a);
                END
            """
        expect = "109876543210-1"
        self.assertTrue(TestCodeGen.test(input,expect,566))   

    def test_for_statement_6(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 downto -1 do
                    BEGIN
                        putInt(a);
                        continue;
                        putString("Continue");
                    END
                END
            """
        expect = "109876543210-1"
        self.assertTrue(TestCodeGen.test(input,expect,567)) 

    def test_for_statement_7(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    for a := 10 downto -1 do
                    BEGIN
                        putInt(a);
                        break;
                        putString("Continue");
                    END
                END
            """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,568)) 

    def test_for_statement_8(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloat(b);
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    for a := 1 to 10 do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        else
                            begin
                                a := a + 1;
                                continue;
                            end   
                        putString("fail");                    
                    end
                END
            VAR b : real;
            """
        expect = "1\nGia tri b = 10.0\n2\n4\n6\n8\n10\nGia tri b = 20.0"
        self.assertTrue(TestCodeGen.test(input,expect,569)) 

    def test_for_statement_9(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloat(b);
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    for a := 10 downto -1 do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        if a <> -1 then
                            putString("a = ");                    
                    end
                END
            VAR b : real;
            """
        expect = "10\nGia tri b = 10.0\n9\na = 8\na = 7\na = 6\na = 5\na = 4\na = 3\na = 2\na = 1\na = 0\na = -1\nGia tri b = 20.0"
        self.assertTrue(TestCodeGen.test(input,expect,570)) 

    def test_for_statement_10(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloatLn(b);
                    putString("Zero");
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    for a := 10 downto -1 do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        else
                            begin
                                if a <> -1 then
                                    putString("a = ");                                 
                                a := a - 1;                            
                                continue;
                            end                             
                        putString("Fail");                                   
                    end
                END
            VAR b : real;
            """
        expect = "10\nGia tri b = 10.0\n9\na = 7\na = 5\na = 3\na = 1\na = -1\nGia tri b = 20.0\nZero"
        self.assertTrue(TestCodeGen.test(input,expect,571)) 

    def test_for_statement_11(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloatLn(b);
                    putString("zero");
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    for a := 10 downto -2 do
                    begin
                        putIntLn(a);
                        if check and true then
                            begin
                                putString("Gia tri b = ");
                                putFloatLn(b);
                                check := false;
                                continue;                                
                            end
                        else
                            begin
                                if a <> -1 then
                                    putString("a = ");                                 
                                a := a - 1;                            
                                continue;
                            end                             
                        putString("Fail");                                   
                    end
                END
            VAR b : real;
            """
        expect = "10\nGia tri b = 10.0\n9\na = 7\na = 5\na = 3\na = 1\na = -1\nGia tri b = 20.0\nzero"
        self.assertTrue(TestCodeGen.test(input,expect,572))     

    def test_with_statement_1(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    a := 10;      
                    putString("Gia tri a = ");
                    putIntLn(a); 
                    putString("Gia tri b = ");
                    putFloatLn(b);                                 
                    with
                        b: boolean;
                        a : boolean;
                    DO
                        BEGIn
                            a := false;
                            b := true;
                            putString("Gia tri a = ");
                            putBoolLn(a); 
                            putString("Gia tri b = ");
                            putBoolLn(b);                     
                        END
                    putString("ZeroNMT");
                END
            VAR b : real;
            """
        expect = "Gia tri a = 10\nGia tri b = 10.0\nGia tri a = false\nGia tri b = true\nZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,573))         

    def test_with_statement_2(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloatLn(b);
                    putString("ZeroNMT");
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    with
                        b : real;
                    do
                        begin
                            b := 30;
                            for a := 10 downto -2 do
                            begin
                                putIntLn(a);
                                if check and true then
                                    begin
                                        putString("Gia tri b = ");
                                        putFloatLn(b);
                                        check := false;
                                        continue;                                
                                    end
                                else
                                    begin
                                        if a <> -1 then
                                            putString("a = ");                                 
                                        a := a - 1;                            
                                        continue;
                                    end                             
                                putString("Fail");                                   
                            end
                        end
                END
            VAR b : real;
            """
        expect = "10\nGia tri b = 30.0\n9\na = 7\na = 5\na = 3\na = 1\na = -1\nGia tri b = 20.0\nZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,574))  

    def test_with_statement_3(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    test(0);
                    b := 20;
                    putString("Gia tri b = ");
                    putFloatLn(b);
                    putString("ZeroNMT");
                END
            PROCEDURE test(a : integer);
                var check : boolean;
                BEGIN
                    check := true;
                    with
                        b : real;
                    do
                        begin
                            b := 30;
                            putString("Gia tri b = ");
                            putFloatLn(b);                            
                        end
                END
            VAR b : real;
            """
        expect = "Gia tri b = 30.0\nGia tri b = 20.0\nZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,575))  

    def test_complex_1(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    b := 10;
                    putString("Gia tri b = ");
                    putFloatLn(b);
                    putString("ZeroNMT");
                END
            VAR b : real;
            """
        expect = "Gia tri b = 10.0\nZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,576))  
    
    def test_complex_2(self):
        """--ZERO--"""
        input = """
            function foo():integer;
                        var a:integer;
                        begin
                            a := 2;
                            if (a < 6) then
                                begin 
                                    for a := 1 to 5 do
                                        return a;
                                    return a;
                                end
                            else
                                begin
                                    a := a*2;
                                    return a;
                                end
                        end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,577))      

    def test_complex_3(self):
        """--ZERO--"""
        input = """
            function foo():integer;
                var a:integer;
                begin
                    a:=2;
                    if (a<6) then 
                        begin
                            a:=a-1;
                            if (a>3) then return a; 
                            else return 1;
                        end
                    else
                    begin
                        a:=a*2;
                        return a;
                    end
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_complex_4(self):
        """--ZERO--"""
        input = """
            function foo():integer;
                var a:integer;
                begin
                    a := 2;
                    if (a < 10) then 
                        begin
                            with
                                b:boolean;
                            do
                                begin
                                end
                            return 10;
                        end
                    else
                        begin
                            a := a*2;
                        end
                    return 20;
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,579))  
    
    def test_complex_5(self):
        """--ZERO--"""
        input = """
            function foo():integer;
                var a:integer;
                begin
                    a := 2;
                    if (a < 10) then 
                        begin
                            with
                                b:boolean;
                            do
                                return 10;
                        end
                    else
                        begin
                            a := a*2;
                            return 20;
                        end
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 580))      

    def test_complex_6(self):
        """--ZERO--"""
        input = """
            function foo():integer;
                var a:integer;
                begin
                    a := 2;
                    if (a < 6) then 
                        begin
                            if (a>4) then 
                                return 10; 
                        end
                    else
                        begin
                            return 20;
                        end
                    return 10;
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test_complex_7(self):
        """--ZERO--"""
        input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    if (2 > 1) then
                        begin 
                        end
                    else
                        putString("minhTham");
                    putString("ZeroNMT");
                END
            VAR b : real;
            """
        expect = "ZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,582))  
    
    def test_complex_8(self):
        """--ZERO--"""
        input = """
            procedure main();
                begin
                    if 10 <> 10 then
                        begin
                        end
                    else
                        putString("10 <> 10");
                end
        """
        expect = "10 <> 10"
        self.assertTrue(TestCodeGen.test(input,expect,583))      

    def test_complex_9(self):
        """--ZERO--"""
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
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_complex_10(self):
        """--ZERO--"""
        input = """
            procedure main();
                var n : integer;
                    c : boolean;
                Begin
                    n := 7 ;
                    while (n >=7) and (n <= 9) do
                        begin
                            with 
                                n:integer; 
                            do 
                                begin
                                    n:=9;
                                    begin 
                                        putint(n); 
                                        n:=n+1; 
                                    end
                                end 
                            n:= n+ 1;
                        end
                end
        """
        expect = """999"""
        self.assertTrue(TestCodeGen.test(input,expect,585))  
    
    def test_complex_11(self):
        """--ZERO--"""
        input = """
            function foo(a,b:real ; c:boolean):real;
                Begin
                    if c then
                        return (A - b);
                    else 
                        return a+B;
                end
            procedure main();
                Begin
                    putFloatLn(foo(1+1, 1.0+0.1, true));
                    putFloat(foo(1+1, 1.0+0.1, not true));
                    return;
                end
        """
        expect = """0.9\n3.1"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))      

    def test_complex_12(self):
        """--ZERO--"""
        input = """
            FUNCTION checkPositive(i:integer) : Boolean;
            begin
                if i >= 0 then
                begin
                    putInt(i);
                    putString("  : POSITIVE ");
                    return true;
                end
                putInt(i);
                putString(" : NEGATIVE ");
                return false;
            end

            procedure main();
            begin
                putBoolLn(checkPositive(1));
                putBoolLn(checkPositive(2));
                putBoolLn(checkPositive(3));
                putBoolLn(checkPositive(-3));
                putBoolLn(checkPositive(-2));
                putBoolLn(checkPositive(0));
            end
        """
        expect = "1  : POSITIVE true\n2  : POSITIVE true\n3  : POSITIVE true\n-3 : NEGATIVE false\n-2 : NEGATIVE false\n0  : POSITIVE true\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))    

    def test_complex_13(self):
        """--ZERO--"""
        input = """
            procedure foo(i:integer);
            begin
                if i >= 0 then
                begin
                    putInt(i);
                    putStringLn("  : POSITIVE");
                    return;
                end
                putInt(i);
                putStringLn(" : NEGATIVE");
            end

            procedure main();
            begin
                foo(1);
                foo(2);
                foo(3);
                foo(-3);
                foo(-2);
                foo(0);
            end
        """
        expect = "1  : POSITIVE\n2  : POSITIVE\n3  : POSITIVE\n-3 : NEGATIVE\n-2 : NEGATIVE\n0  : POSITIVE\n"
        self.assertTrue(TestCodeGen.test(input,expect,588))  
    
    def test_complex_14(self):
        """--ZERO--"""
        input = """
            var i : integer;
            procedure foo();
            begin
                i := 0;
                putInt(i);
                with i:integer; do
                    with f,i:real; do
                        with i:boolean; do
                        begin
                            i := 1 > -5;
                            putBool(i);
                        end
            end

            procedure main();
            var i : integer;
            begin
                i := -1;
                putInt(i);
                foo();
                putInt(i);
            end
        """
        expect = "-10true-1"
        self.assertTrue(TestCodeGen.test(input,expect,589))      

    def test_complex_15(self):
        input = """
            procedure main();
            var b : BOOLEAN;
            begin
                b := true;
                while b do
                begin
                    b := not b;
                    putBool(b);
                end
            end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_complex_16(self):
        """--ZERO--"""
        input = """
            var i:integer;
            procedure main();
            begin
                for i:=9 downto 5 do
                    if i mod 3 = 0 then
                        putFloatLn(i div 3);
            end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input,expect,591))  
    
    def test_complex_17(self):
        """--ZERO--"""
        input = """
        procedure main();
        begin
            putBoolLn(T());
            putBoolLn(F());
            putBoolLn(T() and then FOO());
            putBoolLn(F() and then FOO());
        end

        function T():boolean;
        begin
            return TRUE;
        end

        function F():boolean;
        begin
            return FALSE;
        end

        function FOO():boolean;
        begin
            putString("FOO!");
            return false;
        end
        """
        expect = "true\nfalse\nFOO!false\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 592))      

    def test_complex_18(self):
        """--ZERO--"""
        input = """
        procedure main();
        var i: integer;
        begin
            while True do
            begin
                while true do
                begin
                    while not false do
                        break;
                    break;
                end
                break;
            end
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                putIntLn(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 593))
    
    def test_complex_19(self):
        """--ZERO--"""
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                putIntLn(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input,expect,594))  
    
    def test_complex_20(self):
        """--ZERO--"""
        input = """
        VAR a,b,c:integer;
        PROCEDURE main();
            var isTrue, isT, isF:boolean;
            begin
                a := 10;
                b := a * 2;
                c := b div 7;
                fa := (a * b) - (c div a);
                fb := a * (fa + a) * (c - b);
                fc := fa * fb / c;
                putIntLn(a);
                putIntLn(b);
                putIntLn(c);
                putFloatLn(fa);
                putFloatLn(fb);
                putFloatLn(fc);
                isT := fa < fc;
                isF := fb >= fa;
                putBoolLn(isT);       
                putBoolLn(isF);       
            end
        var  fa,fb,fc:real;
        """
        expect = "10\n20\n2\n200.0\n-37800.0\n-3780000.0\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input,expect,595))      

    def test_complex_21(self):
        """--ZERO--"""
        input = """
        PROCEDURE main();
            begin
                foo(10);
                putString("ZeroNMT");
            end
        PROCEDURE foo(a:integer);
            begin
                if a > 1
                    then return;
                    else
                        begin
                            a := a + 2;
                            return;
                        end
            end
        """
        expect = "ZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_complex_22(self):
        """--ZERO--"""
        input = """
        PROCEDURE main();
            begin
                foo(10);
                putString("ZeroNMT");
            end
        PROCEDURE foo(a:integer);
            begin
                putStringLn("Procedure foo");
                return;
            end
        """
        expect = "Procedure foo\nZeroNMT"
        self.assertTrue(TestCodeGen.test(input,expect,597))  
    
    def test_complex_23(self):
        """--ZERO--"""
        input = """
        PROCEDURE main();
            VAR a:integer;
            BEGIN
                a := 5;
                putFloatLn(foo(a));
            END
        FUNCTION foo(a:integer):real;
            VAR foo:integer;
            BEGIN
                foo := 5;
                putStringLn("ZeroNMT");
                return foo + a;
            END 
        """
        expect = """ZeroNMT\n10.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))      

    def test_complex_24(self):
        """--ZERO--"""
        input = """
            PROCEDURE main();
                VAR a:integer;
                BEGIN
                    a := 5;
                    putFloatLn(foo(a));
                END
            FUNCTION foo(a:integer):real;
                BEGIN
                    WITH
                        foo:integer;
                    DO
                        BEGIN
                            foo := 5;
                            putStringLn("ZeroNMT");
                            return foo + a;
                        END
                END 
        """
        expect = """ZeroNMT\n10.0\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))    