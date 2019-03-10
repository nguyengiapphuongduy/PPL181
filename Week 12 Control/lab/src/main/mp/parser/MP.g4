// id = 1610473

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}




program: decl+ EOF;
decl: varDeclare | funcDeclare | procDeclare;

varDeclare: VAR (varDeclareOne SEMI)+;

varDeclareOne: idlist COLON mptype;

idlist: ID (COMMA ID)*;

funcDeclare: FUNCTION ID LB (varDeclareOne (SEMI varDeclareOne)*)? RB COLON mptype SEMI varDeclare* compStmt;

procDeclare: PROCEDURE ID LB (varDeclareOne (SEMI varDeclareOne)*)? RB SEMI varDeclare* compStmt;


//expression
expr: expr (AND THEN | OR ELSE) exp1 | exp1;
exp1: exp2 (EQ | NOTEQ | LT | LE | GT | GE) exp2 | exp2;
exp2: exp2 (PLUS | MINUS | OR) exp3 | exp3;
exp3: exp3 (STAR | SLASH | DIV | MOD | AND) exp4 | exp4;
exp4: (MINUS | NOT) exp4 | exp5;
exp5: LB expr RB | ID | invoke | indexExpr | INTLIT | REALLIT | BOOLLIT | STRINGLIT;

indexExpr: indexExpr LSB expr RSB
		| LB expr RB LSB expr RSB
		| invoke LSB expr RSB
		| ID LSB expr RSB
		| INTLIT LSB expr RSB
		| REALLIT LSB expr RSB
		| BOOLLIT LSB expr RSB
		| STRINGLIT LSB expr RSB;
invoke: ID LB expList RB;
expList: expr (COMMA expr)* |;


//statements
compStmt: BEGIN listOfStmt END;

listOfStmt: (statement)*;

statement: compStmt | assignment | ifStmt | forStmt | whileStmt | breakStmt | contStmt | retStmt | withStmt | callStmt;

assignment: (lhs ':=')+ expr SEMI;
lhs: ID | indexExpr;
ifStmt: IF expr THEN statement (ELSE statement)?;
whileStmt: WHILE expr DO statement;
forStmt: FOR ID ':=' expr (TO | DOWNTO) expr DO statement;
breakStmt: BREAK SEMI;
contStmt: CONTINUE SEMI;
retStmt: RETURN (expr)? SEMI;
withStmt: WITH (varDeclareOne SEMI)+ DO statement;
callStmt: ID LB expList RB SEMI;


//types
mptype: primtype | arraytype;

primtype: INTEGER | REAL | BOOLEAN | STRING;

arraytype: ARRAY LSB MINUS? INTLIT DOTDOT MINUS? INTLIT RSB OF primtype;


//comments
BLOCKCOMMENT1: '(*' .*? '*)' -> skip;
BLOCKCOMMENT2: LCB .*? RCB -> skip;
LINECOMMENT: '//' ~('\r' | '\n')* -> skip;


//10 operators, AND OR DIV MOD NOT already defined as keyword
PLUS: '+';
MINUS: '-';
SLASH: '/';
STAR: '*';
NOTEQ: '<>';
EQ: '=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';


//normal, curly, square brackets
LB: '(';
RB: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';

COLON: ':';
SEMI: ';';
COMMA: ',';
DOTDOT: '..';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines


//literals
INTLIT: [0-9]+;

REALLIT: FLOATP EXPONENT? | NUMBERPART EXPONENT;
fragment EXPONENT: [eE]MINUS?NUMBERPART;
fragment FRACTIONAL: '.' NUMBERPART;
fragment FLOATP: (NUMBERPART '.' NUMBERPART?) | FRACTIONAL;
fragment NUMBERPART: [0-9]+;

BOOLLIT: TRUE|FALSE;


//string literal and its error
fragment CHARACTER: ~('\b' | '\f' | '\r' | '\n' | '\t' | '\'' | '"' | '\\');
fragment LEGAL_ESCAPE: '\\' ([bBfFrRnNtT"] | '\'' | '\\');

ILLEGAL_ESCAPE:
'"' (CHARACTER | LEGAL_ESCAPE)* '\\' ~([bBfFrRnNtT"] | '\'' | '\\')
{raise IllegalEscape(self.text[1:])};

STRINGLIT:
'"' (CHARACTER | LEGAL_ESCAPE)* '"'
{self.text = self.text[1:-1]};

UNCLOSE_STRING:
'"' (CHARACTER | LEGAL_ESCAPE)*
{raise UncloseString(self.text[1:])};


//capture keyword as case-insensitive
fragment A: ('a' | 'A');
fragment B: ('b' | 'B');
fragment C: ('c' | 'C');
fragment D: ('d' | 'D');
fragment E: ('e' | 'E');
fragment F: ('f' | 'F');
fragment G: ('g' | 'G');
fragment H: ('h' | 'H');
fragment I: ('i' | 'I');
fragment J: ('j' | 'J');
fragment K: ('k' | 'K');
fragment L: ('l' | 'L');
fragment M: ('m' | 'M');
fragment N: ('n' | 'N');
fragment O: ('o' | 'O');
fragment P: ('p' | 'P');
fragment Q: ('q' | 'Q');
fragment R: ('r' | 'R');
fragment S: ('s' | 'S');
fragment T: ('t' | 'T');
fragment U: ('u' | 'U');
fragment V: ('v' | 'V');
fragment W: ('w' | 'W');
fragment X: ('x' | 'X');
fragment Y: ('y' | 'Y');
fragment Z: ('z' | 'Z');
//keywords
BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
TO: T O;
DOWNTO: D O W N T O;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
RETURN: R E T U R N;
WHILE: W H I L E;
BEGIN: B E G I N;
END: E N D;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
VAR: V A R;
TRUE: T R U E;
FALSE: F A L S E;
ARRAY: A R R A Y;
OF: O F;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;
WITH: W I T H;

ID: ([a-zA-Z] | '_') ([a-zA-Z0-9] | '_')*;

ERROR_CHAR:
.
{raise ErrorToken(self.text)};
