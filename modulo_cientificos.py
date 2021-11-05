import utilerias as lb

# Op. 1 - Baja de cientificos 
def altas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- ALTA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")
    id_ci=lb.pide_cadena(5, 5,      "Indica el ID                 : ")
    nombre_ci=lb.pide_cadena(1, 15, "Indica el Nombre             : ")
    ap_ci=lb.pide_cadena(1, 15,     "Indica el Ap. Paterno        : ")
    am_ci=lb.pide_cadena(1, 15,     "Indica el Ap. Materno        : ")
    tel_ci=lb.pide_cadena(10, 10,   "Indica el Numero de telefono : ")
    correo_ci=lb.pide_cadena(1, 30, "Indica el Correo             : ")

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    query="INSERT INTO cientificos VALUES ('"+id_ci+"','"+nombre_ci+"','"+ap_ci+"','"+am_ci+"','"+tel_ci+"','"+correo_ci+"')"

    # print(query)
    seguro=lb.pide_cadena(1, 1, "Los datos son correctos ¿Desea grabar? [S/N] : ")
    seguro=seguro.upper()
    if seguro=="S":
        try:
            x=cursor.execute(query)
        except:
            x=0
        if x==0:
            lb.error("ERROR, el ID se duplica en el archivo de alumnos")
        else:
            lb.error("Los datos han sido grabados correctamente")
    else:
        lb.error("La accion de grabar ha sido cancelada")
    cone_bd.commit()
    cone_bd.close()



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


