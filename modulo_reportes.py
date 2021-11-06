import utilerias as lb


# Menu del modulo de proyectos
def menu_cientificos():
    op=-1
    while op!=6:
        lb.limpia_pantalla()
        print("--------------------------------------------------")
        print("----------------- MENU REPORTES ------------------")
        print("--------------------------------------------------")
        print("1)  Lista de cientificos")
        print("2)  Lista de proyectos")
        print("3)  Lista de proyectos por area")
        print("4)  Lista de cientificos por area")
        print("5)  Lista de proyectos asignados a un cientifico")
        print("6)  Regresar al menú principal")
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