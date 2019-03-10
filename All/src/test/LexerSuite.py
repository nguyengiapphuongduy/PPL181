import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1_identifier(self):
        """test normal identifiers"""
        self.assertTrue(TestLexer.test('abc','abc,<EOF>',101))
    def test_2_identifier(self):
        """test lower-upper mixing identifiers"""
        self.assertTrue(TestLexer.test('aCBbdc','aCBbdc,<EOF>',102))
    def test_3_int(self):
        """integer"""
        self.assertTrue(TestLexer.test('-1','-,1,<EOF>',103))
    def test_4_real_short(self):
        """only int part"""
        self.assertTrue(TestLexer.test('1.','1.,<EOF>',104))
    def test_5_real_short2(self):
        """only fraction part"""
        self.assertTrue(TestLexer.test('-.1','-,.1,<EOF>',105))
    def test_6_real_redun(self):
        """redundant"""
        self.assertTrue(TestLexer.test('-1.1.1','-,1.1,.1,<EOF>',106))
    def test_7_real_exp(self):
        """wrong exponent part"""
        self.assertTrue(TestLexer.test('-1.1e','-,1.1,e,<EOF>',107))
    def test_8_real_full(self):
        """full real number"""
        self.assertTrue(TestLexer.test('-1.2e-3.4','-,1.2e-3,.4,<EOF>',108))
    def test_9_string(self):
        """normal string"""
        self.assertTrue(TestLexer.test('"abc"','abc,<EOF>',109))
    def test_10_integer(self):
        """test wrong integers"""
        self.assertTrue(TestLexer.test('123a123','123,a123,<EOF>',110))
    def test_11_bool(self):
        """normal boolean"""
        self.assertTrue(TestLexer.test('true+false','true,+,false,<EOF>',111))
    def test_12_doubledot(self):
        """.."""
        self.assertTrue(TestLexer.test('1..2','1.,.2,<EOF>',112))
    def test_13_array_type(self):
        """array type"""
        self.assertTrue(TestLexer.test('array[1 .. 10]of integer','array,[,1,..,10,],of,integer,<EOF>',113))
    def test_14_escape(self):
        """ escape \ """
        input = '" \ "'
        self.assertTrue(TestLexer.test(input,'Illegal Escape In String:  \ ',114))
    def test_15_unclosed_string(self):
        """unclosed string"""
        input = '" abc'
        self.assertTrue(TestLexer.test(input,'Unclosed String:  abc',115))
    def test_16_unclosed_string(self):
        """unclosed string"""
        input = """ " abc

"""
        self.assertTrue(TestLexer.test(input,'Unclosed String:  abc',116))
    def test_17_escape(self):
        input = '" abc \n xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,117))
    def test_18_escape(self):
        input = '" abc \\n xyz "'
        expect = ' abc \\n xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,118))
    def test_19_escape(self):
        input = '" abc \b xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,119))
    def test_20_escape(self):
        input = '" abc \\b xyz "'
        expect = ' abc \\b xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,120))
    def test_21_escape(self):
        input = '" abc \r xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,121))
    def test_22_escape(self):
        input = '" abc \\r xyz "'
        expect = ' abc \\r xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,122))
    def test_23_escape(self):
        input = '" abc \f xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,123))
    def test_24_escape(self):
        input = '" abc \\f xyz "'
        expect = ' abc \\f xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,124))
    def test_25_escape(self):
        input = '" abc \t xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,125))
    def test_26_escape(self):
        input = '" abc \\t xyz "'
        expect = ' abc \\t xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,126))
    def test_27_escape(self):
        input = '" abc \' xyz "'
        expect = 'Unclosed String:  abc '
        self.assertTrue(TestLexer.test(input,expect,127))
    def test_28_escape(self):
        input = """ " abc \\' xyz " """
        expect = """ abc \\' xyz ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,128))
    def test_29_escape(self):
        input = '" abc \\" xyz "'
        expect = ' abc \\" xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,129))
    def test_30_escape(self):
        input = '" abc \" xyz "'
        expect = ' abc ,xyz,Unclosed String: '
        self.assertTrue(TestLexer.test(input,expect,130))
    def test_31_escape(self):
        input = '" abc \\ xyz "'
        expect = 'Illegal Escape In String:  abc \\ '
        self.assertTrue(TestLexer.test(input,expect,131))
    def test_32_escape(self):
        input = '" abc \\\\ xyz "'
        expect = ' abc \\\\ xyz ,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,132))
    def test_33_real(self):
        input = '1.2'
        expect = '1.2,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,133))
    def test_34_real(self):
        input = '1.'
        expect = '1.,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,134))
    def test_35_real(self):
        input = '.1'
        expect = '.1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,135))
    def test_36_real(self):
        input = '1e2'
        expect = '1e2,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,136))
    def test_37_real(self):
        input = '1.2E-2'
        expect = '1.2E-2,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,137))
    def test_38_real(self):
        input = '1.2e-2'
        expect = '1.2e-2,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,138))
    def test_39_real(self):
        input = '.1E2'
        expect = '.1E2,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,139))
    def test_40_real(self):
        input = '9.0'
        expect = '9.0,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,140))
    def test_41_real(self):
        input = '12e8'
        expect = '12e8,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,141))
    def test_42_real(self):
        input = '0.33E-3'
        expect = '0.33E-3,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,142))
    def test_43_real(self):
        input = '128e-42'
        expect = '128e-42,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,143))
    def test_44_real(self):
        input = 'e-12'
        expect = 'e,-,12,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,144))
    def test_45_real(self):
        input = '143e'
        expect = '143,e,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,145))
    def test_46_real(self):
        input = 'procedure main(); begin end'
        expect = 'procedure,main,(,),;,begin,end,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,146))
    def test_47_real(self):
        input = 'var a,b,c:integer;'
        expect = 'var,a,,,b,,,c,:,integer,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,147))
    def test_48_real(self):
        input = 'd: array[1 .. 5] of real;'
        expect = 'd,:,array,[,1,..,5,],of,real,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,148))
    def test_49_real(self):
        input = 'x:=1+1-2*3 div 4 mod 5/6'
        expect = 'x,:=,1,+,1,-,2,*,3,div,4,mod,5,/,6,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,149))
    def test_50_real(self):
        input = 'x:=y:=z:=1'
        expect = 'x,:=,y,:=,z,:=,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,150))
    def test_51_real(self):
        input = 'f()[1]>1'
        expect = 'f,(,),[,1,],>,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,151))
    def test_52_real(self):
        input = 'aa:=b[10]:=foo()[3]:=x:=1'
        expect = 'aa,:=,b,[,10,],:=,foo,(,),[,3,],:=,x,:=,1,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,152))
    def test_53_real(self):
        input = 'x := "abcxyz";'
        expect = 'x,:=,abcxyz,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,153))
    def test_54_real(self):
        input = 'x := 1.1e-5;'
        expect = 'x,:=,1.1e-5,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,154))
    def test_55_real(self):
        input = 'x := FALSE and then true;'
        expect = 'x,:=,FALSE,and,then,true,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,155))
    def test_56_real(self):
        input = '(1<2)<>(2<3)'
        expect = '(,1,<,2,),<>,(,2,<,3,),<EOF>'
        self.assertTrue(TestLexer.test(input,expect,156))
    def test_57_real(self):
        input = '123asdf123asdf'
        expect = '123,asdf123asdf,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,157))
    def test_58_real(self):
        input = 'procedure main () ;'
        expect = 'procedure,main,(,),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,158))
    def test_59_real(self):
        input = 'True1False'
        expect = 'True1False,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,159))
    def test_60_real(self):
        input = 'True(True'
        expect = 'True,(,True,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,160))
    def test_61_real(self):
        input = 'boolean:true+false'
        expect = 'boolean,:,true,+,false,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,161))
    def test_62_real(self):
        input = 'x := fu(g(k)+asdf(asdf(-1))/xxxx);'
        expect = 'x,:=,fu,(,g,(,k,),+,asdf,(,asdf,(,-,1,),),/,xxxx,),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,162))
    def test_63_real(self):
        input = '123e-45.67'
        expect = '123e-45,.67,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,163))
    def test_64_real(self):
        input = '-123E-45.67'
        expect = '-,123E-45,.67,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,164))
    def test_65_real(self):
        input = """procedure main () ;
        begin
            while (True) do 
            begin
            end
        end"""
        expect = 'procedure,main,(,),;,begin,while,(,True,),do,begin,end,end,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,165))
    def test_66_real(self):
        input = 'do do dododo'
        expect = 'do,do,dododo,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,166))
    def test_67_real(self):
        input = '{asdf\}'
        expect = '<EOF>'
        self.assertTrue(TestLexer.test(input,expect,167))
    def test_68_real(self):
        input = """//aalsdkfjoinv\\b\\f\\c\\r\\n\\t\\a"""
        expect = '<EOF>'
        self.assertTrue(TestLexer.test(input,expect,168))
    def test_69_real(self):
        input = '123aaa(*mmm*)ddd'
        expect = '123,aaa,ddd,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,169))
    def test_70_real(self):
        input = 'True***False'
        expect = 'True,*,*,*,False,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,170))
    def test_71_real(self):
        input = 'begin bullasdfshitqwenm(); end;;;;'
        expect = 'begin,bullasdfshitqwenm,(,),;,end,;,;,;,;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,171))
    def test_72_real(self):
        input = 'with a,b:integer;c:array[1 .. 2]of real; do'
        expect = 'with,a,,,b,:,integer,;,c,:,array,[,1,..,2,],of,real,;,do,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,172))
    def test_73_real(self):
        input = 'fuuuuu(f(a)[-1]+g(b));'
        expect = 'fuuuuu,(,f,(,a,),[,-,1,],+,g,(,b,),),;,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,173))
    def test_74_real(self):
        input = '**xxx111++--22e3--4ee!'
        expect = '*,*,xxx111,+,+,-,-,22e3,-,-,4,ee,Error Token !'
        self.assertTrue(TestLexer.test(input,expect,174))
    def test_75_real(self):
        input = '@'
        expect = 'Error Token @'
        self.assertTrue(TestLexer.test(input,expect,175))
    def test_76_real(self):
        input = '123@'
        expect = '123,Error Token @'
        self.assertTrue(TestLexer.test(input,expect,176))
    def test_77_real(self):
        input = '#'
        expect = 'Error Token #'
        self.assertTrue(TestLexer.test(input,expect,177))
    def test_78_real(self):
        input = '~123'
        expect = 'Error Token ~'
        self.assertTrue(TestLexer.test(input,expect,178))
    def test_79_real(self):
        input = '^x1234e4'
        expect = 'Error Token ^'
        self.assertTrue(TestLexer.test(input,expect,179))
    def test_80_real(self):
        input = 'True***False^^'
        expect = 'True,*,*,*,False,Error Token ^'
        self.assertTrue(TestLexer.test(input,expect,180))
    def test_81_real(self):
        input = '(x*x+x^2)'
        expect = '(,x,*,x,+,x,Error Token ^'
        self.assertTrue(TestLexer.test(input,expect,181))
    def test_82_real(self):
        input = 'Hi`'
        expect = 'Hi,Error Token `'
        self.assertTrue(TestLexer.test(input,expect,182))
    def test_83_real(self):
        input = 'Baby Shark Doo doo doo doo doo doo...'
        expect = 'Baby,Shark,Doo,doo,doo,doo,doo,doo,..,Error Token .'
        self.assertTrue(TestLexer.test(input,expect,183))
    def test_84_real(self):
        input = '....'
        expect = '..,..,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,184))
    def test_85_real(self):
        input = '... ...'
        expect = '..,Error Token .'
        self.assertTrue(TestLexer.test(input,expect,185))
    def test_86_real(self):
        input = '???'
        expect = 'Error Token ?'
        self.assertTrue(TestLexer.test(input,expect,186))
    def test_87_real(self):
        input = '<3<3<3'
        expect = '<,3,<,3,<,3,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,187))
    def test_88_real(self):
        input = '_'
        expect = '_,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,188))
    def test_89_real(self):
        input = '****You'
        expect = '*,*,*,*,You,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,189))
    def test_90_real(self):
        input = 'mail\@mail.com'
        expect = 'mail,Error Token \\'
        self.assertTrue(TestLexer.test(input,expect,190))
    def test_91_real(self):
        input = '"mail\@mail.com"'
        expect = 'Illegal Escape In String: mail\\@'
        self.assertTrue(TestLexer.test(input,expect,191))
    def test_92_real(self):
        input = '/ffffffffffff\f'
        expect = '/,ffffffffffff,Error Token \f'
        self.assertTrue(TestLexer.test(input,expect,192))
    def test_93_real(self):
        input = 'almost done..'
        expect = 'almost,done,..,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,193))
    def test_94_real(self):
        input = 'few more error /#'
        expect = 'few,more,error,/,Error Token #'
        self.assertTrue(TestLexer.test(input,expect,194))
    def test_95_real(self):
        input = 'another error \b'
        expect = 'another,error,Error Token \b'
        self.assertTrue(TestLexer.test(input,expect,195))
    def test_96_real(self):
        input = 'but there is no err,\r'
        expect = 'but,there,is,no,err,,,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,196))
    def test_97_real(self):
        input = '\n'
        expect = '<EOF>'
        self.assertTrue(TestLexer.test(input,expect,197))
    def test_98_real(self):
        input = 'also//\n'
        expect = 'also,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,198))
    def test_99_real(self):
        input = """PROCEDURE main(); BEGIN
            ffffffffff(a[0][0][0])[1][2][a[3]]:=false or true;
        END"""
        expect = 'PROCEDURE,main,(,),;,BEGIN,ffffffffff,(,a,[,0,],[,0,],[,0,],),[,1,],[,2,],[,a,[,3,],],:=,false,or,true,;,END,<EOF>'
        self.assertTrue(TestLexer.test(input,expect,199))
    def test_00_real(self):
        input = 'Finally done :(((( !!!'
        expect = 'Finally,done,:,(,(,(,(,Error Token !'
        self.assertTrue(TestLexer.test(input,expect,100))
