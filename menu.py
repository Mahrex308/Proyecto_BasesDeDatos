import utilerias as lb

import modulo_cientificos as mc
# import modulo_proyectos as mp

def menu_principal():
    op=-1
    while op!=4:
        lb.limpia_pantalla()
        print("--------------------------------------------------")
        print("----------------- MENU PRINCIPAL -----------------")
        print("--------------------------------------------------")
        print("1)  Cientificos")
        print("2)  Proyectos")
        print("3)  Reportes")
        print("4)  Terminar")
        

        op=lb.pide_entero(1, 4, "Indica la opcion deseada : ")
        if op==1:
            mc.menu_cientificos()
        if op==2:
            print("Opcion 2")
        if op==3:
            # Menu de Reportes
            print("Opcion 3")
        if op==4:
            # Terminar
            print("Opcion 4")

# Principal
menu_principal() 
