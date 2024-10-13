def crear_tablero_vacio(filas, columnas, pregunta):
    
    while(pregunta==0):
        filas = int(input("\nIngrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        pregunta = pregunta+1
        
        if (filas*columnas) % 2 != 0: # es impar
            pregunta=0
            print("\nEl producto de filas por columnas debe ser par, ingrese nuevamente los valores")
    
        else:
            pregunta=1
            m = crear_tablero_vacio2(filas, columnas)
    return filas, columnas, m


def crear_tablero_vacio2(filas, columnas):
    matriz = []
          
    for i in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
        
    return matriz
"""
def imprimir_matriz(matriz):
    
    # Encontrar la longitud del número más grande en la matriz
    max_longitud = max(len(str(elemento)) for fila in matriz for elemento in fila)
    
    # Iterar sobre la matriz e imprimir cada elemento con el ancho adecuado
    for fila in matriz:
        for elemento in fila:
            # Ajustar el ancho del elemento y alinear a la derecha
            print("[", str(elemento).rjust(max_longitud), "]  ", end="")
        print()
        
"""