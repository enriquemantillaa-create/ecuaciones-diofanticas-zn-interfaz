# Interfaz Gráfica para la Resolución de Ecuaciones Diofánticas en $\mathbb{Z}_n$

Este repositorio contiene el componente computacional desarrollado como parte de un trabajo de grado en matemáticas enfocado en la aritmética modular. La aplicación implementa una interfaz gráfica interactiva **desarrollada en el lenguaje de programación Python** que automatiza y permite visualizar la transposición de los métodos de resolución de ecuaciones diofánticas desde el conjunto de los enteros ($\mathbb{Z}$) hacia el anillo de los enteros módulo $n$ ($\mathbb{Z}_n$).

## Características del Sistema

1. **Entorno Visual (`src/interfaz.py`):** Arquitectura gráfica interactiva construida en **Python** utilizando la librería `CustomTkinter` para ofrecer una experiencia de usuario limpia, intuitiva y dinámica.
2. **Modelado Matemático (`src/MSED.py`):** Módulo de **Python** encargado de la computación algebraica que ejecuta las siguientes propiedades y métodos adaptados al anillo $\mathbb{Z}_n$:
   * **Propiedades de Divisibilidad en $\mathbb{Z}$ y $\mathbb{Z}_n$:** Implementación computacional de los pilares aritméticos base. Estos algoritmos se programaron inicialmente en $\mathbb{Z}$ y posteriormente se adaptaron y restringieron para operar bajo las estructuras modulares de $\mathbb{Z}_n$:
     * Algoritmo de la División.
     * Algoritmo de Euclides.
     * Máximo Común Divisor (mcd).
     * Lema de Bézout.
   * **Solucionador de Ecuaciones Lineales Diofánticas ($\overline{a}\cdot \overline{x} + \overline{b}\cdot \overline{y} = \overline{c}$):** Permite la resolución y visualización interactiva mediante los siguientes enfoques algebraicos:
     * **Método de la Falsa Posición**.
     * **Método del Algoritmo de Euclides y Lema de Bézout**.
     * **Método de Diofanto**.
   * **Solucionador de Ternas Pitagóricas y Ecuaciones Cuadráticas ($\overline{x}^2 + \overline{y}^2 = \overline{z}^2$):** Adaptación de los métodos de generación clásicos a las propiedades de los sistemas numéricos finitos a través de:
     * **Método de Diofanto**.
     * **Método de Fibonacci**.

---

## Soporte Teórico y Algorítmico (Jupyter Notebooks)

Para complementar la aplicación y ofrecer un trasfondo académico riguroso, este proyecto incluye cuadernos de **Jupyter Notebook** (ubicados en la carpeta `teoria/`) donde se desarrolla en formato ejecutable:
1. El desarrollo analítico de las propiedades de la divisibilidad en $\mathbb{Z}$ y $\mathbb{Z}_n$.
2. La fundamentación teórica y demostraciones estructurales de cada método de transposición en $\mathbb{Z}_n$.
3. La construcción, verificación y corrida en frío paso a paso de los algoritmos antes de ser implementados formalmente en la interfaz gráfica.

---

## Requisitos e Instalación

Para ejecutar este software de forma local, asegúrese de contar con **Python 3.8 o superior** instalado en su sistema.

1. Clone este repositorio en su máquina local o descargue el archivo comprimido:
   ```bash
   git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
   cd Interfaz