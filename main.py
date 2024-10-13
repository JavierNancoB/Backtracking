from tablero import crear_tablero_vacio
#from tablero import imprimir_matriz
from openpyxl import Workbook
from colorama import Fore, Style
import time

def guarda_la_matriz(matriz, guarda_matriz): # Guarda la matriz en la lista guarda_matriz
    guarda_matriz = matriz[:]

def guardar_matrices_en_excel(guarda_matriz, nombre_archivo): # Guarda las matrices en un archivo de Excel
    wb = Workbook()
    ws = wb.active
    current_sheet = ws  # Inicializa la hoja actual como la hoja activa

    matrices_por_pagina = 20000  # Define el número de matrices por página

    matrices_escritas = 0  # Inicializa el contador de matrices escritas en 0

    for num, matriz in enumerate(guarda_matriz, start=1):
        # Si el número actual de matrices escritas es igual al número de matrices por página,
        # cambia a la siguiente hoja y reinicia el contador de matrices escritas
        if matrices_escritas == matrices_por_pagina:
            current_sheet = wb.create_sheet()  # Crea una nueva hoja en el libro
            matrices_escritas = 0  # Reinicia el contador de matrices escritas

        current_sheet.append([f"Matriz {num}"])

        for fila in matriz:
            # Escribir cada elemento de la fila en una fila separada en la hoja de Excel
            current_sheet.append(fila)

        current_sheet.append([])

        matrices_escritas += 1  # Incrementa el contador de matrices escritas

    wb.save(nombre_archivo)

def contar():
    global cont
    cont+=1


def existen_cortes_filas(matriz, i, columnas): # Verifica si hay cortes en la matriz
    if i == 0:
        return True
    else:
        for k in range(1, columnas):
            if matriz[i][k] == matriz[i-1][k]:
                return True
    return False

def existen_cortes_columnas(matriz, j, filas): # Verifica si hay cortes en la matriz
    if j <= 0:
        return True
    else:
        for k in range(1, filas):
            if matriz[k][j] == matriz[k][j-1]:
                return True
    return False

def existen_cortes_columnas_completo(matriz, filas, columnas): # Verifica si hay por lo menos un corte en cada par de columnas en la matriz  
    cantidad_cortes = 0
    for j in range(1, columnas):
        if existen_cortes_columnas(matriz, j, filas) == True:
            cantidad_cortes += 1
    if cantidad_cortes == columnas-1:
        return True
    return False    

def existen_cortes_filas_completo(matriz, filas, columnas): # Verifica si hay por lo menos un corte en cada par de filas en la matriz
    cantidad_cortes = 0
    for i in range(1, filas):
        if existen_cortes_filas(matriz, i, columnas) == True:
            cantidad_cortes += 1
    if cantidad_cortes == filas-1:
        return True
    return False


def es_movimiento_valido_V(filas, i, j): # Que no se salga la pieza y que no se sobreponga 
    return i+1 <= filas-1 
    
def es_movimiento_valido_H(columnas, i, j): # Que no se salga la pieza y que no se sobreponga
    return 0 <= j <= columnas-1 
    
def poner_ultima_pieza(columnas, j): # Que no se salga la pieza y que no se sobreponga
    return 0 <= j <= columnas 


def comprueba_ceros(matriz, i, j, filas, columnas): # Comprueba si hay ceros en la matriz y si i j no se salen de la matriz
    if (i < filas and j < columnas):
        if matriz[i][j] == 0: 
            return True
    return False

def ultima_columna(j, columnas): # Comprueba si es la ultima columna
    if j == columnas:
        return True
    return False

def ultima_fila(i, fila): # Comprueba si es la ultima fila
    if i == fila-1:
        return True
    return False

