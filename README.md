# Bot de Telegram para hacer encuestas

## Getting Started

Para la parte de compiladores, es decir, compilar los inputs
y ver el renderizado del grafo resultante hay que estar en la carpeta "cl"
Todo los comandos para esto se hacen estando en la carta de "cl"

Todo lo que tenga ver con el bot, su ejecucion y la intereacion hay estar en la carpeta bot y ejecutarlo en la misma carpeta.

Los pickles se generan cada uno en su carpeta , graph.pickle en carpeta cl
stats.pickle en la carpeta bot (estadisticas de todos los usuarios)


### Prerequisites

Tener el entrno configutado siguiendo la guía de LP

```
https://gebakx.github.io/Python3/compiladors.html#2
```




el algoritmo acaba no funcionado por telegram , y si por consola.


## Running the tests

Todo hay que ejecutarlo en la carpeta test



###Ejemplo de reporte, se imprimen tambien las opciones que no han sido contestadas


![Alt text](./images/report.png?raw=true "report")
![Alt text](./images/bar.png?raw=true "bar")
![Alt text](./images/pie.png?raw=true "pie")
### Ejemplo de test mas de una encuesta en el mismo fichero (multiencuestas)

En el caso de juegos publicos tenemos que ejecutando esto

```
python test.py inputmultiencuestas.txt

```
obtenemos esto : 
![Alt text](./images/inputmultiencuestas.png?raw=true "inputmultiencuestas")

En el caso de juegos publicos tenemos que ejecutando esto

```
python test.py inputmultiencuestas.txt

```
obtenemos esto : 
![Alt text](./images/inputmultiencuestas.png?raw=true "inputmultiencuestas")

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

```
Give an example
```

## Built With

* [antlr4](https://www.antlr.org/) - antlr4 python


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

Git

## Authors

* **Ali Muhammad Shiekh** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Suposiciones y aclaraciones
* Todas las encuestas van al nodo END.
* Encuesta puede tener como ID : E, E0, E1...En general, E[0-9]*
* Pregunta, Respuesta, Item y Alternativa tienen P1,R1,I1,A1...En general, LETRAINICIAL[0-9]+
* Las opciones de alternativa pueden tener los pares (numero,item), sin coma o con coma.
* Dos o mas preguntas pueden tener la misma respuesta.
* Una pregunta tiene exactamente una respuesta.
* Se imprimien en el reporte todas las preguntas con sus opciones, es decir, no depende que hayan sido selecionadas como
 minimo una vez.
* Mi lenguaje NO contempla la opcion para tildes
* Depende del sistema operativo la entrada la coje de una sola linea o reconoce bien los EOF por ese motivo he
dejado dos entrada publicas uno que es input (la publica sin acentos) y inputoneline(publica sin acentos y en una sola
linea todo)
* La practica esta pensada para que en un mismo grafo haya mas de una encuesta y que hay mas de una alternativa que te
lleve a otra alternativa si contestas una cierta opcion, es decir, la practica es multiencuesta y multilaternativas.
Para ver esto tenemos la oneline3e y oneline2a.
# Problematica con el algoritmo de recorrido del bot
En el archivo ./bot/algoritmo.py, que podemos ejecutar usando [exec] , podemos ver que si le pasamos un grafo , podemos obtener 
las preguntas de las encuestas, y en funcion de lo que hayamos metido como entrada
por la entrada standar (consola), es capaz de ir dandonos las preguntas correctamente. El promblema es esencialmente
la intereacion con el bot , es decir, el modelo que se nos da para hacer bots en LP de ejemplo, no permite guardar estado automaticamente,
el algoritmo acaba NO funcionado por telegram , y si por consola , incluyendo multialternativas en las encuetas , y tambien teniendo más de una encuesta en el grafo.
