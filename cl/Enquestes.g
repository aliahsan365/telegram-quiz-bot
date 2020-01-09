grammar Enquestes;
root : blocs FINAL EOF ;
blocs: (pregunta|resposta|element|alternativa|enquesta)*;

pregunta : PID PUNTS PREGUNTA PARAULES* SIGNEPREGUNTA;

resposta : RID PUNTS RESPOSTA opcio*;
opcio : NUMERO PUNTS PARAULES* PUNTCOMA;

element: IID PUNTS ELEMENT relacio*;
relacio: PID FLETXA RID ;


alternativa: AID PUNTS ALTERNATIVA implications;
implications: IID CE blocrespostaelement CD;
blocrespostaelement: (respostaelement COMA|respostaelement)*;
respostaelement: PE NUMERO COMA IID PR;

enquesta : EID PUNTS ENQUESTA IID*;

AID : 'A'[0-9]+;
EID : 'E'[0-9]*;
IID : 'I'[0-9]+;
RID : 'R'[0-9]+;
PID : 'P'[0-9]+;
COMA : ',';
CE : '[';
CD : ']';
PE : '(';
PR : ')';
ENQUESTA  : 'ENQUESTA';
ELEMENT : 'ITEM';
PREGUNTA : 'PREGUNTA';
RESPOSTA : 'RESPOSTA';
ALTERNATIVA : 'ALTERNATIVA';
PUNTCOMA : ';';
FLETXA : '->';
NUMERO : [0-9]+ ;
FINAL : 'END';
PARAULES : [a-zA-Z]+;
PUNTS : ':';
SIGNEPREGUNTA : '?';
WS : [ \n]+ -> skip ;
