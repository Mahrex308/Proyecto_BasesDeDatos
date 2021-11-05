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