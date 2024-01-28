grammar gramatyka;

// Following grammar reflects in some way Golang programming language. Reflected Golang features is
// for example 'for' loop.
main: (statement | NL*) (NL* statement)* NL*;
statement:
	printStatement ';'
	| inputStatement ';'
	| conditionalStatement
	| loopStatement
	| variableAssignmentStatement ';';
name: STRING;
printStatement: 'print ' (expression);
inputStatement: 'read';
conditionalStatement:
	'if ' comparison codeBlock (' else ' codeBlock)?;
loopStatement: 'for ' comparison codeBlock;
variableAssignmentStatement:
	name '=' (expression | inputStatement);
comparison:
	expression ('==' | '!=' | '<' | '>' | '<=' | '>=') expression
	| notComparison
	| comparison (' and ' | ' or ') comparison;

notComparison: 'not' comparison;

expression:
	term
	| expression ('+' | '-') expression
	| inputStatement;

term:
	INTEGER
	| name
	| inputStatement
	| '(' expression ')'
	| term ('*' | '/') term;

codeBlock: '{' NL* main NL* '}';

INTEGER: '-'? [0-9]* '.'? [0-9]*;
STRING: [a-zA-Z][a-zA-Z0-9_]*;
NL: [\r\n]*;
WS: [ \t]+ -> skip;