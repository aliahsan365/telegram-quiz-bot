# Bot de Telegram para hacer encuestas

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
python test.py publicinput.txt

```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

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
como minimo una vez.
* Mi lenguaje no contempla la opcion para tildes
* Depende del sistema operativo la entrada la coje de una sola linea o reconoce bien los EOF por ese motivo he
dejado dos entrada publicas uno que es input (la publica sin acentos) y inputoneline(publica sin acentos y en una sola
linea todo)
* La practica esta pensada para que en un mismo grafo haya mas de una encuesta y que hay mas de una alternativa que te
lleve a otra alternativa si contestas una cierta opcion, es decir, la practica es multiencuesta y multilaternativas.
Para ver esto tenemos la oneline3e y oneline2a.
