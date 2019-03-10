import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_500(self):
        input = """
        var x:integer;
        procedure main();
        begin
            x := 1;
            foo(x, 1.0);
            putInt(x);
        end

        procedure foo(i: integer; f: real);
        var bar:boolean;
        begin
            bar := true;
            putBool(bar);
            i := 2;
            putInt(i);
        end
        """
        expect = "true21"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_with_501(self):
        input = """
        var i:integer;
        procedure main();
        begin
            i := 1;
            with i:integer; do
            begin
                i := 2;
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_if_502(self):
        input = """
        procedure main();
        begin
            if true then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_if_503(self):
        input = """
        procedure main();
        begin
            if false then
                putBool(true);
            else
                putBool(false);
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_for_504(self):
        input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        expect = "123"
        self.assertTrue(TestCodeGen.test(input, expect, 504))



    def test_binop_507(self):
        input = """
		procedure main();
		begin
			putIntLn(1+2);
            putIntLn(1-2);
            putIntLn(1*2);
            putIntLn(1 div 2);
            putIntLn(31 mod 4);
            putFloatLn(1/2);
            putBoolLn(1 > 2);
            putBoolLn(1 < 2);
            putBoolLn(1 <= 2);
			return;
		end
		"""
        expect = "3\n-1\n2\n0\n3\n0.5\nfalse\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_binop_508(self):
        input = """
		procedure main();
		begin
            // same result as AND
			putBoolLn(true and then false);
            putBoolLn(true and then true);
            putBoolLn(false and then true);
            putBoolLn(false and then false);
            // skip evaluation of the second operand --> no error
            putBoolLn(false and then 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\nfalse\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_binop_509(self):
        input = """
		procedure main();
		begin
            // same result as OR
			putBoolLn(false or else false);
            putBoolLn(false or else true);
            putBoolLn(true or else true);
            putBoolLn(true or else false);
            // skip evaluation of the second operand --> no error
            putBoolLn(true or else 0 div 0 = 0);
            // error
            // putBoolLn(true and then 0 div 0 = 0);
			return;
		end
		"""
        expect = "false\ntrue\ntrue\ntrue\ntrue\n"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_binop_510(self):
        input = """
        function foo():real;
        begin
            return 1;
        end

		procedure main();
		begin
            putFloat(foo());
		end
		"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))


    def test_while_515(self):
        input = """
        procedure main();
        var i:integer;
        begin
            i := 0;
            while true do
            begin
                if i = 5 then break;
                putInt(i);
                i := i + 1;
            end
        end
		"""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    
    def test_exp_517(self):
        input = """
        procedure main();
        begin
            putInt(1+1-2*3);
        end
		"""
        expect = "-4"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_exp_518(self):
        input = """
        procedure main();
        begin
            putFloatLn(-2/5);
            putIntLn((27 mod 8));
            putIntLn(27 div -3);
            putInt(-28 div -3);
        end
		"""
        expect = "-0.4\n3\n-9\n9"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_exp_519(self):
        input = """
        procedure main();
        begin
            putFloatLn(1/1);
            putFloatLn(1./1);
            putFloatLn(1/1.);
            putFloatLn(1./1.);
            putFloat(1./1. - 1/1);
        end
		"""
        expect = "1.0\n1.0\n1.0\n1.0\n0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_exp_520(self):
        input = """
        procedure main();
        begin
            putFloatLn(----------3.14e10);
            putIntLn(0 div 1);
            putFloat(-0 / -1);
        end
		"""
        expect = "3.13999995E10\n0\n-0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_exp_521(self):
        input = """
        procedure main();
        var x,y,z:integer;
        begin
            x := 1;
            y := 2;
            z := -5;
            putInt(x+y-z*3);
        end
		"""
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_exp_522(self):
        input = """
        procedure main();
        var x,y,z:integer;
        f,r:real;
        begin
            x := 1;
            y := 2;
            z := -5;
            f := x + y;
            r := f/2;
            putIntLn(x+y-z*3);
            putFloat(f*r*x);
        end
		"""
        expect = "18\n4.5"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_exp_523(self):
        input = """
        procedure main();
        begin
            putFloatLn(0);
            putBoolLn(true);
            putBool(false);
        end
		"""
        expect = "0.0\ntrue\nfalse"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_exp_524(self):
        input = """
        procedure main();
        begin
            putBool(true or false);
            putBool(true or true);
            putBool(false or true);
            putBool(false or false);
        end
		"""
        expect = "truetruetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_exp_525(self):
        input = """
        procedure main();
        begin
            putBool(true and false);
            putBool(true and true);
            putBool(false and true);
            putBool(false and false);
        end
		"""
        expect = "falsetruefalsefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_exp_526(self):
        input = """
        procedure main();
        begin
            putBool(not true);
            putBool(not false);
            putBool(not not true);
            putBool(not not false);
            putBool(not not not not (true and true));
        end
		"""
        expect = "falsetruetruefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_exp_527(self):
        input = """
        procedure main();
        begin
            putBool(1 > 2);
            putBool(1.0 < 2);
            putBool(-1 <= 10.0);
        end
		"""
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_exp_528(self):
        input = """
        procedure main();
        begin
            putBool(-5.0 >= -5.);
            putBool(1. = 1);
            putBool(0.0 <> 0);
        end
		"""
        expect = "truetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_exp_529(self):
        input = """
        procedure main();
        begin
            putBool(1-1 = 0);
            putBool(not (1 > 2));
            putBoolLn(1.*1 <> 1/1);
            putBoolLn(1 div 1 <> 1*1);
            putFloatLn(1.*1);
            putFloatLn(1/1);
        end
		"""
        expect = "truetruefalse\nfalse\n1.0\n1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_exp_530(self):
        input = """
        var a : integer;
        procedure main();
        begin
            a := -4;
            putBool((a/8 - 3) < 0);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_exp_531(self):
        input = """
        var a : integer;
        procedure main();
        begin
            a := -4;
            putBool(a = a);
            putBool(a = a*1.);
        end
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_exp_537(self):
        input = """
        procedure main();
        begin
            putboolln(T());
            putboolln(F());
            putboolln(T() and then foo());
            putboolln(F() and then foo());
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
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_exp_538(self):
        input = """
        var INTMAX, INTMIN:integer;
        procedure main();
        begin
            INTMAX := 2147483647;
            INTMIN := INTMAX*-1-1;
            putIntLn(INTMAX);
            putIntLn(INTMIN);
            putIntLn(INTMAX + INTMIN);
        end
        """
        expect = "2147483647\n-2147483648\n-1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 538))


    def test_if_540(self):
        input = """
        procedure main();
        begin
            if true then
                putString("TRUE");
        end
        """
        expect = "TRUE"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_if_541(self):
        input = """
        procedure main();
        begin
            if false then
                putString("TRUE");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_if_542(self):
        input = """
        procedure foo(i:integer);
        begin
            if i >= 0 then
                putStringLn("POSITIVE");
            else
                putStringLn("NEGATIVE");
        end

        procedure main();
        begin
            foo(100);
            foo(0);
            foo(-1);
        end
        """
        expect = "POSITIVE\nPOSITIVE\nNEGATIVE\n"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_if_543(self):
        input = """
        function abs(i:integer):integer;
        begin
            if i >= 0 then
                return i;
            else
                return -i;
        end

        procedure main();
        begin
            putIntLn(abs(167));
            putIntLn(abs(-167));
            putIntLn(abs(167)-abs(-167));
        end
        """
        expect = "167\n167\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_if_544(self):
        input = """
        function absFloat(i:integer):real;
        begin
            if i >= 0 then
                return i*1.;
            else
                return -i*1.;
        end

        procedure main();
        begin
            putFloatLn(absFloat(167));
            putFloatLn(absFloat(-167));
            putFloatLn(absFloat(167)-absFloat(-167));
        end
        """
        expect = "167.0\n167.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_if_545(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            putString("ABC");
        end
        """
        expect = "ABC"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_if_546(self):
        input = """
        procedure main();
        begin
            if (10 > 1) then
            begin end
            else
                putString("ABC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_if_547(self):
        input = """
        procedure main();
        begin
            if 10 = 10 then
            begin
                putString("10 = 10"); 
            end
            else
                putString("10 <> 10");
        end
        """
        expect = "10 = 10"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_if_548(self):
        input = """
        procedure main();
        begin
            if 10 <> 10 then
            begin end
            else
                putString("10 <> 10");
        end
        """
        expect = "10 <> 10"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_if_549(self):
        input = """
        procedure main();
        begin
            if 1.0 >= -1.0 then
                putStringLn("1.0 >= -1.0");
            putString("Hi");
        end
        """
        expect = "1.0 >= -1.0\nHi"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_assign_550(self):
        input = """
        var globalInt:integer;
        globalFloat:real;
        globalBool:boolean;

        procedure main();
        var localInt:integer;
        localFloat:real;
        localBool:boolean;
        begin
            globalInt := localInt := 0;
            globalFloat := localFloat := 1;
            localBool := globalBool := not not not true;
            putIntLn(globalInt);
            putIntLn(localInt);
            putFloatLn(globalFloat);
            putFloatLn(localFloat);
            putBoolLn(localBool);
            putBoolLn(globalBool);
        end
        """
        expect = "0\n0\n1.0\n1.0\nfalse\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 550))


    def test_assign_555(self):
        input = """
        procedure main();
        begin
            x := 37 div 5;
            x := x := x := x;
            putInt(x);
        end

        var x : integer;
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_assign_556(self):
        input = """
        procedure main();
        begin
            a := -1000000;
            b := 1000000;
            // swap
            t := a;
            a := b;
            b := t;
            putIntLn(a);
            putIntLn(b);
        end

        var a,b,t : integer;
        """
        expect = "1000000\n-1000000\n"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_while_557(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            while i < 5 do
            begin
                i := i + 1;
            end
            putInt(i);
        end
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_while_558(self):
        input = """
        procedure main();
        var i : integer;
        begin
            while FALSE do
                putString("FALSE");
            while -256 > -1 do
            begin
                putString("-256 > -1");
            end
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_while_559(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 10;
            while i = 10 do
            begin
                putIntLn(i);
                i := 11;
            end
            putIntLn(i);
        end
        """
        expect = "10\n11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_while_560(self):
        input = """
        procedure main();
        var b : BOOLEAN;
        begin
            b := true;
            while B do
            begin
                b := not b;
                putBool(b);
            end
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_while_561(self):
        input = """
        procedure main();
        var a, b : real;
        begin
            a := 100;
            b := -100;
            while a <> b do
            begin
                a := -1 + a;
                b := 1 + b;
            end
            putFloat(a - b);
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_while_562(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            while i mod 3 = 0 do
            begin
                i := i + 3;
                if i = 99 then i := i + 1;
            end
            putInt(i);
        end
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_while_563(self):
        input = """
        function isPositive(i:integer):boolean;
        begin
            return i >= 0;
        end

        function getMaxInt():integer;
        var i: integer;
        begin
            i := 0;
            while isPositive(i) and isPositive(i + 1) do
            begin
                i := i + 1;
            end
            return i;
        end

        procedure main();
        var i : integer;
        begin
            putInt(getMaxInt());
        end
        """
        expect = "2147483647"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_while_564(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    j := j + 1;
                    counter := counter + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_while_565(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    k := 0;
                    while k < 5 do
                    begin
                        k := k + 1;
                        counter := counter + 1;
                    end
                    j := j + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        expect = "60"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_while_566(self):
        input = """
        procedure main();
        begin
            while not true do
                while not false do
                    while true do
                        WHILE TRUE and TRUE do
                            putInt(-999);
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_for_567(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 9 do
                putInt(i);
        end
        """
        expect = "123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_for_568(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -5 to -1 do
                putInt(i);
        end
        """
        expect = "-5-4-3-2-1"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_for_569(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 3 do
            begin end
            putInt(i);
        end
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_for_570(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 9 downto 1 do
            begin
                putInt(i);
            end
        end
        """
        expect = "987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_for_571(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -1 downto -4 do
            begin
                putInt(i);
            end
            putInt(i);
        end
        """
        expect = "-1-2-3-4-5"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_for_572(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := 0 to 10 do
            begin
                if i mod 2 = 0 then
                    putInt(i);
            end
        end
        """
        expect = "0246810"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_for_573(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i := 0 to 10 do
                for j := 0 to 10 do
                    counter := counter + 1;
            putInt(counter);
        end
        """
        expect = "121"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_for_574(self):
        input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            counter := 0;
            for i := 9 downto 1 do
                for j := 8 downto 1 do
                    for k:= 7 downto 1 do
                        counter := counter + 1;
            putBool(counter = 7*8*9);
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_for_575(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i:= 10 div 10 to 9 * 19 div 10 do
                while 5 > i do
                begin
                    putInt(i);
                    i := i + 1;
                end
            putStringLn("");
            putInt(i);
        end
        """
        expect = "1234\n18"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_for_576(self):
        input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i:= 1 to 20000 do
                for j := 20000 downto 1 do
                    counter := counter - 1;
            putInt(counter);
        end
        """
        expect = "-400000000"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_for_578(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=9 downto 5 do
                if i mod 3 = 0 then
                    putfloatln(i div 3);
        end
        """
        expect = "3.0\n2.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_for_579(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:=-100 to 100 do
                for i:= 0 to 100 do begin end
            putInt(i);
        end
        """
        expect = "102"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_break_continue_580(self):
        input = """
        var i:integer;
        procedure main();
        begin
            for i:= 0 to 10 do
                if i > 5 then break;
            putIntLn(i);

            for i:= 0 to 100 do
            begin
                if i >= 10 then continue;
                else putInt(i);
            end
        end
        """
        expect = "6\n0123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_break_continue_581(self):
        input = """
        var i,j:integer;
        procedure main();
        begin
            while TRUE do
            begin
                putStringLn("LOOPING...");
                break;
            end
            for i:= 1 to 100 do
            begin
                while not not not false do
                    break;
                for j := -9 to -1 do
                begin
                    putInt(-(j*i));
                end
                break;
            end
        end
        """
        expect = "LOOPING...\n987654321"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_break_continue_582(self):
        input = """
        procedure main();
        var i : integer;
        begin
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_break_continue_583(self):
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
                PUTINTln(i);
            end
        end
        """
        expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_break_continue_584(self):
        input = """
        var i : integer;
        procedure main();
        begin
            for i:=90 downto 0 do
                if i mod 10 <> 0 then continue;
                else
                    putFloatLn(i / 10);
        end
        """
        expect = "9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_return_585(self):
        input = """
        procedure main();
        begin
            if true then return;
            else putString("HUYTC");
        end
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_return_586(self):
        input = """
        function fib(n:integer):integer; //calculate the nth Fibonacci number
        begin
            if n < 0 then return -1;
            else if n = 0 then return 0;
            else if n = 1 then return 1;
            else return fib(n - 1) + fib(n - 2);
        end

        procedure main();
        var i : integer;
        begin
            putIntLn(fib(-100));
            for i := 0 to 10 do
                putIntLn(fib(i));
        end
        """
        expect = "-1\n0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_return_587(self):
        input = """
        procedure foo(i:integer);
        begin
            if i >= 0 then
            begin
                putStringLn("POSITIVE");
                return;
            end
            putStringLn("NEGATIVE");
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
        expect = "POSITIVE\nPOSITIVE\nPOSITIVE\nNEGATIVE\nNEGATIVE\nPOSITIVE\n"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_with_588(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:integer; do
            begin
                i := 8;
                putIntLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_with_589(self):
        input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:real; do
            begin
                i := 8;
                putFloatLn(i);
            end
            putIntLn(i);
        end
        """
        expect = "0\n8.0\n0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_with_590(self):
        input = """
        var i : integer;
        procedure foo();
        begin
            i := 0;
            putint(i);
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
            putint(i);
            foo();
            putint(i);
        end
        """
        expect = "-10true-1"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_call_591(self):
        input = """
        procedure printSum(a,b,c:integer);
        begin
            putIntLn(a+b+c);
            a := 0;
            b := 0;
            c := 0;
        end

        procedure main();
        var a : integer;
        begin
            a := 1;
            printSum(a, 6, 7);
            putIntLn(a);
        end
        """
        expect = "14\n1\n"
        self.assertTrue(TestCodeGen.test(input, expect, 591))


    def test_call_595(self):
        input = """
        function sum(a,b:integer):integer;
        begin
            return a + b;
        end

        procedure main();
        begin
            putInt(sum(1,10) - sum(10,1));
        end
        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 595))


    def test_call_598(self):
        input = """
        procedure print(s:string);
        begin
            putStringLn(s);
        end

        function helloWorld():String;
        begin
            return "HELLO WORLD";
        end

        procedure main();
        begin
            print("TEST");
            print(helloWorld());
        end
        """
        expect = "TEST\nHELLO WORLD\n"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_call_599(self):
        input = """
        function finalTest():real;
        begin
            return 420/420;
        end

        procedure main();
        begin
            putFloatLn(100*finalTest()*100 - 1e4);
        end
        """
        expect = "0.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 599))