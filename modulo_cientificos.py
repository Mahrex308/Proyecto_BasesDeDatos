import utilerias as lb

# Op. 1 - Baja de cientificos 
def altas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- ALTA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")

# Op 2 - Baja de cientificos 
def bajas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- BAJA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")
    
# Op 3 - Consulta de cientificos
def consulta_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("------------- CONSULTA DE CIENTIFICOS ------------")
    print("--------------------------------------------------")

# Op 4 - Cambios de cientificos
def cambios_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("-------------- CAMBIOS DE CIENTIFICOS ------------")
    print("--------------------------------------------------")

# Menu del modulo de cientificos
def menu_cientificos():
    op=-1
    while op!=5:
        lb.limpia_pantalla()
        print("--------------------------------------------------")
        print("---------------- MENU CIENTIFICOS ----------------")
        print("--------------------------------------------------")
        print("1)  Altas de cientificos")
        print("2)  Bajas de cientificos")
        print("3)  Consulta de cientificos")
        print("4)  Cambios de cientificos")
        print("5)  Regresar al menú principal")
        print("-------------------------------------------------")

        op=lb.pide_entero(1, 5, "Indica la opcion deseada : ")
        if op==1:
            altas_cientificos()
        if op==2:
            bajas_cientificos()
        if op==3:
            consulta_cientificos()
        if op==4:
            cambios_cientificos()
    lb.limpia_pantalla()


