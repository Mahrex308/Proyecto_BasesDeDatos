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


def error(Let):
    print(Let)
    print("Oprima [Enter] para continuar")
    input()

