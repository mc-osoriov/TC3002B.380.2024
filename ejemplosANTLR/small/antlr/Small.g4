grammar Small;

program
    :   (decl|function_decl|statement)*
    ;

decl
    :   type ident_list ';'      #varDecl
    ;

type
    :   'int'
    |   'float'
    |   'string'
    |   'bool'
    ;

function_decl
    :   type ID '(' params? ')' '{' statement* '}'
    ;

params
    :   param (',' param)*
    ;

param
    :   type ID
    ;

ident_list
    :   ident (',' ident)*
    ;

ident
    : ID ( '=' expr )?
    ;

statement
    :  type ident_list ';'                #varDeclStmt
    |  expr '=' expr ';'                  #assign
    |  type ID '=' expr ';'               #varInitStmt
    |  'print' '(' expr ')' ';'           #print
    |  'if' '(' expr ')' '{' statement* '}' ('else' '{' statement* '}')? #if
    |  'while' '(' expr ')' '{' statement* '}' #while
    |  'return' expr ';'                  #return
    ;

expr
    :   '!' expr        #not
    |   expr '==' expr  #equal
    |   expr '!=' expr  #notEqual
    |   expr '>' expr   #greater
    |   expr '<' expr   #less
    |   expr '>=' expr  #greaterEqual
    |   expr '<=' expr  #lessEqual
    |   expr '&&' expr  #and
    |   expr '||' expr  #or
    |   expr '*' expr   #mult
    |   expr '/' expr   #div
    |   expr '+' expr   #add
    |   expr '-' expr   #sub
    |   expr '^' expr   #pow
    |   'sqrt' '(' expr ')'  #sqrt
    |   INT             #int
    |   STRING          #string
    |   FLOAT           #float
    |   'true'          #true
    |   'false'         #false
    |   ID              #id
    |   ID '(' (expr (',' expr)*)? ')'  #functionCall
    |   '(' expr ')'    #parens
    ;


INT     : [0-9]+ ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
STRING  : '"' .*? '"' ;
ID      : [a-zA-Z_][a-zA-Z0-9_]* ;

WS : [ \t\n\r]+ -> skip ;
