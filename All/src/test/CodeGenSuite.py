import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
	def test_0_int(self):
		input = """procedure main(); begin putInt(1); end"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input, expect, 500))

	def test_1_int(self):
		input = """procedure main(); begin putInt(-1); end"""
		expect = "-1"
		self.assertTrue(TestCodeGen.test(input, expect, 501))

	def test_2_float(self):
		input = """procedure main(); begin putFloat(1.0); end"""
		expect = "1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 502))

	def test_3_float(self):
		input = """procedure main(); begin putFloat(-1.0); end"""
		expect = "-1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 503))

	def test_4_int_to_float(self):
		input = """procedure main(); begin putFloat(1); end"""
		expect = "1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 504))

	def test_5_bool_true(self):
		input = """procedure main(); begin putBool(true); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 505))

	def test_6_bool_false(self):
		input = """procedure main(); begin putBool(False); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 506))

	def test_7_int8(self):
		input = """procedure main(); begin putInt(127); end"""
		expect = "127"
		self.assertTrue(TestCodeGen.test(input, expect, 507))

	def test_8_int8(self):
		input = """procedure main(); begin putInt(-128); end"""
		expect = "-128"
		self.assertTrue(TestCodeGen.test(input, expect, 508))

	def test_9_int16(self):
		input = """procedure main(); begin putInt(32767); end"""
		expect = "32767"
		self.assertTrue(TestCodeGen.test(input, expect, 509))

	def test_10_int16(self):
		input = """procedure main(); begin putInt(-32768); end"""
		expect = "-32768"
		self.assertTrue(TestCodeGen.test(input, expect, 510))

	def test_11_int32(self):
		input = """procedure main(); begin putInt(2147483647); end"""
		expect = "2147483647"
		self.assertTrue(TestCodeGen.test(input, expect, 511))

	def test_12_int32(self):
		input = """procedure main(); begin putInt(-2147483648); end"""
		expect = "-2147483648"
		self.assertTrue(TestCodeGen.test(input, expect, 512))

	def test_13_string(self):
		input = """procedure main(); begin putString("something"); end"""
		expect = "something"
		self.assertTrue(TestCodeGen.test(input, expect, 513))

	def test_14_special_char(self):
		input = """procedure main(); begin putString("some\\tthing"); end"""
		expect = "some\tthing"
		self.assertTrue(TestCodeGen.test(input, expect, 514))

	def test_15_add_op(self):
		input = """procedure main(); begin putInt(1 + 9); end"""
		expect = "10"
		self.assertTrue(TestCodeGen.test(input, expect, 515))

	def test_16_add_op(self):
		input = """procedure main(); begin putFloat(1 + 9.); end"""
		expect = "10.0"
		self.assertTrue(TestCodeGen.test(input, expect, 516))

	def test_17_sub_op(self):
		input = """procedure main(); begin putFloat(1 - 9); end"""
		expect = "-8.0"
		self.assertTrue(TestCodeGen.test(input, expect, 517))

	def test_18_mul_op(self):
		input = """procedure main(); begin putFloat(1 * 9); end"""
		expect = "9.0"
		self.assertTrue(TestCodeGen.test(input, expect, 518))

	def test_19_div_op(self):
		input = """procedure main(); begin putFloat(1 / 9.0); end"""
		expect = "0.11111111"
		self.assertTrue(TestCodeGen.test(input, expect, 519))

	def test_20_div_op(self):
		input = """procedure main(); begin putFloat(9 / 1); end"""
		expect = "9.0"
		self.assertTrue(TestCodeGen.test(input, expect, 520))

	def test_21_float(self):
		input = """procedure main(); begin putFloat(2.1-2.0); end"""
		expect = "0.099999905"
		self.assertTrue(TestCodeGen.test(input, expect, 521))

	def test_22_float(self):
		input = """procedure main(); begin putFloat(2.5-2.0); end"""
		expect = "0.5"
		self.assertTrue(TestCodeGen.test(input, expect, 522))

	def test_23_div_op(self):
		input = """procedure main(); begin putInt(7 div 3); end"""
		expect = "2"
		self.assertTrue(TestCodeGen.test(input, expect, 523))

	def test_24_mod_op(self):
		input = """procedure main(); begin putInt(7 mod 3); end"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input, expect, 524))

	def test_25_gt_op_int(self):
		input = """procedure main(); begin putBool(7 > 3); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 525))

	def test_26_ge_op_int(self):
		input = """procedure main(); begin putBool(7 >= 3); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 526))

	def test_27_lt_op_int(self):
		input = """procedure main(); begin putBool(7 < 3); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 527))

	def test_28_le_op_int(self):
		input = """procedure main(); begin putBool(7 <= 3); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 528))

	def test_29_eq_op_int(self):
		input = """procedure main(); begin putBool(7 = 3); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 529))

	def test_30_ne_op_int(self):
		input = """procedure main(); begin putBool(7 <> 3); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 530))

	def test_31_gt_op_float(self):
		input = """procedure main(); begin putBool(7 > 3.0); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 531))

	def test_32_ge_op_float(self):
		input = """procedure main(); begin putBool(7.0 >= 3); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 532))

	def test_33_lt_op_float(self):
		input = """procedure main(); begin putBool(7 < 3.); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 533))

	def test_34_le_op_float(self):
		input = """procedure main(); begin putBool(7. <= 3); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 534))

	def test_35_eq_op_float(self):
		input = """procedure main(); begin putBool(7 = 3); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 535))

	def test_36_eq_op_float(self):
		"""Float is not exact"""
		input = """procedure main(); begin putBool(2.1-2.0 = 1.1-1.0); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 536))

	def test_37_ne_op_float(self):
		input = """procedure main(); begin putBool(7 <> 3); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 537))

	def test_38_notop(self):
		input = """procedure main(); begin putBool(not(1>0)); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 538))

	def test_39_var_global(self):
		input = """var x: integer; procedure main(); begin x:=10; putint(x); end"""
		expect = "10"
		self.assertTrue(TestCodeGen.test(input, expect, 539))

	def test_40_var_local(self):
		input = """procedure main(); var x: integer; begin x:=1; putint(x); end"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input, expect, 540))

	def test_41_callexpr_int(self):
		input = """procedure main(); var x:integer; begin x:=foo(10); putInt(x); end
		function foo(x:integer):integer; begin return x; end"""
		expect = "10"
		self.assertTrue(TestCodeGen.test(input, expect, 541))

	def test_42_callexpr_float(self):
		input = """procedure main(); var x:real; begin x:=foo(10); putFloat(x); end
		function foo(x:real):real; begin return x; end"""
		expect = "10.0"
		self.assertTrue(TestCodeGen.test(input, expect, 542))

	def test_43_callexpr_bool(self):
		input = """procedure main(); var x:boolean; begin x:=foo(true); putBoolLn(x); end
		function foo(x:boolean):boolean; begin return x; end"""
		expect = "true\n"
		self.assertTrue(TestCodeGen.test(input, expect, 543))

	def test_44_callexpr_coerce(self):
		input = """procedure main(); var x:real; begin x:=foo(10); putFloat(x); end
		function foo(x:integer):real; begin return x; end"""
		expect = "10.0"
		self.assertTrue(TestCodeGen.test(input, expect, 544))

	def test_45_callexpr_string(self):
		input = """procedure main(); begin putString(foo("something")); end
		function foo(x:string):string; begin return x; end"""
		expect = "something"
		self.assertTrue(TestCodeGen.test(input, expect, 545))

	def test_46_with(self):
		input = """procedure main(); var x:real; begin
		x:=1; with x:boolean; do begin x:=true; putBool(x); end
		putFloat(x); end"""
		expect = "true1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 546))

	def test_47_with_nested(self):
		input = """procedure main(); var x:real; begin
		x:=1; with x:boolean; do begin x:=true;
			with x:integer; do begin x:=2; putInt(x); end
			putBool(x); end
		putFloat(x); end"""
		expect = "2true1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 547))

	def test_48_with_more_nested(self):
		input = """var x:integer; procedure main(); var x:real; begin
		x:=1; with x:boolean; do begin x:=true;
			with x:integer; do begin x:=2; putInt(x); end
			putBool(x); end
		putFloat(x); f(); end
		procedure f(); begin x:=-1; putFloat(x); end"""
		expect = "2true1.0-1.0"
		self.assertTrue(TestCodeGen.test(input, expect, 548))

	def test_49_if(self):
		input = """procedure main(); begin foo(10); end
		procedure foo(x:integer); begin if (x>0) then putBool(true); end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 549))

	def test_50_if(self):
		input = """procedure main(); begin foo(-10); end
		procedure foo(x:integer); begin if (x>0) then putBool(true); else putBool(false); end"""
		expect = "false"
		self.assertTrue(TestCodeGen.test(input, expect, 550))

	def test_51_if(self):
		input = """procedure main(); begin putInt(foo(1,1)); putInt(foo(1,-1)); putInt(foo(-1,1)); putInt(foo(-1,-1)); end
		function foo(x:integer; y:real):integer;
		begin if (x>0) then if (y>0) then return 1; else return 2;
		else if (y>0) then return 3; else return 4; end"""
		expect = "1234"
		self.assertTrue(TestCodeGen.test(input, expect, 551))

	def test_52_if(self):
		input = """procedure main(); begin putFloat(foo(1,1)); putFloat(foo(1,-1)); putFloat(foo(-1,1)); putFloat(foo(-1,-1)); end
		function foo(x:integer; y:real):real; begin
		if (x>0) then if (y>0) then return x + y; else return x - y;
		else if (y>0) then return -x + y; else return -x - y; end"""
		expect = "2.02.02.02.0"
		self.assertTrue(TestCodeGen.test(input, expect, 552))

	def test_53_return_procedure(self):
		input = """procedure main(); begin foo(1,-1); end
		procedure foo(x:integer; y:real); begin if (x<y) then return; putInt(1); end"""
		expect = "1"
		self.assertTrue(TestCodeGen.test(input, expect, 553))

	def test_54_return_function(self):
		input = """procedure main(); begin putBool(foo(1,-1)); end
		function foo(x:integer; y:real):boolean; begin putInt(0); if (x>y) then return true; else return false; end"""
		expect = "0true"
		self.assertTrue(TestCodeGen.test(input, expect, 554))

	def test_55_return_string(self):
		input = """procedure main(); begin putString(foo(true)); end
		function foo(x:boolean):string; begin putInt(0); if x then return "True"; else return "False"; end"""
		expect = "0True"
		self.assertTrue(TestCodeGen.test(input, expect, 555))

	def test_56_while(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin
		putInt(0); y:=0; while y<x do begin y:=y+1;putInt(y);end end"""
		expect = "012345"
		self.assertTrue(TestCodeGen.test(input, expect, 556))

	def test_57_while_nothing(self):
		input = """procedure main(); begin foo(-1); end
		procedure foo(x:integer); var y:integer; begin
		y:=0; while y<x do begin y:=y+1;putInt(y);end end"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input, expect, 557))

	def test_58_break_while(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin y:=0;
		while y<x do begin y:=y+1; if y=3 then break; putInt(y); end end"""
		expect = "12"
		self.assertTrue(TestCodeGen.test(input, expect, 558))

	def test_59_continue_while(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin y:=0;
		while y<x do begin y:=y+1; if y=3 then continue; putInt(y); end end"""
		expect = "1245"
		self.assertTrue(TestCodeGen.test(input, expect, 559))

	def test_60_for(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin for y:=1 to x do putInt(y); end"""
		expect = "12345"
		self.assertTrue(TestCodeGen.test(input, expect, 560))

	def test_61_for_nothing(self):
		input = """procedure main(); begin foo(0); end
		procedure foo(x:integer); var y:integer; begin for y:=1 to x do putInt(y); end"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input, expect, 561))

	def test_62_break_for(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin for y:=1 to x do begin if y=3 then break; putInt(y); end end"""
		expect = "12"
		self.assertTrue(TestCodeGen.test(input, expect, 562))

	def test_63_continue_for(self):
		input = """procedure main(); begin foo(5); end
		procedure foo(x:integer); var y:integer; begin for y:=1 to x do begin if y=3 then continue; putInt(y); end end"""
		expect = "1245"
		self.assertTrue(TestCodeGen.test(input, expect, 563))

	def test_64_for_down(self):
		input = """procedure main(); begin foo(1); end
		procedure foo(x:integer); var y:integer; begin for y:=5 downto x do putInt(y); end"""
		expect = "54321"
		self.assertTrue(TestCodeGen.test(input, expect, 564))

	def test_65_break_for_down(self):
		input = """procedure main(); begin foo(1); end
		procedure foo(x:integer); var y:integer; begin for y:=5 downto x do begin if y=3 then break; putInt(y); end end"""
		expect = "54"
		self.assertTrue(TestCodeGen.test(input, expect, 565))

	def test_66_continue_for_down(self):
		input = """procedure main(); begin foo(1); end
		procedure foo(x:integer); var y:integer; begin for y:=5 downto x do begin if y=3 then continue; putInt(y); end end"""
		expect = "5421"
		self.assertTrue(TestCodeGen.test(input, expect, 566))

	def test_67_short_circuit_andthen(self):
		input = """procedure main(); var x:real; begin
		if (f(2) and then f(1) and then f(0) and then f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x>2 then return true; else return false; end"""
		expect = "2"
		self.assertTrue(TestCodeGen.test(input, expect, 567))

	def test_68_short_circuit_andthen(self):
		input = """procedure main(); var x:real; begin
		if (f(2) and then f(1) and then f(0) and then f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x>1 then return true; else return false; end"""
		expect = "21"
		self.assertTrue(TestCodeGen.test(input, expect, 568))

	def test_69_short_circuit_andthen(self):
		input = """procedure main(); var x:real; begin
		if (f(2) and then f(1) and then f(0) and then f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x>0 then return true; else return false; end"""
		expect = "210"
		self.assertTrue(TestCodeGen.test(input, expect, 569))

	def test_70_short_circuit_andthen(self):
		input = """procedure main(); var x:real; begin
		if (f(2) and then f(1) and then f(0) and then f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x>-1 then return true; else return false; end"""
		expect = "210-1"
		self.assertTrue(TestCodeGen.test(input, expect, 570))

	def test_71_short_circuit_andthen(self):
		input = """procedure main(); var x:real; begin
		if (f(2) and then f(1) and then f(0) and then f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x>-2 then return true; else return false; end"""
		expect = "210-1passed"
		self.assertTrue(TestCodeGen.test(input, expect, 571))

	def test_72_short_circuit_orelse(self):
		input = """procedure main(); var x:real; begin
		if (f(2) or else f(1) or else f(0) or else f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x<3 then return true; else return false; end"""
		expect = "2passed"
		self.assertTrue(TestCodeGen.test(input, expect, 572))

	def test_73_short_circuit_orelse(self):
		input = """procedure main(); var x:real; begin
		if (f(2) or else f(1) or else f(0) or else f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x<2 then return true; else return false; end"""
		expect = "21passed"
		self.assertTrue(TestCodeGen.test(input, expect, 573))

	def test_74_short_circuit_orelse(self):
		input = """procedure main(); var x:real; begin
		if (f(2) or else f(1) or else f(0) or else f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x<1 then return true; else return false; end"""
		expect = "210passed"
		self.assertTrue(TestCodeGen.test(input, expect, 574))

	def test_75_short_circuit_orelse(self):
		input = """procedure main(); var x:real; begin
		if (f(2) or else f(1) or else f(0) or else f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x<0 then return true; else return false; end"""
		expect = "210-1passed"
		self.assertTrue(TestCodeGen.test(input, expect, 575))

	def test_76_short_circuit_orelse(self):
		input = """procedure main(); var x:real; begin
		if (f(2) or else f(1) or else f(0) or else f(-1)) then putString("passed"); end
		function f(x:integer):boolean; begin putInt(x); if x<-1 then return true; else return false; end"""
		expect = "210-1"
		self.assertTrue(TestCodeGen.test(input, expect, 576))

	def test_77_misc(self):
		input = """procedure main(); begin putFloat(foo(1)); putFloat(foo(0)); end
		function foo(x:integer):real; begin putInt(x);
		with a:real; do begin a:=0.5; if x<a then return a; end return x; end"""
		expect = "11.000.5"
		self.assertTrue(TestCodeGen.test(input, expect, 577))

	def test_78_misc_recursive(self):
		input = """procedure main(); begin putInt(f(5)); end
		function f(x:integer):integer; begin if x=1 then return 1; else return x*f(x-1); end"""
		expect = "120"
		self.assertTrue(TestCodeGen.test(input, expect, 578))

	def test_79_misc_recursive(self):
		input = """procedure main(); begin putInt(f(5)); end
		function f(x:integer):integer; begin if x=1 then return 1; else return x*g(x-1); end
		function g(x:integer):integer; begin if x=2 then return 1; else return x*f(x-1); end"""
		expect = "60"
		self.assertTrue(TestCodeGen.test(input, expect, 579))

	def test_80_misc_swap(self):
		input = """procedure main(); var x,y:integer; begin
		x:=-100; y:=200; putInt(x); putInt(y);
		with a:integer; do begin a:=x; x:=y; y:=a; end
		putInt(x); putInt(y); end"""
		expect = "-100200200-100"
		self.assertTrue(TestCodeGen.test(input, expect, 580))

	def test_81_misc_swap(self):
		"""Pass by value, swap in function wont work"""
		input = """procedure main(); var x,y:integer; begin
		x:=-100; y:=200; putInt(x); putInt(y); swap(x,y); putInt(x); putInt(y); end
		procedure swap(x,y:integer); begin with a:integer; do begin a:=x; x:=y; y:=a; end end"""
		expect = "-100200-100200"
		self.assertTrue(TestCodeGen.test(input, expect, 581))

	def test_82_misc_prime_number(self):
		input = """procedure main(); begin putBool(prim(13)); putBool(prim(4)); end
		function prim(x:integer):boolean; var i:integer; begin for i:=2 to x-1 do if x mod i = 0 then return false; return true; end"""
		expect = "truefalse"
		self.assertTrue(TestCodeGen.test(input, expect, 582))

	def test_83_misc_prime_number_use_while(self):
		input = """procedure main(); begin putBool(prim(13)); putBool(prim(4)); end
		function prim(x:integer):boolean; var i:integer;
		begin if x<=1 then return false; i:=2; while i<=x-1 do begin if x mod i = 0 then return false; i:=i+1; end return true; end"""
		expect = "truefalse"
		self.assertTrue(TestCodeGen.test(input, expect, 583))

	def test_84_misc_count_prime_number(self):
		input = """procedure main(); begin putInt(countPrim(20)); end
		function prim(x:integer):boolean; var i:integer;
		begin if x<=1 then return false; for i:=2 to x-1 do if x mod i = 0 then return false; return true; end
		function countPrim(x:integer):integer; var i,a:integer; begin a:=0; for i:=1 to x do if prim(i) then a:=a+1; return a; end"""
		expect = "8"
		self.assertTrue(TestCodeGen.test(input, expect, 584))

	def test_85_misc(self):
		input = """procedure main(); var a: integer; begin putInt(foo(foo(foo(5)))); end
		function foo(x:integer):integer; begin putInt(x); return x - 1; end"""
		expect = "5432"
		self.assertTrue(TestCodeGen.test(input, expect, 585))

	def test_86_misc_power_calc(self):
		input = """procedure main(); var a: integer; begin putInt(power(2,3)); end
		function power(x,y:integer):integer; var i,r:integer; begin r:=1; for i:=1 to y do r:=r*x; return r; end"""
		expect = "8"
		self.assertTrue(TestCodeGen.test(input, expect, 586))

	def test_87_misc_power_calc_recursive(self):
		input = """procedure main(); var a: integer; begin putInt(power(2,3)); end
		function power(x,y:integer):integer; begin if y=0 then return 1; else return x*power(x,y-1); end"""
		expect = "8"
		self.assertTrue(TestCodeGen.test(input, expect, 587))

	def test_88_misc_complex_if_else(self):
		input = """procedure main(); var a: integer; begin putFloat(max(1,4,2,3)); end
		function max(x,y,z,t:integer):real; begin 
		if x>y then
			if x>z then
				if x>t then
					return x;
				else
					return t;
			else
				if z>t then
					return z;
				else
					return t;
		else
			if y>z then
				if y>t then
					return y;
				else
					return t;
			else
				if z>t then
					return z;
				else
					return t;
		end"""
		expect = "4.0"
		self.assertTrue(TestCodeGen.test(input, expect, 588))

	def test_89_misc_print_factors(self):
		input = """procedure main(); var a: integer; begin putBool(prim(15)); end
		function prim(x:integer):boolean; var i:integer; a:boolean;
		begin a:=true; for i:=2 to x-1 do if x mod i = 0 then begin putInt(i); a:=false; end return a; end"""
		expect = "35false"
		self.assertTrue(TestCodeGen.test(input, expect, 589))

	def test_90_misc_print_factors(self):
		input = """procedure main(); var a: integer; begin putBool(prim(17)); end
		function prim(x:integer):boolean; var i:integer; a:boolean;
		begin a:=true; for i:=2 to x-1 do if x mod i = 0 then begin putInt(i); a:=false; end return a; end"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 590))

	def test_91_misc(self):
		input = """var a,b:integer;
		procedure notMain(d:integer; e,f:real); begin putFloat(e+f); return; end
		procedure main(); var x,y:integer; b:boolean; z:real;
		begin
			x:=1; z:=8.9;
			notMAIN(x,1,z);
			putFLOAT(z);
		end"""
		expect = "9.98.9"
		self.assertTrue(TestCodeGen.test(input, expect, 591))

	def test_92_misc(self):
		input = """function foo(x,y,z,t:integer):integer;
		begin if x>y and then z>t then return y+z; else return x+t; end
		procedure main(); begin putInt(foo(1,foo(3,2,1,0),3,foo(5,6,7,8))); end"""
		expect = "14"
		self.assertTrue(TestCodeGen.test(input, expect, 592))

	def test_93_misc(self):
		input = """function foo(x,y,z,t:integer):integer;
		begin if x>y and then z>t then return y+z; else return x+t; end
		procedure main(); begin putInt(foo(4,foo(3,2,1,0),14,foo(5,6,7,8))); end"""
		expect = "17"
		self.assertTrue(TestCodeGen.test(input, expect, 593))

	def test_94_misc(self):
		input = """function foo(x,y,z,t:integer):integer;
		begin if x>y and then z>t then return y+z; else return x+t; end
		function power(x,y:integer):integer; var i,r:integer; begin r:=1; for i:=1 to y do r:=r*x; return r; end
		procedure main(); begin putInt(foo(4,foo(3,2,1,0),power(3,4),foo(5,6,7,8))); end"""
		expect = "84"
		self.assertTrue(TestCodeGen.test(input, expect, 594))

	def test_95_misc_gcd_loop(self):
		input = """function gcd(a,b:integer):integer; var i,r:integer;
		begin r:=1; for i:=1 to max(a,b) do if a mod i = 0 and then b mod i = 0 then r:=i; return r; end
		function max(a,b:integer):integer; begin if a>b then return a; else return b; end
		procedure main(); begin putInt(gcd(35,60)); end"""
		expect = "5"
		self.assertTrue(TestCodeGen.test(input, expect, 595))

	def test_96_misc_gcd_recursive(self):
		input = """function gcd(a,b:integer):integer;
		begin if a=b then return a; if a>b then return gcd(a-b,b); else return gcd(a,b-a); end
		procedure main(); begin putInt(gcd(45,60)); end"""
		expect = "15"
		self.assertTrue(TestCodeGen.test(input, expect, 596))

	def test_97_misc_lcm(self):
		input = """function lcm(a,b:integer):integer; var r:integer;
		begin r:=a; while true do begin if r mod b = 0 then break; r:=r+a; end return r; end
		procedure main(); begin putInt(lcm(6,8)); end"""
		expect = "24"
		self.assertTrue(TestCodeGen.test(input, expect, 597))

	def test_98_misc(self):
		input = """function gcd(a,b:integer):integer;
		begin if a=b then return a; if a>b then return gcd(a-b,b); else return gcd(a,b-a); end
		function lcm(a,b:integer):integer; var r:integer;
		begin r:=a; while true do begin if r mod b = 0 then break; r:=r+a; end return r; end
		procedure main(); var a,b:integer; begin
			a:=1234; b:=44350;
			putString("GCD("); putInt(a); putString(", "); putInt(b); putString(") = ");
			putInt(gcd(a,b)); putLn();
			putString("LCM("); putInt(a); putString(", "); putInt(b); putString(") = ");
			putInt(lcm(a,b));
		end"""
		expect = "GCD(1234, 44350) = 2\nLCM(1234, 44350) = 27363950"
		self.assertTrue(TestCodeGen.test(input, expect, 598))

	def test_99_misc(self):
		"""This test is from MP.pdf"""
		input = """
		var i:integer; function f():integer; begin return 200; end
		procedure main(); var main:integer; begin
		main:=f(); putIntLn(main);
		with i:integer; main:integer; f:integer; do begin
			main:=f:=i:=100;
			putIntLn(i);
			putIntLn(main);
			putIntLn(f);
		end putIntLn(main); end
		var g:real;"""
		expect = "200\n100\n100\n100\n200\n"
		self.assertTrue(TestCodeGen.test(input, expect, 599))
