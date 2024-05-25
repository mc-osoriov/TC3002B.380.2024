grammar calc;

operacion : exp+;

exp :
    exp '*' exp     #mult
    | exp '+' exp   #suma
    | NUMERO        #num
    | VARIABLE      #var
    | '(' exp ')'   #parens
    ;

NUMERO : [0-9]+;
VARIABLE : [a-zA-Z]+;
WS : [ \n]+ -> skip;