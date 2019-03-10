# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u024d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00c9")
        buf.write("\n\3\f\3\16\3\u00cc\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7")
        buf.write("\4\u00d5\n\4\f\4\16\4\u00d8\13\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\7\5\u00e2\n\5\f\5\16\5\u00e5\13\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\6\32\u0116")
        buf.write("\n\32\r\32\16\32\u0117\3\32\3\32\3\33\6\33\u011d\n\33")
        buf.write("\r\33\16\33\u011e\3\34\3\34\5\34\u0123\n\34\3\34\3\34")
        buf.write("\3\34\5\34\u0128\n\34\3\35\3\35\5\35\u012c\n\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\37\3\37\3\37\5\37\u0136\n\37\3\37")
        buf.write("\5\37\u0139\n\37\3 \6 \u013c\n \r \16 \u013d\3!\3!\5!")
        buf.write("\u0142\n!\3\"\3\"\3#\3#\5#\u0148\n#\3$\3$\3$\7$\u014d")
        buf.write("\n$\f$\16$\u0150\13$\3$\3$\3$\3$\3%\3%\3%\7%\u0159\n%")
        buf.write("\f%\16%\u015c\13%\3%\3%\3%\3&\3&\3&\7&\u0164\n&\f&\16")
        buf.write("&\u0167\13&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3")
        buf.write("A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3")
        buf.write("K\3K\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3N\3N\3N\3N\3N\3N\3")
        buf.write("N\3N\3N\3O\3O\3O\3O\3O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3Q\3")
        buf.write("Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\3S\3T\3T\3")
        buf.write("T\3U\3U\3U\3U\3U\3V\3V\3V\3V\3V\3V\3V\3V\3W\3W\3W\3W\3")
        buf.write("W\3W\3W\3W\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3")
        buf.write("Z\3[\3[\3[\3\\\3\\\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3^\3^")
        buf.write("\3_\5_\u0243\n_\3_\7_\u0246\n_\f_\16_\u0249\13_\3`\3`")
        buf.write("\3`\4\u00ca\u00d6\2a\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\2;\2=\2")
        buf.write("?\2A\36C\2E\2G\37I K!M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2")
        buf.write("c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081")
        buf.write("\"\u0083#\u0085$\u0087%\u0089&\u008b\'\u008d(\u008f)\u0091")
        buf.write("*\u0093+\u0095,\u0097-\u0099.\u009b/\u009d\60\u009f\61")
        buf.write("\u00a1\62\u00a3\63\u00a5\64\u00a7\65\u00a9\66\u00ab\67")
        buf.write("\u00ad8\u00af9\u00b1:\u00b3;\u00b5<\u00b7=\u00b9>\u00bb")
        buf.write("?\u00bd@\u00bfA\3\2#\4\2\f\f\17\17\5\2\13\f\17\17\"\"")
        buf.write("\3\2\62;\4\2GGgg\7\2\n\f\16\17$$))^^\17\2$$))DDHHPPTT")
        buf.write("VV^^ddhhppttvv\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2HHh")
        buf.write("h\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\5\2C\\aac|\6\2\62;C\\aac|\2\u023f\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2A\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2\u0081\3\2\2\2\2")
        buf.write("\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2")
        buf.write("\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3")
        buf.write("\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2")
        buf.write("\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1")
        buf.write("\3\2\2\2\5\u00c4\3\2\2\2\7\u00d2\3\2\2\2\t\u00dd\3\2\2")
        buf.write("\2\13\u00e8\3\2\2\2\r\u00ea\3\2\2\2\17\u00ec\3\2\2\2\21")
        buf.write("\u00ee\3\2\2\2\23\u00f0\3\2\2\2\25\u00f3\3\2\2\2\27\u00f5")
        buf.write("\3\2\2\2\31\u00f7\3\2\2\2\33\u00f9\3\2\2\2\35\u00fc\3")
        buf.write("\2\2\2\37\u00ff\3\2\2\2!\u0101\3\2\2\2#\u0103\3\2\2\2")
        buf.write("%\u0105\3\2\2\2\'\u0107\3\2\2\2)\u0109\3\2\2\2+\u010b")
        buf.write("\3\2\2\2-\u010d\3\2\2\2/\u010f\3\2\2\2\61\u0111\3\2\2")
        buf.write("\2\63\u0115\3\2\2\2\65\u011c\3\2\2\2\67\u0127\3\2\2\2")
        buf.write("9\u0129\3\2\2\2;\u012f\3\2\2\2=\u0138\3\2\2\2?\u013b\3")
        buf.write("\2\2\2A\u0141\3\2\2\2C\u0143\3\2\2\2E\u0145\3\2\2\2G\u0149")
        buf.write("\3\2\2\2I\u0155\3\2\2\2K\u0160\3\2\2\2M\u016a\3\2\2\2")
        buf.write("O\u016c\3\2\2\2Q\u016e\3\2\2\2S\u0170\3\2\2\2U\u0172\3")
        buf.write("\2\2\2W\u0174\3\2\2\2Y\u0176\3\2\2\2[\u0178\3\2\2\2]\u017a")
        buf.write("\3\2\2\2_\u017c\3\2\2\2a\u017e\3\2\2\2c\u0180\3\2\2\2")
        buf.write("e\u0182\3\2\2\2g\u0184\3\2\2\2i\u0186\3\2\2\2k\u0188\3")
        buf.write("\2\2\2m\u018a\3\2\2\2o\u018c\3\2\2\2q\u018e\3\2\2\2s\u0190")
        buf.write("\3\2\2\2u\u0192\3\2\2\2w\u0194\3\2\2\2y\u0196\3\2\2\2")
        buf.write("{\u0198\3\2\2\2}\u019a\3\2\2\2\177\u019c\3\2\2\2\u0081")
        buf.write("\u019e\3\2\2\2\u0083\u01a4\3\2\2\2\u0085\u01ad\3\2\2\2")
        buf.write("\u0087\u01b1\3\2\2\2\u0089\u01b4\3\2\2\2\u008b\u01bb\3")
        buf.write("\2\2\2\u008d\u01be\3\2\2\2\u008f\u01c1\3\2\2\2\u0091\u01c6")
        buf.write("\3\2\2\2\u0093\u01cb\3\2\2\2\u0095\u01d2\3\2\2\2\u0097")
        buf.write("\u01d8\3\2\2\2\u0099\u01de\3\2\2\2\u009b\u01e2\3\2\2\2")
        buf.write("\u009d\u01eb\3\2\2\2\u009f\u01f5\3\2\2\2\u00a1\u01f9\3")
        buf.write("\2\2\2\u00a3\u01fe\3\2\2\2\u00a5\u0204\3\2\2\2\u00a7\u020a")
        buf.write("\3\2\2\2\u00a9\u020d\3\2\2\2\u00ab\u0212\3\2\2\2\u00ad")
        buf.write("\u021a\3\2\2\2\u00af\u0222\3\2\2\2\u00b1\u0229\3\2\2\2")
        buf.write("\u00b3\u022d\3\2\2\2\u00b5\u0231\3\2\2\2\u00b7\u0234\3")
        buf.write("\2\2\2\u00b9\u0238\3\2\2\2\u00bb\u023c\3\2\2\2\u00bd\u0242")
        buf.write("\3\2\2\2\u00bf\u024a\3\2\2\2\u00c1\u00c2\7<\2\2\u00c2")
        buf.write("\u00c3\7?\2\2\u00c3\4\3\2\2\2\u00c4\u00c5\7*\2\2\u00c5")
        buf.write("\u00c6\7,\2\2\u00c6\u00ca\3\2\2\2\u00c7\u00c9\13\2\2\2")
        buf.write("\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00cb\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca")
        buf.write("\3\2\2\2\u00cd\u00ce\7,\2\2\u00ce\u00cf\7+\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\b\3\2\2\u00d1\6\3\2\2\2\u00d2\u00d6")
        buf.write("\5#\22\2\u00d3\u00d5\13\2\2\2\u00d4\u00d3\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\5")
        buf.write("%\23\2\u00da\u00db\3\2\2\2\u00db\u00dc\b\4\2\2\u00dc\b")
        buf.write("\3\2\2\2\u00dd\u00de\7\61\2\2\u00de\u00df\7\61\2\2\u00df")
        buf.write("\u00e3\3\2\2\2\u00e0\u00e2\n\2\2\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e2\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3")
        buf.write("\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7")
        buf.write("\b\5\2\2\u00e7\n\3\2\2\2\u00e8\u00e9\7-\2\2\u00e9\f\3")
        buf.write("\2\2\2\u00ea\u00eb\7/\2\2\u00eb\16\3\2\2\2\u00ec\u00ed")
        buf.write("\7\61\2\2\u00ed\20\3\2\2\2\u00ee\u00ef\7,\2\2\u00ef\22")
        buf.write("\3\2\2\2\u00f0\u00f1\7>\2\2\u00f1\u00f2\7@\2\2\u00f2\24")
        buf.write("\3\2\2\2\u00f3\u00f4\7?\2\2\u00f4\26\3\2\2\2\u00f5\u00f6")
        buf.write("\7>\2\2\u00f6\30\3\2\2\2\u00f7\u00f8\7@\2\2\u00f8\32\3")
        buf.write("\2\2\2\u00f9\u00fa\7>\2\2\u00fa\u00fb\7?\2\2\u00fb\34")
        buf.write("\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd\u00fe\7?\2\2\u00fe\36")
        buf.write("\3\2\2\2\u00ff\u0100\7*\2\2\u0100 \3\2\2\2\u0101\u0102")
        buf.write("\7+\2\2\u0102\"\3\2\2\2\u0103\u0104\7}\2\2\u0104$\3\2")
        buf.write("\2\2\u0105\u0106\7\177\2\2\u0106&\3\2\2\2\u0107\u0108")
        buf.write("\7]\2\2\u0108(\3\2\2\2\u0109\u010a\7_\2\2\u010a*\3\2\2")
        buf.write("\2\u010b\u010c\7<\2\2\u010c,\3\2\2\2\u010d\u010e\7=\2")
        buf.write("\2\u010e.\3\2\2\2\u010f\u0110\7.\2\2\u0110\60\3\2\2\2")
        buf.write("\u0111\u0112\7\60\2\2\u0112\u0113\7\60\2\2\u0113\62\3")
        buf.write("\2\2\2\u0114\u0116\t\3\2\2\u0115\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011a\b\32\2\2\u011a\64\3\2\2\2\u011b")
        buf.write("\u011d\t\4\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011f\66\3\2")
        buf.write("\2\2\u0120\u0122\5=\37\2\u0121\u0123\59\35\2\u0122\u0121")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0128\3\2\2\2\u0124")
        buf.write("\u0125\5? \2\u0125\u0126\59\35\2\u0126\u0128\3\2\2\2\u0127")
        buf.write("\u0120\3\2\2\2\u0127\u0124\3\2\2\2\u01288\3\2\2\2\u0129")
        buf.write("\u012b\t\5\2\2\u012a\u012c\5\r\7\2\u012b\u012a\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012e\5")
        buf.write("? \2\u012e:\3\2\2\2\u012f\u0130\7\60\2\2\u0130\u0131\5")
        buf.write("? \2\u0131<\3\2\2\2\u0132\u0133\5? \2\u0133\u0135\7\60")
        buf.write("\2\2\u0134\u0136\5? \2\u0135\u0134\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0139\5;\36\2\u0138")
        buf.write("\u0132\3\2\2\2\u0138\u0137\3\2\2\2\u0139>\3\2\2\2\u013a")
        buf.write("\u013c\t\4\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e@\3\2\2")
        buf.write("\2\u013f\u0142\5\u00a1Q\2\u0140\u0142\5\u00a3R\2\u0141")
        buf.write("\u013f\3\2\2\2\u0141\u0140\3\2\2\2\u0142B\3\2\2\2\u0143")
        buf.write("\u0144\n\6\2\2\u0144D\3\2\2\2\u0145\u0147\7^\2\2\u0146")
        buf.write("\u0148\t\7\2\2\u0147\u0146\3\2\2\2\u0148F\3\2\2\2\u0149")
        buf.write("\u014e\7$\2\2\u014a\u014d\5C\"\2\u014b\u014d\5E#\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2")
        buf.write("\u014e\u014c\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3")
        buf.write("\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\7^\2\2\u0152\u0153")
        buf.write("\n\7\2\2\u0153\u0154\b$\3\2\u0154H\3\2\2\2\u0155\u015a")
        buf.write("\7$\2\2\u0156\u0159\5C\"\2\u0157\u0159\5E#\2\u0158\u0156")
        buf.write("\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015d\u015e\7$\2\2\u015e\u015f\b")
        buf.write("%\4\2\u015fJ\3\2\2\2\u0160\u0165\7$\2\2\u0161\u0164\5")
        buf.write("C\"\2\u0162\u0164\5E#\2\u0163\u0161\3\2\2\2\u0163\u0162")
        buf.write("\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165")
        buf.write("\u0166\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0165\3\2\2\2")
        buf.write("\u0168\u0169\b&\5\2\u0169L\3\2\2\2\u016a\u016b\t\b\2\2")
        buf.write("\u016bN\3\2\2\2\u016c\u016d\t\t\2\2\u016dP\3\2\2\2\u016e")
        buf.write("\u016f\t\n\2\2\u016fR\3\2\2\2\u0170\u0171\t\13\2\2\u0171")
        buf.write("T\3\2\2\2\u0172\u0173\t\5\2\2\u0173V\3\2\2\2\u0174\u0175")
        buf.write("\t\f\2\2\u0175X\3\2\2\2\u0176\u0177\t\r\2\2\u0177Z\3\2")
        buf.write("\2\2\u0178\u0179\t\16\2\2\u0179\\\3\2\2\2\u017a\u017b")
        buf.write("\t\17\2\2\u017b^\3\2\2\2\u017c\u017d\t\20\2\2\u017d`\3")
        buf.write("\2\2\2\u017e\u017f\t\21\2\2\u017fb\3\2\2\2\u0180\u0181")
        buf.write("\t\22\2\2\u0181d\3\2\2\2\u0182\u0183\t\23\2\2\u0183f\3")
        buf.write("\2\2\2\u0184\u0185\t\24\2\2\u0185h\3\2\2\2\u0186\u0187")
        buf.write("\t\25\2\2\u0187j\3\2\2\2\u0188\u0189\t\26\2\2\u0189l\3")
        buf.write("\2\2\2\u018a\u018b\t\27\2\2\u018bn\3\2\2\2\u018c\u018d")
        buf.write("\t\30\2\2\u018dp\3\2\2\2\u018e\u018f\t\31\2\2\u018fr\3")
        buf.write("\2\2\2\u0190\u0191\t\32\2\2\u0191t\3\2\2\2\u0192\u0193")
        buf.write("\t\33\2\2\u0193v\3\2\2\2\u0194\u0195\t\34\2\2\u0195x\3")
        buf.write("\2\2\2\u0196\u0197\t\35\2\2\u0197z\3\2\2\2\u0198\u0199")
        buf.write("\t\36\2\2\u0199|\3\2\2\2\u019a\u019b\t\37\2\2\u019b~\3")
        buf.write("\2\2\2\u019c\u019d\t \2\2\u019d\u0080\3\2\2\2\u019e\u019f")
        buf.write("\5O(\2\u019f\u01a0\5o8\2\u01a0\u01a1\5U+\2\u01a1\u01a2")
        buf.write("\5M\'\2\u01a2\u01a3\5a\61\2\u01a3\u0082\3\2\2\2\u01a4")
        buf.write("\u01a5\5Q)\2\u01a5\u01a6\5i\65\2\u01a6\u01a7\5g\64\2\u01a7")
        buf.write("\u01a8\5s:\2\u01a8\u01a9\5]/\2\u01a9\u01aa\5g\64\2\u01aa")
        buf.write("\u01ab\5u;\2\u01ab\u01ac\5U+\2\u01ac\u0084\3\2\2\2\u01ad")
        buf.write("\u01ae\5W,\2\u01ae\u01af\5i\65\2\u01af\u01b0\5o8\2\u01b0")
        buf.write("\u0086\3\2\2\2\u01b1\u01b2\5s:\2\u01b2\u01b3\5i\65\2\u01b3")
        buf.write("\u0088\3\2\2\2\u01b4\u01b5\5S*\2\u01b5\u01b6\5i\65\2\u01b6")
        buf.write("\u01b7\5y=\2\u01b7\u01b8\5g\64\2\u01b8\u01b9\5s:\2\u01b9")
        buf.write("\u01ba\5i\65\2\u01ba\u008a\3\2\2\2\u01bb\u01bc\5S*\2\u01bc")
        buf.write("\u01bd\5i\65\2\u01bd\u008c\3\2\2\2\u01be\u01bf\5]/\2\u01bf")
        buf.write("\u01c0\5W,\2\u01c0\u008e\3\2\2\2\u01c1\u01c2\5s:\2\u01c2")
        buf.write("\u01c3\5[.\2\u01c3\u01c4\5U+\2\u01c4\u01c5\5g\64\2\u01c5")
        buf.write("\u0090\3\2\2\2\u01c6\u01c7\5U+\2\u01c7\u01c8\5c\62\2\u01c8")
        buf.write("\u01c9\5q9\2\u01c9\u01ca\5U+\2\u01ca\u0092\3\2\2\2\u01cb")
        buf.write("\u01cc\5o8\2\u01cc\u01cd\5U+\2\u01cd\u01ce\5s:\2\u01ce")
        buf.write("\u01cf\5u;\2\u01cf\u01d0\5o8\2\u01d0\u01d1\5g\64\2\u01d1")
        buf.write("\u0094\3\2\2\2\u01d2\u01d3\5y=\2\u01d3\u01d4\5[.\2\u01d4")
        buf.write("\u01d5\5]/\2\u01d5\u01d6\5c\62\2\u01d6\u01d7\5U+\2\u01d7")
        buf.write("\u0096\3\2\2\2\u01d8\u01d9\5O(\2\u01d9\u01da\5U+\2\u01da")
        buf.write("\u01db\5Y-\2\u01db\u01dc\5]/\2\u01dc\u01dd\5g\64\2\u01dd")
        buf.write("\u0098\3\2\2\2\u01de\u01df\5U+\2\u01df\u01e0\5g\64\2\u01e0")
        buf.write("\u01e1\5S*\2\u01e1\u009a\3\2\2\2\u01e2\u01e3\5W,\2\u01e3")
        buf.write("\u01e4\5u;\2\u01e4\u01e5\5g\64\2\u01e5\u01e6\5Q)\2\u01e6")
        buf.write("\u01e7\5s:\2\u01e7\u01e8\5]/\2\u01e8\u01e9\5i\65\2\u01e9")
        buf.write("\u01ea\5g\64\2\u01ea\u009c\3\2\2\2\u01eb\u01ec\5k\66\2")
        buf.write("\u01ec\u01ed\5o8\2\u01ed\u01ee\5i\65\2\u01ee\u01ef\5Q")
        buf.write(")\2\u01ef\u01f0\5U+\2\u01f0\u01f1\5S*\2\u01f1\u01f2\5")
        buf.write("u;\2\u01f2\u01f3\5o8\2\u01f3\u01f4\5U+\2\u01f4\u009e\3")
        buf.write("\2\2\2\u01f5\u01f6\5w<\2\u01f6\u01f7\5M\'\2\u01f7\u01f8")
        buf.write("\5o8\2\u01f8\u00a0\3\2\2\2\u01f9\u01fa\5s:\2\u01fa\u01fb")
        buf.write("\5o8\2\u01fb\u01fc\5u;\2\u01fc\u01fd\5U+\2\u01fd\u00a2")
        buf.write("\3\2\2\2\u01fe\u01ff\5W,\2\u01ff\u0200\5M\'\2\u0200\u0201")
        buf.write("\5c\62\2\u0201\u0202\5q9\2\u0202\u0203\5U+\2\u0203\u00a4")
        buf.write("\3\2\2\2\u0204\u0205\5M\'\2\u0205\u0206\5o8\2\u0206\u0207")
        buf.write("\5o8\2\u0207\u0208\5M\'\2\u0208\u0209\5}?\2\u0209\u00a6")
        buf.write("\3\2\2\2\u020a\u020b\5i\65\2\u020b\u020c\5W,\2\u020c\u00a8")
        buf.write("\3\2\2\2\u020d\u020e\5o8\2\u020e\u020f\5U+\2\u020f\u0210")
        buf.write("\5M\'\2\u0210\u0211\5c\62\2\u0211\u00aa\3\2\2\2\u0212")
        buf.write("\u0213\5O(\2\u0213\u0214\5i\65\2\u0214\u0215\5i\65\2\u0215")
        buf.write("\u0216\5c\62\2\u0216\u0217\5U+\2\u0217\u0218\5M\'\2\u0218")
        buf.write("\u0219\5g\64\2\u0219\u00ac\3\2\2\2\u021a\u021b\5]/\2\u021b")
        buf.write("\u021c\5g\64\2\u021c\u021d\5s:\2\u021d\u021e\5U+\2\u021e")
        buf.write("\u021f\5Y-\2\u021f\u0220\5U+\2\u0220\u0221\5o8\2\u0221")
        buf.write("\u00ae\3\2\2\2\u0222\u0223\5q9\2\u0223\u0224\5s:\2\u0224")
        buf.write("\u0225\5o8\2\u0225\u0226\5]/\2\u0226\u0227\5g\64\2\u0227")
        buf.write("\u0228\5Y-\2\u0228\u00b0\3\2\2\2\u0229\u022a\5g\64\2\u022a")
        buf.write("\u022b\5i\65\2\u022b\u022c\5s:\2\u022c\u00b2\3\2\2\2\u022d")
        buf.write("\u022e\5M\'\2\u022e\u022f\5g\64\2\u022f\u0230\5S*\2\u0230")
        buf.write("\u00b4\3\2\2\2\u0231\u0232\5i\65\2\u0232\u0233\5o8\2\u0233")
        buf.write("\u00b6\3\2\2\2\u0234\u0235\5S*\2\u0235\u0236\5]/\2\u0236")
        buf.write("\u0237\5w<\2\u0237\u00b8\3\2\2\2\u0238\u0239\5e\63\2\u0239")
        buf.write("\u023a\5i\65\2\u023a\u023b\5S*\2\u023b\u00ba\3\2\2\2\u023c")
        buf.write("\u023d\5y=\2\u023d\u023e\5]/\2\u023e\u023f\5s:\2\u023f")
        buf.write("\u0240\5[.\2\u0240\u00bc\3\2\2\2\u0241\u0243\t!\2\2\u0242")
        buf.write("\u0241\3\2\2\2\u0243\u0247\3\2\2\2\u0244\u0246\t\"\2\2")
        buf.write("\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3")
        buf.write("\2\2\2\u0247\u0248\3\2\2\2\u0248\u00be\3\2\2\2\u0249\u0247")
        buf.write("\3\2\2\2\u024a\u024b\13\2\2\2\u024b\u024c\b`\6\2\u024c")
        buf.write("\u00c0\3\2\2\2\31\2\u00ca\u00d6\u00e3\u0117\u011e\u0122")
        buf.write("\u0127\u012b\u0135\u0138\u013d\u0141\u0147\u014c\u014e")
        buf.write("\u0158\u015a\u0163\u0165\u0242\u0245\u0247\7\b\2\2\3$")
        buf.write("\2\3%\3\3&\4\3`\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BLOCKCOMMENT1 = 2
    BLOCKCOMMENT2 = 3
    LINECOMMENT = 4
    PLUS = 5
    MINUS = 6
    SLASH = 7
    STAR = 8
    NOTEQ = 9
    EQ = 10
    LT = 11
    GT = 12
    LE = 13
    GE = 14
    LB = 15
    RB = 16
    LCB = 17
    RCB = 18
    LSB = 19
    RSB = 20
    COLON = 21
    SEMI = 22
    COMMA = 23
    DOTDOT = 24
    WS = 25
    INTLIT = 26
    REALLIT = 27
    BOOLLIT = 28
    ILLEGAL_ESCAPE = 29
    STRINGLIT = 30
    UNCLOSE_STRING = 31
    BREAK = 32
    CONTINUE = 33
    FOR = 34
    TO = 35
    DOWNTO = 36
    DO = 37
    IF = 38
    THEN = 39
    ELSE = 40
    RETURN = 41
    WHILE = 42
    BEGIN = 43
    END = 44
    FUNCTION = 45
    PROCEDURE = 46
    VAR = 47
    TRUE = 48
    FALSE = 49
    ARRAY = 50
    OF = 51
    REAL = 52
    BOOLEAN = 53
    INTEGER = 54
    STRING = 55
    NOT = 56
    AND = 57
    OR = 58
    DIV = 59
    MOD = 60
    WITH = 61
    ID = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'/'", "'*'", "'<>'", "'='", "'<'", "'>'", 
            "'<='", "'>='", "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", 
            "';'", "','", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOMMENT1", "BLOCKCOMMENT2", "LINECOMMENT", "PLUS", "MINUS", 
            "SLASH", "STAR", "NOTEQ", "EQ", "LT", "GT", "LE", "GE", "LB", 
            "RB", "LCB", "RCB", "LSB", "RSB", "COLON", "SEMI", "COMMA", 
            "DOTDOT", "WS", "INTLIT", "REALLIT", "BOOLLIT", "ILLEGAL_ESCAPE", 
            "STRINGLIT", "UNCLOSE_STRING", "BREAK", "CONTINUE", "FOR", "TO", 
            "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", "BEGIN", 
            "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", 
            "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", 
            "OR", "DIV", "MOD", "WITH", "ID", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "BLOCKCOMMENT1", "BLOCKCOMMENT2", "LINECOMMENT", 
                  "PLUS", "MINUS", "SLASH", "STAR", "NOTEQ", "EQ", "LT", 
                  "GT", "LE", "GE", "LB", "RB", "LCB", "RCB", "LSB", "RSB", 
                  "COLON", "SEMI", "COMMA", "DOTDOT", "WS", "INTLIT", "REALLIT", 
                  "EXPONENT", "FRACTIONAL", "FLOATP", "NUMBERPART", "BOOLLIT", 
                  "CHARACTER", "LEGAL_ESCAPE", "ILLEGAL_ESCAPE", "STRINGLIT", 
                  "UNCLOSE_STRING", "A", "B", "C", "D", "E", "F", "G", "H", 
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                  "T", "U", "V", "W", "X", "Y", "Z", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "WITH", "ID", 
                  "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[34] = self.ILLEGAL_ESCAPE_action 
            actions[35] = self.STRINGLIT_action 
            actions[36] = self.UNCLOSE_STRING_action 
            actions[94] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise IllegalEscape(self.text[1:])
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


