# Taller de Análisis de Algoritmos - Trabajo 1

**Integrantes:**  
- Javier Nanco Becerra  
- Constanza Olivos Fernández  

**Profesor:** Luis Herrera  

**Fecha de entrega:** 28/04/2024  

## Descripción

Este trabajo tiene como objetivo resolver el Taller 1 de Análisis de Algoritmos, que consiste en crear un tablero y colocar piezas de dominó de manera que todas las filas y columnas estén interrumpidas por al menos una pieza. Cada pieza ocupa dos casillas del tablero, y el producto del número de filas y columnas debe ser un número par para que exista una solución al problema.

Para abordar este problema, se utilizó el **algoritmo de Backtracking** que explora todas las soluciones posibles de manera recursiva, descartando aquellas que no cumplen las restricciones.

## Funcionalidades del Programa

- **Ingreso del tamaño del tablero**: El usuario introduce el número de filas y columnas.
- **Verificación de restricciones**: El programa verifica que el producto de filas por columnas sea par, que las piezas no se sobrepongan ni se salgan del tablero, y que cada fila y columna tenga al menos un "corte" (interrupción por una pieza).
- **Llenado del tablero**: Utilizando Backtracking, el programa coloca las piezas en el tablero respetando las restricciones.
- **Tiempo de ejecución**: Al finalizar, se muestra el tiempo que tardó el algoritmo en encontrar la solución.
- **Exportación a Excel**: Las soluciones obtenidas se guardan en un archivo Excel para facilitar su visualización.

## Restricciones Implementadas

1. **El producto de filas por columnas debe ser par**: Verificado al iniciar el programa.
2. **Las piezas no deben sobreponerse**: Implementado con funciones que verifican si las casillas están vacías.
3. **Las piezas no deben salirse del tablero**: Controlado por funciones que validan los movimientos horizontales y verticales.
4. **Debe haber cortes en filas y columnas**: Se asegura que al menos una pieza interrumpa cada fila y columna.

## Resultados

El programa logró encontrar soluciones para matrices de distintos tamaños, aunque las matrices más pequeñas (como 4x4) no tienen solución debido a las restricciones del problema. Se demostró que Backtracking es una técnica eficaz para este tipo de problemas, aunque su eficiencia puede verse afectada por la complejidad del tablero y las restricciones impuestas.

## Conclusiones

- **Elección de Python**: Python fue elegido por su facilidad de manejo de arreglos y matrices, así como por su rendimiento en operaciones recursivas.
- **Desafíos**: Uno de los principales retos fue integrar el Backtracking y gestionar los cortes en filas y columnas.
- **Optimización**: Aunque inicialmente se intentó una técnica de fuerza bruta, finalmente se implementó Backtracking para mejorar la eficiencia del programa.
- **Visualización**: El programa exporta las soluciones a un archivo Excel, lo que facilita la verificación de los resultados.

Este proyecto demuestra un enfoque riguroso para resolver problemas algorítmicos utilizando Backtracking, con una implementación detallada y resultados verificables.
