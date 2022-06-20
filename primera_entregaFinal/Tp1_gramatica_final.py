from utiles import obtener_color, obtener_palabras_validas
"""
Distrinucion del Tp:
    
    Santino Peiretti: validacion_caracteres
    
    Nicolas Nayar: validacion_caracteres, pintar_palabra, validacion_vocales, elegir_palabra
    
    Valentin Somoza: comienzo_partida, pintar, imprimir_tablero, asignador_intento, main, validacion_caracteres, pintar_palabra
    
    Diego Lavia: puntos, validacion_vocales, validacion caracteres, main, comienzo_partida, pintar_palabra
"""

import random
import time

LONGITUD_PALABRA_SECRETA = 5 
MAXIMO_PARTIDAS = 5
REINICIAR_ARCHIV0_PARTIDAS = False 

PUNTAJE_POR_GANAR = 50  
PUNTAJE_POR_PERDER = -100
PUNTAJE_POR_PERDER_V2 = -50
FILAS = 5
COLUMNAS = 5
ACENTOS = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )

def puntos(jugador, gano, intentos):
    """
    Esta funcion asigna el puntaje correspondiente dependiendo si el jugador gano o perdio, estas son variables globales
    hecho por Diego Lavia
    """
    if gano == True:
        jugador = PUNTAJE_POR_GANAR  - intentos * 10  # Lo pusimos porque el i nos da un 1(posicion) de mas
    else:
        jugador = PUNTAJE_POR_PERDER
 
    return jugador

def comienzo_partida(puntaje, elegido, jugador_1, jugador_2, puntajes_jugador_1, puntajes_jugador_2):
    """
    Esta funcion cuando se la llama empieza una partida, esta partida se compone de 5 intentos que se iteran a traves del while 
    En cada intento dentro del while se llama a distintas funciones para que valide la palabra, pinte la palabra y imprima la fila del tablero.
    Luego se le asignan los puntos a los jugadores (Esta parte no logramos que funcione correctamente) dependiendo si ganaron o no y quien fue el que gano.
    Cuando termina el while una parte pequeña del codigo que se compone de un if que se encarga de cambiar de turno para que en el siguiente intento juege el otro jugador.
    La funcion termina devolviendo los puntajes que se sumaran y imprimiran en el main

    Hipotesis: Para poder lograr que funcione correctamente la parte de puntos se plantea la siguiente logica:
    Cada vez que itera el while se pregunta si el usuario gano o perdio, entonces con este dato llamamos a la funcion puntos dandole el jugador ganador o perdedor.
    La funcion terminaria devolviendo 2 valores, el puntaje del jugador 1 y del jugador 2

    hecho por Valentin Somoza y  Diego Lavia
    """
    la_palabra_al_azar = elegir_palabra()   
    
    puntajes_a=0
    puntajes_b=0
    print(la_palabra_al_azar, "Es la palabra a adivinar") #Esto es auxiliar para probar el programa
    cartel_inicio=["?","?","?","?","?"]
    palabra_a_adivinar=" ".join(cartel_inicio)
    
    gano_perdio = False
    intentos=0
    while intentos < MAXIMO_PARTIDAS and gano_perdio == False:
        print(f"Ahora le toca jugar a {elegido}")
        print(f"Palabra a adivinar:   {palabra_a_adivinar}") # Esto es el cartel de signos de pregunta
        palabra_ingresar = input("ingrese el intento: ")
        
        while validacion_caracteres(palabra_ingresar) == False:
            palabra_ingresar = input("ingrese la palabra nuevamente: ")    
        print("la palabra con la que arriesgaste es: ", palabra_ingresar)
        
        palabra_pintada= pintar_palabra(palabra_ingresar, la_palabra_al_azar, palabra_a_adivinar)

        print(asignador_intento(palabra_pintada, intentos))
        
        if palabra_ingresar != la_palabra_al_azar:
            print(elegido)
            puntaje = puntos(elegido, gano_perdio, intentos)
            print("Perdiste")
            
        else:
            gano_perdio=True
            puntaje=puntos(elegido, gano_perdio, intentos)
            print(f"Ganaste! El jugador {elegido} obtuvo un total de {puntaje} puntos")
            
            
        if elegido == jugador_1:
            elegido = jugador_2
        else:
            elegido = jugador_1
        intentos += 1
        
    if intentos == 5:
        if elegido == jugador_1:
            puntajes_jugador_1+= PUNTAJE_POR_PERDER
            puntajes_jugador_2+= PUNTAJE_POR_PERDER_V2
        else:
            puntajes_jugador_1+= PUNTAJE_POR_PERDER_V2
            puntajes_jugador_2+= PUNTAJE_POR_PERDER
            
        print(f"El jugador {elegido} obtuvo un total de {puntaje} puntos")
        
    return puntaje, elegido, puntajes_jugador_1, puntajes_jugador_2, gano_perdio

    
    

