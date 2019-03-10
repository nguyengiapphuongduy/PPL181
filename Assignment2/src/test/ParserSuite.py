import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1_simple_program(self):
        """Simple program: only main() with no statement"""
        input = """
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2_more_complex_program(self):
        """one-statement program"""
        input = """
        procedure main ();
        begin
            putIntLn(4);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_3_wrong_miss_close(self):
        """Miss ) in main()"""
        input = """
        procedure main( ; begin end
        """
        expect = "Error on line 2 col 24: ;"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_4_var_declare(self):
        """variable declaration"""
        input = """
        var a,b,c:integer;
        d: array[1 .. 5] of real;
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_5_func_declare(self):
        """normal function declaration"""
        input = """
        function fu(x:integer):array[1 .. 2]of real;
        begin end
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_6_proc_declare(self):
        """normal procedure declaration"""
        input = """
        procedure fu(a,b:integer;c:real);
        begin end
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_7_func_err_declare(self):
        """function declaration with err begin end"""
        input = """
        function foo(i:integer):real;
            procedure child_of_foo(real f);
            begin end
        begin end
        procedure main(); begin end
        """
        expect = "Error on line 3 col 12: procedure"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_8_line_comment(self):
        """single-line comment"""
        input = """
        //asdlkfj;asdf\t\f\b\'"\\
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_9_block_comment(self):
        """block comment"""
        input = """
        {
        alskdfn;kohqpweornlk\b\f\r\n\t\'"~\\
        }
        procedure main(); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_10_simple_exp(self):
        """normal simple expression"""
        input = """
        procedure main(); begin
            x:=1+1-2*3 div 4 mod 5/6;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
    def test_11_simple_assignment(self):
        """normal simple assignment"""
        input = """
        procedure main(); begin
            x:=y:=z:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_12_simple_if_else(self):
        """normal simple if statement"""
        input = """
        procedure main(); begin
            if a>1 then fu(); else ff();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13_simple_if(self):
        """normal simple if no else"""
        input = """
        procedure main(); begin
            if f()[1]>1 then fu();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14_simple_program(self):
        """simple program"""
        input = """
        procedurE foo (b : real) ;
        beGin
            aa := b [ 10 ] := foo ( ) [ 3 ] := x := 1 ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15_simple_expr(self):
        """expr and assignment"""
        input = """
        procedure main () ;
            beGin
                a := b [ 10 ] := foo ( ) [ 3 ] := x := 1 ;
            END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16_procedure_declaration(self):
        input = """procedure foo(a, b: integer ; c: real) ;
        var x,y: real ;
        BEGIN
        END
        procedure main(); begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17_complex_program(self):
        input = """
        var i : integer ;
        function f ( ) : integer ;
        begin
        return 200;
        end
        procedure main ( ) ;
        var
        main : integer ;
        begin
            main := f ( ) ;
            putIntLn ( main ) ;
            with
                i : integer ;
                main : integer ;
                f : integer ;
            do begin
                main := f := i := 100;
                putIntLn ( i ) ;
                putIntLn ( main ) ;
                putIntLn ( f ) ;
            end
            putIntLn ( main ) ;
        end
        var g : real ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18_assigment_statement(self):
        """single assignment"""
        input = """
        procedure main () ;
        begin
            x := a = b;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19_assigment_statement(self):
        """multiple assignment"""
        input = """
        procedure main () ;
        begin
            x := a := b;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20_assigment_statement(self):
        """assign string"""
        input = """
        procedure main () ;
        begin
            x := "abcxyz";
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21_assigment_statement(self):
        """assign real"""
        input = """
        procedure main () ;
        begin
            x := 1.1e-5;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22_assigment_statement(self):
        """assign boolean"""
        input = """
        procedure main () ;
        begin
            x := FALSE and then true;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23_if_statement(self):
        """simple if-else statement"""
        input = """
        procedure main () ;
        begin
            if(a>1) then a:=1 ;
            else if (1<2)<>(2<3) then a:=0 ;
            else foo(a+1,2,3,4,5);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24_if_statement(self):
        """wrong if-else: missing statement after else"""
        input = """
        procedure main () ;
        begin
            if(a>1) then a:=1 ;
            else 
            else foo(a+1,2,3,4,5);
        end
        """
        expect = "Error on line 6 col 12: else"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25_if_statement(self):
        """wrong if-else: empty statement"""
        input = """
        procedure main () ;
        begin
            if(a>1) then a:=1 ;
            else ;
            else foo(a+1,2,3,4,5);
        end
        """
        expect = "Error on line 5 col 17: ;"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26_if_statement(self):
        """wrong statement: only expression"""
        input = """
        procedure main () ;
        begin
            if(a>1) then a:=1 ;
            else 1+1+1-2-3;
            else foo(a+1,2,3,4,5);
        end
        """
        expect = "Error on line 5 col 18: +"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27_if_statement(self):
        """wrong if-else: unexpected else statement"""
        input = """
        procedure main () ;
        begin
            if(a>1) then a:=1 ;
            else a:=0;
            else foo(a,1,2,3,4,5);
        end
        """
        expect = "Error on line 6 col 12: else"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28_expression(self):
        """complex expression"""
        input = """
        procedure main () ;
        begin
            x := fu()[1][x*x+1][gu[fu()[0]][1]];
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29_invocation(self):
        """complex invocation"""
        input = """
        procedure main () ;
        begin
            x := fu(g(k)+asdf(asdf(-1))/xxxx);
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30_while_statement(self):
        """simple while statement"""
        input = """
        procedure main () ;
        begin
            while (x>0) do x:=x-1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31_while_statement(self):
        """wrong while statement: missing expression"""
        input = """
        procedure main () ;
        begin
            while () do x:=1;
        end
        """
        expect = "Error on line 4 col 19: )"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32_while_statement(self):
        """wrong while statement: missing statement"""
        input = """
        procedure main () ;
        begin
            while (True) do ;
        end
        """
        expect = "Error on line 4 col 28: ;"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33_while_statement(self):
        """wrong while statement: missing statement"""
        input = """
        procedure main () ;
        begin
            while (True) do 
        end
        """
        expect = "Error on line 5 col 8: end"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34_while_statement(self):
        """correct while statement"""
        input = """
        procedure main () ;
        begin
            while (True) do 
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35_for_statement(self):
        """correct for statement"""
        input = """
        procedure main () ;
        begin
            for i:=1 to n do a:=i;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36_for_statement(self):
        """correct for statement"""
        input = """
        procedure main () ;
        begin
            for i:=1 to n do
            begin
                a:=i;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37_for_statement(self):
        """wrong for statement: unexpected semi"""
        input = """
        procedure main () ;
        begin
            for i:=1 to n do
            begin
                a:=i;
            end;
        end
        """
        expect = "Error on line 7 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38_for_statement(self):
        """wrong for statement: wrong id"""
        input = """
        procedure main () ;
        begin
            for 2i:=1 to n do
            begin
                a:=i;
            end
        end
        """
        expect = "Error on line 4 col 16: 2"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39_for_statement(self):
        """wrong for statement: missing assignment"""
        input = """
        procedure main () ;
        begin
            for asdfi=1 to n do
            begin
                a:=i;
            end
        end
        """
        expect = "Error on line 4 col 21: ="
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40_for_statement(self):
        """wrong for statement: missing expression"""
        input = """
        procedure main () ;
        begin
            for asdfi:= to n do
            begin
                a:=i;
            end
        end
        """
        expect = "Error on line 4 col 24: to"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41_for_statement(self):
        """correct for statement"""
        input = """
        procedure main () ;
        begin
            for asdfi:=nnn downto x=n[1] do
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42_break_statement(self):
        """correct break statement"""
        input = """
        procedure main () ;
        begin
            break;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43_break_statement(self):
        """wrong break statement"""
        input = """
        procedure main () ;
        begin
            break;;
        end
        """
        expect = "Error on line 4 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44_break_statement(self):
        """wrong break statement: unexpected expression"""
        input = """
        procedure main () ;
        begin
            break asdf;
        end
        """
        expect = "Error on line 4 col 18: asdf"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45_continue_statement(self):
        """correct continue statement"""
        input = """
        procedure main () ;
        begin
            continue ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46_continue_statement(self):
        """wrong continue statement: unexpected ;"""
        input = """
        procedure main () ;
        begin
            continue ;;
        end
        """
        expect = "Error on line 4 col 22: ;"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47_continue_statement(self):
        """wrong continue statement: unexpected expression"""
        input = """
        procedure main () ;
        begin
            continue x:=1+1;
        end
        """
        expect = "Error on line 4 col 21: x"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48_return_statement(self):
        """correct return statement"""
        input = """
        procedure main () ;
        begin
            return;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49_return_statement(self):
        """correct return statement"""
        input = """
        procedure main () ;
        begin
            return x=f()[2];
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50_return_statement(self):
        """wrong return statement: expression not assignment"""
        input = """
        procedure main () ;
        begin
            return x:=f()[2];
        end
        """
        expect = "Error on line 4 col 20: :="
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51_return_statement(self):
        """wrong return statement: unexpected ;"""
        input = """
        procedure main () ;
        begin
            return ;;
        end
        """
        expect = "Error on line 4 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52_compound_statement(self):
        """normal compound statement"""
        input = """
        procedure main () ;
        begin
            begin
                begin
                    a:=a+1;
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53_compound_statement(self):
        """normal compound statement"""
        input = """
        procedure main () ;
        begin
            begin
                begin
                end
                begin
                end
                a:=a+1;
            end
            fuckasdfthisjklassignment();
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54_compound_statement(self):
        """wrong compound statement: unexpected ;"""
        input = """
        procedure main () ;
        begin
            begin
                a:=a+1;
            end;
            fuckasdfthisjklassignment();
        end
        """
        expect = "Error on line 6 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55_compound_statement(self):
        """correct compound statement"""
        input = """
        procedure main () ;
        begin
            bullasdfshitqwenm();
        end;
        """
        expect = "Error on line 5 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56_compound_statement(self):
        """correct compound statement"""
        input = """
        procedure main () ;
        begin
            bullasdfshitqwenm();
        end;;;;
        """
        expect = "Error on line 5 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57_with_statement(self):
        """correct with statement"""
        input = """
        procedure main () ;
        begin
            with a,b:integer;c:array[1 .. 2]of real; do
            d:=c[a] + b ;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58_with_statement(self):
        """correct with statement"""
        input = """
        procedure main () ;
        begin
            with a,b:integer;c:array[1 .. 2]of real; do
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59_with_statement(self):
        """wrong with statement: missing ; in vardecl"""
        input = """
        procedure main () ;
        begin
            with a:integer do begin end
        end
        """
        expect = "Error on line 4 col 27: do"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60_with_statement(self):
        """correct nested with statement"""
        input = """
        procedure main () ;
        begin
            with a:integer; do
            begin
                with b:real; do b:=a+b;
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61_comment(self):
        """block comment"""
        input = """
        {
        a;lsdifjasvnbvik\\\
        she\b\s\f\g
        }
        procedure main (); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62_comment(self):
        """block comment"""
        input = """
        (*
        a;lsdifjasvnbvik\\\
        \r\n\t
        
        she\b\s\f\g
        *)
        procedure main (); begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63_string_expression(self):
        """expression contains string"""
        input = """
        procedure main (); begin
            writeln("asdfas\\n;kljf");
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64_loop(self):
        """while loop"""
        input = """
        procedure main (); begin
            while (1) do begin
                if (a<>b) then fuuuuu(f(a)[-1]+g(b));
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65_nested_loop(self):
        """for and while"""
        input = """
        procedure main (); begin
            for i:=1 to 100 do while (1) do begin
                if (a<>b) then fuuuuu(f(a)[-1]+g(b));
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66_assignment(self):
        """expression instead of id"""
        input = """
        procedure main (); begin
            a + b := c;
        end
        """
        expect = "Error on line 3 col 14: +"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67_assignment(self):
        """wrong multiple assignment"""
        input = """
        procedure main (); begin
            a := b + c := d;
        end
        """
        expect = "Error on line 3 col 23: :="
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68_assignment(self):
        """wrong multiple assignment"""
        input = """
        procedure main (); begin
            a := (b + c) := d;
        end
        """
        expect = "Error on line 3 col 25: :="
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69_assignment(self):
        """complex assignment"""
        input = """
        procedure main (); begin
            a := b := foiasudf(xzxcv)[aa[ccc[xxx]]] := -1.23e-10;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70_var_declare(self):
        """variable declaration"""
        input = """
        var a:integer; BbBb:real;
        cccC:array[n..m] of real;
        var x:integer;
        procedure main (); begin
            a:=1;
        end
        """
        expect = "Error on line 3 col 19: n"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71_var_declare(self):
        """variable declaration"""
        input = """
        var a:integer; BbBb:real;
        cccC:array[n..m] of real;
        var x:integer;
        procedure main (); var y:integer; begin
            a:=1;
        end
        """
        expect = "Error on line 3 col 19: n"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72_mix_declare(self):
        """function - variable declaration"""
        input = """
        var a:integer; BbBb:real;
        function foo(var x:integer): real;
        cccC:array[n..m] of real;
        begin end
        var x:integer;
        procedure main (); var y:integer; begin
            a:=1;
        end
        """
        expect = "Error on line 3 col 21: var"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_73_mix_declare(self):
        """function - variable declaration"""
        input = """
        var a:integer; BbBb:real;
        function foo(x:integer): real;
        var cccC:array[n..m] of real;
        begin end
        var x:integer;
        procedure main (); var y:integer; begin
            a:=1;
        end
        """
        expect = "Error on line 4 col 23: n"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_74_mix_declare(self):
        """var - func - proc declaration"""
        input = """
        var a:integer; var BbBb:real;
        function foo(x:integer): real; begin end
        procedure pr(); begin end
        var x:integer;
        procedure main (); var y:integer; begin
            a:=1;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_75_mix_declare(self):
        """func missing compound statement"""
        input = """
        function foo(x:integer): real;
        procedure pr(); begin end
        var x:integer;
        procedure main (); var y:integer; begin end
        """
        expect = "Error on line 3 col 8: procedure"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_76_mix_declare(self):
        """proc missing compound statement"""
        input = """
        function foo(x:integer): real; begin end
        procedure pr();
        var x:integer;
        procedure main (); var y:integer; begin end
        """
        expect = "Error on line 5 col 8: procedure"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_77_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[1..2]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "Error on line 2 col 32: 1."
        self.assertTrue(TestParser.test(input,expect,277))
    def test_78_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[1 ..2]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_79_array(self):
        """array indexes"""
        input = """
        var y: array[1.. ]of real;
        procedure main (); begin end
        """
        expect = "."
        self.assertTrue(TestParser.test(input,expect,279))
    def test_80_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[1 .. ]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "Error on line 2 col 37: ]"
        self.assertTrue(TestParser.test(input,expect,280))
    def test_81_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[.. 2]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "Error on line 2 col 32: .."
        self.assertTrue(TestParser.test(input,expect,281))
    def test_82_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[asdf .. fdsa]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "Error on line 2 col 32: asdf"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_83_array(self):
        """array indexes"""
        input = """
        var x:integer; y: array[x+y div z*foo() .. fdsa]of real;
        procedure main (); var z:integer; begin end
        """
        expect = "Error on line 2 col 32: x"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_84_expression(self):
        """expression error: '=' has assoc = none"""
        input = """
        function foo(a, b: integer ; c: real):array [1 .. 2] of integer ;
        var x:real ;
        BEGIN
            while (a=3 or a+b = 6) do 
            begin end
        END
        """
        expect = "Error on line 5 col 30: ="
        self.assertTrue(TestParser.test(input,expect,284))
    def test_85_mix(self):
        """mix program"""
        input = """
        procedure abc ();
        var x , y : real ; 
            begin
                if x = y then
                   a:= 1000;
                else;
                    b:= 999;
            end
        """
        expect = "Error on line 7 col 20: ;"
        self.assertTrue(TestParser.test(input,expect,285))
    def test_86_mix(self):
        """mix program"""
        input = """
        procedure foo(aaaasdf: real) ;
        var x:real ;
        BEGIN
        if(aaaasdf>1) then beGin
            aaaasdf:=1 ;
            if(x=1) then aaaasdf:= b[1];
            else b:=aaaasdf[1]:= 1;end END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_87_expression(self):
        """expression error: '>=' has assoc = none"""
        input = """
        procedure main(); begin
            if( a >= b >= c ) then a:= b[1];
            else b:=a[1]:= 1;
        END
        """
        expect = "Error on line 3 col 23: >="
        self.assertTrue(TestParser.test(input,expect,287))
    def test_88_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            if( a = b or 100 ) then a:= b[1];
            else b:=a[1]:= 1;
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_89_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            if( a = b or 100 or foo()[d] + 1 ) then a:= b[1];
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_90_expression(self):
        """expression error: '=' and '>=' have none associative"""
        input = """
        procedure main(); begin
            if( a = b >= c ) then begin end
        END
        """
        expect = "Error on line 3 col 22: >="
        self.assertTrue(TestParser.test(input,expect,290))
    def test_91_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            if( (a = b) >= c ) then begin end
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_92_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            if( a = (b >= c) ) then begin end
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_93_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            x:=a+-1;
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_94_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            if (a and b and then c or d and then f) then begin end
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_95_expression(self):
        """expression ok"""
        input = """
        procedure main(); begin
            while (True) do begin e:=1; continue; break; end
            return; return e;
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_96_mix(self):
        """expression ok"""
        input = """
        PROCEDURE main() ;
        var x,y: real ;
        BEGIN
            1 := 1;
            c := a[12] ;
        END
        """
        expect = "Error on line 5 col 14: :="
        self.assertTrue(TestParser.test(input,expect,296))
    def test_97_mix(self):
        """multiple declaration"""
        input = """
        PROCEDURE main() ;
        var x,y: real; abc: integer; xx: array[-4 .. -100] of real;
        var a: string; var b: boolean;
        BEGIN
            a := "a";
            b := truE;
        END
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_98_mix(self):
        """error: declare in begin-end"""
        input = """
        PROCEDURE main() ;
        var x,y: real; abc: integer; xx: array[-4 .. -100] of real;
        var a: string; var b: boolean;
        BEGIN
            var a:integer;
            a := "a";
            b := truE;
        END
        """
        expect = "Error on line 6 col 12: var"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_99_mix(self):
        """expression ok"""
        input = """var a:integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_00_mix(self):
        """expression ok"""
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,200))
