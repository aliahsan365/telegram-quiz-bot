grammar Enquestes;
root : pregunta EOF ;
pregunta : PID PREGUNTA;


PID : 'P[0-9]+';
PREGUNTA : 'PREGUNTA';
NUM : [0-9]+ ;
WORD : '[a-zA-Z]+';
PUNTOS : ':';
WS : [ \n]+ -> skip ;