def pintar(string, color):
    """
    Esta funcion recibe una string y un color, y devuelve la string pintada con ese color, a partir
    del archivo utiles dado por los profesores
    hecho por Valentin Somoza
    """
    palabra_pintada=obtener_color(color)+string
    return palabra_pintada
    

def validacion_vocales(caracteres):
    """
    Esta funcion reemplaza los acentos con el método .replace(), utilizando ACENTOS que es una variable global
    hecho por Nicolas Nayar y Diego Lavia
    """
    
    for acento, sin_acento in ACENTOS:
        caracteres = caracteres.replace(acento, sin_acento)
    
    print(caracteres) # hace falta dejar este print?
    
    return caracteres

def pintar_palabra(palabra_ingresar, la_palabra_al_azar, palabra_a_adivinar):
    """
    Recorre la palabra ingresada, letra por letra, la indexa y compara letra por letra
    con la palabra random que fue obtenida por la funcion elegir_palabra(), luego llamamos a la funcion pintar palabra y la agregamos a una nueva lista.
    Esta lista contiene toda la palabra pintada hecha a base de pintar letra por letra, luego se la transforma en string y la funcion termina devolviendo esa string
    hecho por Valentin Somoza, Nicolas Nayar y Diego Lavia
    """
    #Hipotesis: No logramos poner una lista con signos de pregunta y reemplazar las letras con verde.
    
    palabra_ingresar = palabra_ingresar.lower()
    
    lista_de_letras_pintadas = [] #era listin
    for j in range(len(palabra_ingresar)):
        if palabra_ingresar[j] == la_palabra_al_azar[j]:
            lista_de_letras_pintadas.append(pintar(palabra_ingresar[j], "Verde"))
#            verdes.append(pintar(palabra_ingresar[j], "Verde"))
        elif palabra_ingresar[j] in la_palabra_al_azar:
            lista_de_letras_pintadas.append(pintar(palabra_ingresar[j], "Amarillo"))
#            amarillos.append(pintar(palabra_ingresar[j], "Amarillo"))
        else:
            lista_de_letras_pintadas.append(pintar(palabra_ingresar[j], "GrisOscuro"))
#            grises.append(pintar(palabra_ingresar[j], "GrisOscuro"))
    string_de_letras_pintadas = "".join(lista_de_letras_pintadas)
    
    #Hipotesis: No logramos poner una lista con signos de pregunta y reemplazar las letras con verde.
    return string_de_letras_pintadas
    
def validacion_caracteres(palabra):
    """
    Esta funcion valida si no tiene numeros, y si la palabra tiene longitud 5
    ademas llama a la funcion validacion acentos
    hecho por Nicolas Nayar, Diego Lavia y Valentin Somoza
    esto fue modularizado por Santino Peiretti
    """
    caracteres = validacion_vocales(palabra)
    i = 0
    alfanumerico = 0
    validacion= False
    if len(caracteres) == LONGITUD_PALABRA_SECRETA:
        while len(caracteres)>i:
            if caracteres.isalpha():
                    alfanumerico += 1
            i+=1
        if alfanumerico == 0:
            validacion = False
            print("la palabra no debe tener caracteres especiales")
        else: 
            validacion = True   
    else:
        print(f"la palabra debe tener {LONGITUD_PALABRA_SECRETA} letras")
        
    return validacion
    
