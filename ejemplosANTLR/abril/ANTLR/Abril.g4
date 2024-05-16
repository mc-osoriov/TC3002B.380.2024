grammar Abril;

prog: decl+;

decl:
    'int' ID ';'
    | 'float' ID ';'
    | 'string' ID ';'
    ;

klass: 'estroct' ID '%' (peculiaridad | tecnica)+ '%';

peculiaridad: tipo ID
    ;

tecnica: ID '(' params* ')' '%' sentencia+'%'
    ;

params: tipo ID (',' tipo ID)*;

sentencia:
    ID
    ;

tipo: INT;

INT: 'int';
BLANKS: [ \n]* -> skip;
ID: [a-zA-Z]+;
NUMERO: [0-9]+;



