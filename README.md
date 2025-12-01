# Viajes Metro Caracas  CLI
Programa para calcular costo de viajes de metro y estaciones recorridas con Python

- **Desafío de resolución de problemas y lógica - Nexureon**
- **Autor:** Diego Hernández
- **Lenguaje:** Python 3.10+

## Descripción del proyecto

Este programa de linea de comandos (CLI) calcula y determina el costo y trayecto a recorrer según las indicaciones que se pide al usuario; el programa preguntara al usuario las estaciones de inicio y destino, tras ello el programa calculara las estaciones y líneas recorridas y el costo del viaje.

## Guía de Instalación y Ejecución

Siga los siguientes pasos para ejecutar el programa

### 1- Pre-requisitos
- Tener instalado Python 3.

### 2- Preparación

Asegúrese de tener el archivo `main.py` en su dispositivo, de preferencia guardado en una carpeta con un nombre designado y claro de lo que realiza el programa

### 3- Ejecución

El programa se ejecuta directamente en el `archivo main.py`. Abra un terminal en la carpeta o ruta en el que guardo el proyecto, para ello deberá utilizar cd (ruta). Ejemplo: `cd destkop/programa_metro`

Posteriormente deberá de utilizar el siguiente comando:
`Python main.py`

Y estará ejecutado.

### Guía de funcionamiento:

Tras ejecutar el programa como se indica previamente el programa hará 2 preguntas al usuario:

- ¿Cuál es su estación de inicio? (En el cual deberá indicar en cual estación inicia el viaje)

- ¿Cuál es su estación de destino? (Cual es la estación en la terminara su viaje)

Posteriormente a estas preguntas el programa comparara las respuestas del usuario con las listas de las estaciones disponibles en las respectivas líneas del metro, dependiendo de lo que se haya indicado pueden pasar dos situaciones en ambas preguntas, una es que el usuario introdujo de forma incorrecta la estación y el programa preguntara de nuevo al usuario la estación, y la segunda donde el usuario introdujo correctamente la estación y el programa calculara el costo del viaje y las estaciones a recorrer en el trayecto.

## Ejemplo de ejecución:

Situación: El usuario desea viajar desde Altamira a Plaza Venezuela, desconoce el costo y que ruta deberá de tomar.

*Se ejecuta el programa*

- ¿Cuál es su estación de inicio? Altamira
- Se inicia en Altamira (Línea 1).
- ¿Cuál es su estación de destino? Plaza Venezuela
- El destino es Plaza Venezuela (Línea 1).
Calculando Costo y Ruta
Viaje directo en la Línea 1.
El costo total del viaje es: 4 unidades.
La ruta detallada a recorrer es:
INICIO: Altamira (Línea 1)
...
DESTINO: Plaza Venezuela (Línea 1)

Resultado: El programa ha calculado el costo de unidades y el trayecto y el usuario puede saber con certeza el viaje que debe de realizar y su costo.
