import pymysql as my

def limpia_pantalla():
    for i in range(45):
        print()

def pide_entero(Li, Ls, Let):
    valor=Ls+1
    while valor<Li or valor>Ls:
        valor=int(input(Let))
        if valor<Li or valor>Ls:
            print("Error")
            input()
    return(valor)

def pide_flotante(Li, Ls, Let):
    valor=Ls+1
    while valor<Li or valor>Ls:
        valor=float(input(Let))
        if valor<Li or valor>Ls:
            print("Error")
            input()
    return(valor)

def pide_cadena(Li, Ls, Let):
    longitud=Li-1
    while longitud<Li or longitud>Ls:
        cadena=input(Let)
        longitud=len(cadena)
        if longitud<Li or longitud>Ls:
            print("Error")
            input()
    return(cadena)

def error(Let):
    print(Let)
    print("Oprima [Enter] para continuar")
    input()

def pausa():
    input("[ENTER] para continuar")

def conectar_bd():
    cone_bd=my.connect(host="localhost",user="root",password="",database="sistema_alumnos_materia_clase")
    return(cone_bd)
    # Checar

def pide_id(Let):
    longitud=0
    cadena="Hello"
    while longitud != 5 or cadena.isnumeric() != True:
        cadena=input(Let)
        longitud=len(cadena)
        if longitud != 5 or cadena.isnumeric() != True:
            error("ERROR, el ID debe tener exactamente 5 digitos numericos (Ej. 00001)")
    return(cadena)

def pide_telefono(Let):
    longitud=0
    cadena="Hello"
    while longitud != 10 or cadena.isnumeric() !=  True:
        cadena=input(Let)
        longitud=len(cadena)
        if longitud != 10 or cadena.isnumeric() != True:
            error("ERROR, el Numero telefonico debe tener exactamente 10 digitos numericos (Ej. 7221234567)")
    return(cadena)

def pide_correo(Let):
    longitud=0
    correo=False
    while longitud < 3 or longitud > 30 or correo == False:
        cadena=input(Let)
        longitud=len(cadena)
        for i in range(0, longitud):
            if cadena[i]=="@":
                correo=True
        if longitud < 3 or longitud > 30 or correo == False:
            error("ERROR, el Correo debe de estar entre 3 y 30 caracteres y debe de tener un '@'")
    return(cadena)