def elegir_palabra():
    """
    esta funcion elige una palabra al azar de todas las que hay, usando la libreria random
    hecho por Nicolas Nayar
    """
    """ funciona """
    palabra = obtener_palabras_validas()
    palabra_random =random.choice(palabra)
    return palabra_random

def asignador_intento(palabra_pintada, intentos):
    """
    imprime una fila del tablero, del intento actual
    hecho por Valentin Somoza
    """
    lista_palabra_pintada = palabra_pintada.split()
    string_palabra_pintada = "".join(lista_palabra_pintada)
    string_final = f"Intento {intentos} = {string_palabra_pintada}"
    return string_final

def main():
    """
    En el main entre otras cosas, calculamos el tiempo de cada partida en minutos/segundo, con la libreria time hecho:
    Diego Lavia, Valentin Somoza
    mostramos el tablero, asignamos el nombre de los jugadores, esto lo pasamos a una lista que luego con
    Random elige al azar quien empieza 
    hecho por: Diego Lavia y Valentin Somoza
    
    """
    inicio=time.time()
    
    tablero = {"intento_1": ["?", "?", "?", "?", "?"],
           "intento_2": ["?", "?", "?", "?", "?"],
           "intento_3": ["?", "?", "?", "?", "?"],
           "intento_4": ["?", "?", "?", "?", "?"],
           "intento_5": ["?", "?", "?", "?", "?"]}
    for intento, valores in tablero.items():
        print(f" {intento} : {valores} ")

    partida=0
    
    seguir_jugando=input("Presione Enter para empezar el juego!")
    
    jugador_1 = input("Ingrese el Nombre del jugador 1:  ")
    jugador_2 = input("Ingrese el Nombre del jugador 2:  ")
    jugadores = [jugador_1,jugador_2]
    elegido = random.choice(jugadores)

    puntaje_final=0
    puntajes_jugador_1=0
    puntajes_jugador_2=0
    puntaje=0
    seguir=True
    minutos=0
    """
    Este while llama a la funcion comienza partida que es donde se desarrolla el juego, antes de esto el tiempo
    empieza a correr y al salir de la funcion se termina de medir el tiempo, en el caso que la partida dure mas de 60 segundos,
    empieza a sumarse los minutos. Al terminar pregunta si se desea seguir jugando o no.
    hecho por Diego Lavia y Valentin Somoza
    
    """
    while seguir:
        
        inicio = time.time()
        
        print(f"Empieza un nuevo juego ! Partida Nº {partida + 1}")
        
        puntaje_final = comienzo_partida(puntaje, elegido, jugador_1, jugador_2, puntajes_jugador_1, puntajes_jugador_2)
        
        if puntaje_final[4] == True:
            if puntaje_final[1] == jugador_1:
                puntajes_jugador_1 += puntaje_final[0]
            else:
                puntajes_jugador_2 += puntaje_final[0]
        else:
            puntajes_jugador_1 += puntaje_final[2]
            puntajes_jugador_2 += puntaje_final[3]
            
        fin = time.time()
        total = fin - inicio
        total_int = int(total)
        
        minutos = total / 60
        minutos_int = int(minutos)
        segundos = total % 60
        segundos_int = int(segundos)

        print("Tardaste", minutos_int,"minutos y ",segundos_int,"segundos")
        
        
        
        print(f"El jugador", jugador_1, "tiene acumulado", puntajes_jugador_1," puntos")
        print(f"El jugador", jugador_2, "tiene acumulado", puntajes_jugador_2," puntos")
#         print(f"El jugador {elegido} tiene acumulados {puntaje_final} puntos")
        
        seguir_jugando=input("¿Desea seguir jugando? - - conteste S/N: ")
        seguir_jugando=seguir_jugando.lower()
        
        if seguir_jugando == "n":
            seguir=False
        partida+=1

    print("El juego termino")

    
main()