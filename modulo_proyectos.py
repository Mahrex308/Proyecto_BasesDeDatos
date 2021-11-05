import utilerias as lb


def altas_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- ALTA DE PROYECTOS ----------------")
    print("--------------------------------------------------")


def bajas_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- BAJA DE PROYECTOS ----------------")
    print("--------------------------------------------------")


def consulta_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("-------------- CONSULTA DE PROYECTOS -------------")
    print("--------------------------------------------------")


def cambios_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("---------------- CAMBIO PROYECTOS ----------------")
    print("--------------------------------------------------")


# Menu del modulo de proyectos
def menu_cientificos():
    op=-1
    while op!=5:
        lb.limpia_pantalla()
        print("--------------------------------------------------")
        print("---------------- MENU PROYECTOS ------------------")
        print("--------------------------------------------------")
        print("1)  Altas de proyectos")
        print("2)  Bajas de proyectos")
        print("3)  Consulta de proyectos")
        print("4)  Cambios de proyectos")
        print("5)  Regresar al menú principal")
        print("-------------------------------------------------")

        op=lb.pide_entero(1, 5, "Indica la opcion deseada : ")
        if op==1:
            altas_proyectos()
        if op==2:
            bajas_proyectos()
        if op==3:
            consulta_proyectos()
        if op==4:
            cambios_proyectos()
    lb.limpia_pantalla()