grammar Expr;		

// Parser
lenguaje: operacion+;

operacion:
    numero #num
    | operacion '*' operacion #mul
    | operacion '/' operacion #div
    | operacion '+' operacion #add
    | operacion '-' operacion #sub
    | '(' operacion ')' #paren
    ;

numero: ENTERO | FLOTANTE;

// Léxico
ENTERO: INT ;
FLOTANTE: INT '.' INT;
BLANK: [ \n]+ -> skip;
MAS: '+';
POR: '*';

fragment INT:[0-9]+;










//prog:	(expr)* ;

//expr:	expr ('*'|'/') expr
//    |	expr ('+'|'-') expr
//    |	INT
//    |	'(' expr ')'
//    ;




//NEWLINE : [\r\n]+ -> skip;
//BLANK   : [ ]+ -> skip;