def llenar_tablero(matriz, i, j, pieza, filas, columnas):
 
    #contar()
    #imprimir_matriz(matriz)
    if(comprueba_ceros(matriz, i, j, filas, columnas) == True and ultima_fila(i, filas) == False): # Comprueba que haya ceros en la posicion y que la fila no sea la ultima
            
        if(es_movimiento_valido_H(columnas, i, j+1)): # Si el movimiento horizontal es valido entonces inserta la pieza
            if(comprueba_ceros(matriz, i, j+1, filas, columnas) == True):
                matriz[i][j] = pieza
                matriz[i][j+1] = pieza
                result = llenar_tablero(matriz, i, j+1, pieza+1, filas, columnas)
                if result is not None:
                    return result
                # Revertir cambios antes de retornar None
                matriz[i][j] = 0
                matriz[i][j+1] = 0
        if(es_movimiento_valido_V(filas, i, j+1)): # Si el movimiento vertical es valido entonces inserta la pieza
            if(comprueba_ceros(matriz, i+1, j, filas, columnas) == True):  
                matriz[i][j] = pieza
                matriz[i+1][j] = pieza
                result = llenar_tablero(matriz, i, j+1, pieza+1, filas, columnas)
                if result is not None:
                    return result
                # Revertir cambios antes de retornar None
                matriz[i][j] = 0
                matriz[i+1][j] = 0
        return None # Si no se cumple ninguna de las condiciones anteriores retorna None

    

    
    if(comprueba_ceros(matriz, i, j, filas, columnas)==False and ultima_columna(j, columnas) == False): # Comprueba que no haya ceros en la posicion y que la columna no sea la ultima
        return llenar_tablero(matriz, i, j+1, pieza, filas, columnas) 
    
    if(comprueba_ceros(matriz, i, j, filas, columnas) == False and ultima_columna(j, columnas) == True and ultima_fila(i, filas) == False): # Comprueba que no haya ceros en la posicion y que la columna sea la ultima pero no la ultima fila
        if(existen_cortes_filas(matriz, i, columnas)): # Si hay cortes en las filas y no es la ultima fila entonces pasa a la siguiente fila
            return llenar_tablero(matriz, i+1, 0, pieza, filas, columnas) 
        if(existen_cortes_filas(matriz, i, columnas) == False): # Si no hay cortes en las filas y no es la ultima fila entonces se devuelve y sigue buscando otra solucion
            return None # Si no se cumple ninguna de las condiciones anteriores retorna None
    
    if(comprueba_ceros(matriz, i, j, filas, columnas) == True and ultima_fila(i, filas) == True and ultima_columna(j, columnas) == False): # Si hay ceros en el espacio, es la última fila y no es la última columna, entonces pasa a la siguiente columna  
        if(es_movimiento_valido_H(columnas, i, j) and comprueba_ceros(matriz, i, j+1, filas, columnas) and existen_cortes_columnas(matriz, j, filas)): # Si el movimiento es valido entonces inserta la pieza
             # Si el movimiento es valido entonces inserta la pieza
            matriz[i][j] = pieza
            matriz[i][j+1] = pieza
            result = llenar_tablero(matriz, i, j+1, pieza+1, filas, columnas)
            if result is not None:
                return result   
            # Revertir cambios antes de retornar None
            matriz[i][j] = 0
            matriz[i][j+1] = 0
        return None
    
    
    if(comprueba_ceros(matriz, i, j, filas, columnas) == False and ultima_fila(i, filas) == True and ultima_columna(j, columnas) == True):
        if(existen_cortes_columnas_completo(matriz, filas, columnas) and existen_cortes_filas_completo(matriz, filas, columnas)): 
            # Aquí guardamos una copia de la matriz actual
            guarda_matriz.append([fila[:] for fila in matriz])
            contar()
            ###imprimir_matriz(matriz)
            guarda_la_matriz(matriz, guarda_matriz)
            
        return None 
   
    
    return matriz 


filas = 0
columnas = 0
pregunta = 0

guarda_matriz = []

cont = 0

nombre_archivo = "soluciones_matrices.xlsx"

dfs = []
filas,columnas,matriz_ejemplo = crear_tablero_vacio(filas, columnas, pregunta)

inicio = time.time() # Registra el tiempo de inicio
print("\nBuscando soluciones para el tablero de", filas, "x", columnas, "......\n")
matriz_ejemplo = llenar_tablero(matriz_ejemplo, 0, 0, 1, filas, columnas)
if(cont == 0):
    fin = time.time()   
    tiempo_transcurrido = fin - inicio
    print("--Se encontraron", cont, "soluciones para el tablero de", filas, "x", columnas)
    print("\n--El Tiempo transcurrido en la busqueda de las soluciones fue de:", tiempo_transcurrido, "segundos.\n")

else:
    fin = time.time()
    tiempo_transcurrido = fin - inicio  
    print("--Se encontraron", cont, "soluciones para el tablero de", filas, "x", columnas)  
    print("\n--El Tiempo transcurrido en la busqueda de las soluciones fue de:", tiempo_transcurrido, "segundos.")
    print("\n--El codigo ha terminado de ejecutarse, estamos a la espera de la creación del excel. \n")
    guardar_matrices_en_excel(guarda_matriz, nombre_archivo)
    print("--El excel con las soluciones fue creado correctamente. \n")

    texto_importante = "¡Recuerde cerrar el excel antes de volver a ejecutar el programa!"
    print(Fore.YELLOW + Style.BRIGHT + texto_importante)
    print(Style.RESET_ALL)