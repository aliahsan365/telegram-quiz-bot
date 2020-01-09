# Bot de Telegram para hacer encuestas

## Autor
* **Ali Muhammad Shiekh** 
## Empezando
Para la parte de compiladores, es decir, compilar los inputs
y ver el renderizado del grafo resultante:

1 : Hay que estar en la carpeta cl. 

Todo los comandos para esto se hacen estando en la carpeta de cl

Todo lo que tenga ver con el bot, su ejecucion y la interacion hay estar en la carpeta bot, y 
ejecutarlo en la misma carpeta bot.

Los pickles se generan cada uno en su carpeta, graph.pickle en carpeta /cl.
stats.pickle en la carpeta /bot. (estadisticas de todos los usuarios de todas las preguntas)
### Prerequisites
Tener el entorno configutado siguiendo la guía de LP

```
https://gebakx.github.io/Python3/compiladors.html#2
```
###### RESUMEN PARA EJECUTAR TODO CON LA FINALIDAD DE PROBARLO.

```
https://gebakx.github.io/Python3/compiladors.html#2
```
## Tests

#### Compilado y renderizado de grafo:
##### Ejemplo 1:
En la carpeta cl ejecutar

```
python test.py publicinput.txt
```
obtenemos como resultado : 

![Alt text](./images/publicinput.png?raw=true "publicinput")

##### Ejemplo 2:
En la carpeta cl ejecutar

```
python test.py inputmultialternativas.txt
```
obtenemos como resultado : 

![Alt text](./images/inputmultialternativas.png?raw=true "inputmultialternativas")

##### Ejemplo 3:
En la carpeta cl ejecutar

```
python test.py inputmultiencuestas.txt
```
obtenemos como resultado : con E1,E2,E3 , tres nodos encuesta

![Alt text](./images/inputmultiencuestas.png?raw=true "inputmultiencuestas")

#### Ejecucion del bot y reporte


##### Ejemplo encuesta:

Encuesta con multiencuesta empezando des del nodo E3 del grafo del ejemplo 3.
![Alt text](./images/multiencuestas.png?raw=true "multiencuestas")


##### Ejemplo reportes:
He pintado tambien los que son 0 de la misma pregunta.
El explode  no se ha usado finalmente.

![Alt text](./images/report.png?raw=true "report")
![Alt text](./images/bar.png?raw=true "bar")
![Alt text](./images/pie.png?raw=true "pie")


## Suposiciones y aclaraciones
* Todas las encuestas van al nodo END.
* Siempre hay nodo END.
* Encuesta puede tener como ID : E, E0, E1...En general, E[0-9]*
* Pregunta, Respuesta, Item y Alternativa tienen P1,R1,I1,A1...En general, LETRAINICIAL[0-9]+
* Las opciones de alternativa pueden tener los pares (numero,item), sin coma o con coma.
* Dos o mas preguntas pueden tener la misma respuesta.
* Una pregunta tiene exactamente una respuesta.
* Se imprimien en el reporte todas las preguntas con sus opciones, es decir, no depende que hayan sido selecionadas como
 minimo una vez.
* Mi lenguaje NO contempla la opcion para tildes
* Depende del sistema operativo la entrada la coje de una sola linea o reconoce bien los EOF. Por ese motivo he
dejado dos entradas publicas, una que es publicinput.txt (la publica sin acentos), y otra  publicinputoneline.txt (publica sin acentos y en una sola
linea todo)
* La practica esta pensada para que en un mismo grafo haya mas de una encuesta y que haya mas de una alternativa que te
lleve a otra alternativa, si contestas una cierta opcion, es decir, la practica es multiencuesta y multilaternativas.
Para ver esto tenemos la inputmultiencuestas.txt y inputmultialternativas.txt, respectivamente. 

# El algoritmo de recorrido del bot

El algoritmo es un doble DFS por el grafo en cuestion. Es decir, es un DFS anidado. El primero , mas exterior, es para
las preguntas de la encuesta en si. El siguiente DFS es para las alternativas. Se acaba volviendo al mismo nodo despues de
visitar las alternativas. El algoritmo se puede ejecutar usando: 

```
python algoritmo.py
```
(NOTA: se debe estar en la carpeta bot para ejecuarlo y el pickle del grafo ha de estar generado en
la carpeta cl)

# Problematica con el algoritmo de recorrido del bot
En el archivo algoritmo.py de la carpeta bot podemos ver que si le pasamos un grafo , podemos obtener 
las preguntas de las encuestas, y en funcion de lo que hayamos metido como entrada
por la entrada standar (consola) como respuestas a la pregunta, es capaz de ir dandonos las preguntas correctamente. El promblema es esencialmente
la intereacion con el bot, es decir, el modelo que se nos da para hacer bots en LP de ejemplo, no permite guardar estado automaticamente.
Es decir, si lo printamos por telegram , acaba dando todas las pregutas por que hace el recorrido sin parar, a menos que lo hagamos por consola (entrada standard)

RESUMEN : El algoritmo acaba NO funcionado por telegram, y si por consola , incluyendo multialternativas en las encuetas , y tambien teniendo más de una encuesta en el grafo.

## Versioning
Se ha usado Git.
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
## Built With
* [antlr4](https://www.antlr.org/) - antlr4 python
* Tambien se debe usar el fichero requirements.txt para instalar las librerias.
