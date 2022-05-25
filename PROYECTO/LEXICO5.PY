#!/usr/bin/env python
# encoding: utf-8
from CONST import MATRIZ_ESTADO, COLUMNAS_MATRIZ, PALABRAS_RESERVADAS, ESTADOS_FINALES, ESTADOS_ERROR
from tabulate import tabulate
from SINTACTICO import ANALIZADOR_SINTACTICO

# Tablas para cada tipo de estados
PALABRAS_RESERVADAS_RECONOCIDAS=[]
IDENTIFICADORES=[]
SIMBOLOS=[]
ERRORES=[]
# Tabla general (lo que detecta el lexico)
ITERADOR=[]

def ANALIZADOR_LEXICO():

    #ARCHIVO_DE_ENTRADA = sys.argv[l]
    with open(TEXTO) as k:
        ENTRADA = k.readlines()

    #INDICA EL ESTADO ACTUAL EN EL QUE SE ENCUENTRA EL AUTOMATA
    ESTADO=0
    # CONTADOR DE IDENTIFICADORES
    NUM_IDENTIFICADORES = 0
    #Numero de filas de la tabla general
    NUM_FILAS = 0
    #CADENA QUE EVALUA EL ANALIZADOR
    CADENA_ACTUAL=""

    for i in range(len(ENTRADA)):
        LINE = ENTRADA[i]
        # if(ENTRADA!=""):
        for j in range(len(LINE)):
            CAR = LINE[j]

            CADENA_ACTUAL += CAR
            # EN LA VARIABLE COLUMNA SE UBICA EL TIPO DE CARACTER EN CURSO
            #print(CAR)
            COLUMNA=COLUMNAS_MATRIZ[CAR]
            #print(ESTADO, COLUMNA)
            ESTADO=MATRIZ_ESTADO[ESTADO][COLUMNA]

            if ESTADO in ESTADOS_FINALES:
                if ESTADO == 125:
                    # Asignar el token a partir de 127 (Porque el ultimo estado final tiene codigo 131)
                    TOKEN = PALABRAS_RESERVADAS.index(CADENA_ACTUAL.strip()) + 131
                    # Agregar la palabra a a lista de reconocidas
                    PALABRAS_RESERVADAS_RECONOCIDAS.append([CADENA_ACTUAL, TOKEN])
                    ITERADOR.append([NUM_FILAS, "Reservada", CADENA_ACTUAL.strip(), ESTADO])
                elif ESTADO == 101:
                    # Se almacena el identificador junto con la posición que ocupa (# de identificadores)
                    IDENTIFICADORES.append([CADENA_ACTUAL, NUM_IDENTIFICADORES])
                    NUM_IDENTIFICADORES += 1
                    ITERADOR.append([NUM_FILAS, "Identificador", CADENA_ACTUAL.strip(), ESTADO])
                elif ESTADO == 100:
                    #Logica para numeros
                    ITERADOR.append([NUM_FILAS, "Numero", CADENA_ACTUAL.strip(), ESTADO])
                else:
                    SIMBOLOS.append([CADENA_ACTUAL, ESTADO])
                    ITERADOR.append([NUM_FILAS, "Simbolo", CADENA_ACTUAL.strip(), ESTADO])

                CADENA_ACTUAL=""
                ESTADO=0
                NUM_FILAS += 1
            #CUALQUIER NUMERO POR ARRIBA DE 200 SERÁ MARCADO COMO ERROR
            elif ESTADO >= 200:
                ERRORES.append(CADENA_ACTUAL+" "+ESTADOS_ERROR[ESTADO])
                # print(CADENA_ACTUAL+" "+ESTADOS_ERROR[ESTADO])
                CADENA_ACTUAL=""
                ESTADO=0

if __name__ == '__main__':
    TEXTO ="prueba2.txt"
    # print(ANALIZADOR_LEXICO())
    ANALIZADOR_LEXICO()
    print("TABLA DE TOKENS")
    print(tabulate(ITERADOR, headers=["id", "Tipo Token", "Token", "Token numerico"], tablefmt='fancy_grid'))
    print("TABLA PARA PALABRAS RESERVADAS")
    print(tabulate(PALABRAS_RESERVADAS_RECONOCIDAS, headers=["Palabra Reservada", "Token"], tablefmt='fancy_grid'))
    print("TABLA PARA IDENTIFICADORES")
    print(tabulate(IDENTIFICADORES, headers=["Identificador", "Id"], tablefmt='fancy_grid'))
    print("TABLA PARA SIMBOLOS")
    print(tabulate(SIMBOLOS, headers=["Simbolo", "Token"], tablefmt='fancy_grid'))
    print("TABLA DE ERRORES")
    print(*ERRORES, sep='\n')

    STACK_LEXICO = list(map(lambda x: x[2], ITERADOR))
    ANALIZADOR_SINTACTICO(STACK_LEXICO[::-1])
