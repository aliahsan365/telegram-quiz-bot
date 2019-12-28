grammar Enquestes;
root : expr EOF ;

expr : expr MES term | expr MENYS term | term;
term : term MUL atom | term DIV atom | atom;
atom : NUM;

NUM : [0-9]+ ;
ID :  [a-z]+;
MES : '+' ;
MENYS : '-';
MUL : '*';
DIV : '/';
WS : [ \n]+ -> skip ;
