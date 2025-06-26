# Sistema de Cálculo de Salarios para Traductores - Ivan Sanchez

Este proyecto implementa un sistema de cálculo salarial para traductores aplicando múltiples paradigmas de programación: orientación a objetos, lógica, funcional y eventos con interfaz gráfica.

## 📌 Funcionalidades

- Cálculo del salario mensual por cantidad de palabras o por tiempo trabajado.
- Interfaz gráfica desarrollada con Tkinter (GUI - programación orientada a eventos).
- Evaluación de bonificación si el salario supera los 4 millones de guaraníes, usando pyDatalog (programación lógica).
- Uso de funciones funcionales (`map`, `lambda`, `filter`) para procesamientos puntuales.
- Persistencia de salarios calculados con `pickle`, permitiendo:
  - Guardar automáticamente resultados en archivos `.pkl`
  - Listar los salarios guardados desde la interfaz
  - Limpiar todos los archivos guardados

## 🧱 Estructura del Proyecto

- `main.py`: Punto de entrada principal, lanza la GUI.
- `interfaz_gui.py`: Interfaz de usuario con botones para calcular, listar y limpiar salarios.
- `interfaz_console.py`: Versión alternativa por consola.
- `controlador.py`: Orquesta las operaciones entre la interfaz y la lógica de negocio.
- `estrategias.py`: Contiene las clases `CalculoPorPalabra` y `CalculoPorHora` con polimorfismo.
- `modelos.py`: Modelos base como `Trabajador` y `Productividad`.
- `datos.py`: Carga de datos desde archivo Excel y filtrado por mes.
- `logica.py`: Contiene la lógica de bonificación implementada en `pyDatalog`.
- `persistencia.py`: Módulo de guardado, carga, listado y limpieza de salarios calculados (`pickle`).
- `PlanillaCalculo.xlsx`: Archivo fuente con registros de productividad.

## 🧪 Requisitos de Ejecución

- Python 3.10 o superior
- Paquetes requeridos:
  - `pandas`
  - `openpyxl`
  - `pyDatalog`
  - `tkinter`

## ▶️ Ejecución
OBS : Contar con el archivo PlanillaCalculo.xlsx en la carpeta raiz.
Desde la terminal:
- python main.py
- Realizar la carga en numeros ej: ["04"] y el nombre del Traductor ["Ivan Sanchez"] y calcular.
- Si se desea listar, presionar el boton y si se desea eliminar los listados esta el segundo boton.
