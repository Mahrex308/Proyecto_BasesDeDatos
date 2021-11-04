import utilerias as lb


def menu_principal():
    op=-1
    while op!=0:
        lb.limpia_pantalla()
        print("--------------------------------------------------")
        print("----------------- MENU PRINCIPAL -----------------")
        print("--------------------------------------------------")
        print("1)  Cientificos")
        print("2)  Proyectos")
        print("3)  Reportes")
        print("4)  Terminar")

        op=lb.pide_entero(0, 4, "Indica la opcion deseada : ")
        if op==1:
            # Menu de Cientificos
        if op==2:
            # Menu de Proyectos
        if op==3:
            # Menu de Reportes
        if op==4:
            # Terminar

# Principal
menu_principal()
