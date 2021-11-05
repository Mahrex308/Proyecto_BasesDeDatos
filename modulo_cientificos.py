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

    # FALTAN LAS VALIDACIONES DE QUE SOLO SEAN NUMEROS EN EL "ID" Y EN "NUMERO TELEFONICO"
    # Comprobar con el doc
    # Corregir ortografia dentro de los mensajes de error y de los input


# Op 2 - Baja de cientificos 
def bajas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- BAJA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")
    id_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico a eliminar : ")

    query="DELETE FROM cientificos WHERE id_ci='"+id_ci+"'"
    seguro=lb.pide_cadena(1, 1, "¿Seguro de querer eliminar? [S/N] : ")
    seguro=seguro.upper()
    if seguro=="S":
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()
        x=cursor.execute(query)
        if x==0:
            lb.error("ERROR, ID inexistente en el archivo de alumnos")
        else:
            lb.error("El registro ha sido eliminado correctamente")
        cone_bd.commit()
        cone_bd.close()
    else:
        lb.error("La accion de eliminar ha sido cancelada")

    # Probar las validaciones
    # Checar la ortografia

    
# Op 3 - Consulta de cientificos
def consulta_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("------------- CONSULTA DE CIENTIFICOS ------------")
    print("--------------------------------------------------")
    id_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico a consultar : ")
    
    query="SELECT * FROM cientificos WHERE id_ci='"+id_ci+"'"
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    if x==0:
        lb.error("ERROR, matricula inexistente en el archivo de alumnos")
    else:
        datos_cientificos=cursor.fetchone()
        print("Nombre             : ",datos_cientificos[1])
        print("Ap. Paterno        : ",datos_cientificos[2])
        print("Ap. Materno        : ",datos_cientificos[3])
        print("Numero de telefono : ",datos_cientificos[4])
        print("Correo             : ",datos_cientificos[5])
        lb.error(" ")
    cone_bd.close()

    # Checar validaciones
    # Checar la ortografia de los input y de los mensajes de error


# Op 4 - Cambios de cientificos
def cambios_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- CAMBIOS CIENTIFICOS --------------")
    print("--------------------------------------------------")
    id_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico : ")

    # Hacer un pequeño menu para hacer que el usuario elija si quiere cambiar
    # uno de los dos datos o los dos datos, (correo, telefono o ambos)

    # Checar la ortografia de las salidas y de los input 


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


