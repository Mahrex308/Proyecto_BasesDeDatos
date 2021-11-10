import utilerias as lb


# Op. 1 - Baja de cientificos 
def altas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- ALTA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")

    # vid=lb.pide_cadena(5, 5,      "Indica el ID                 : ")
    vid_ci=lb.pide_id("Indica el ID                 : ")
    vnom_ci=lb.pide_cadena(1, 15, "Indica el Nombre             : ")
    vap_ci=lb.pide_cadena(1, 15,  "Indica el Ap. Paterno        : ")
    vam_ci=lb.pide_cadena(1, 15,  "Indica el Ap. Materno        : ")
    # vtel_ci=lb.pide_cadena(10, 10,   "Indica el Numero de telefono : ")
    vtel_ci=lb.pide_telefono("Indica el Numero de telefono : ")
    # vcor_ci=lb.pide_cadena(3, 30, "Indica el Correo             : ")
    vcor_ci=lb.pide_correo("Indica el Correo             : ")

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    query="INSERT INTO cientificos VALUES ('"+vid_ci+"','"+vnom_ci+"','"+vap_ci+"','"+vam_ci+"','"+vtel_ci+"','"+vcor_ci+"')"

    # print(query)
    seguro=lb.pide_cadena(1, 1, "Los datos son correctos ¿Desea grabar? [S/N] : ")
    seguro=seguro.upper()
    if seguro=="S":
        try:
            x=cursor.execute(query)
        except:
            x=0
        if x==0:
            lb.error("ERROR, el ID se duplica en el archivo de cientificos")
        else:
            lb.error("Los datos han sido grabados correctamente")
    else:
        lb.error("La accion de grabar ha sido cancelada")
    cone_bd.commit()
    cone_bd.close()

    # Probar
    # Corregir ortografia dentro de los mensajes de error y de los input


# Op 2 - Baja de cientificos 
def bajas_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- BAJA DE CIENTIFICOS --------------")
    print("--------------------------------------------------")

    # vid_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico a eliminar : ")
    vid_ci=lb.pide_id("Indica el ID del cientifico a eliminar : ")

    query="DELETE FROM cientificos WHERE id_ci='"+vid_ci+"'"
    seguro=lb.pide_cadena(1, 1, "¿Seguro de querer eliminar? [S/N] : ")
    seguro=seguro.upper()
    if seguro=="S":
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()
        x=cursor.execute(query)
        if x==0:
            lb.error("ERROR, ID inexistente en el archivo de cientificos")
        else:
            lb.error("El registro ha sido eliminado correctamente")
        cone_bd.commit()
        cone_bd.close()
    else:
        lb.error("La accion de eliminar ha sido cancelada")

    # Probar 
    # Checar la ortografia

    
# Op 3 - Consulta de cientificos
def consulta_cientificos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("------------- CONSULTA DE CIENTIFICOS ------------")
    print("--------------------------------------------------")

    # vid_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico a consultar : ")
    vid_ci=lb.pide_id("Indica el ID del cientifico a consultar : ")
    
    query="SELECT * FROM cientificos WHERE id_ci='"+vid_ci+"'"
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    if x==0:
        lb.error("ERROR, ID inexistente en el archivo de cientificos")
    else:
        datos_cientificos=cursor.fetchone()
        print("Nombre             : ",datos_cientificos[1])
        print("Ap. Paterno        : ",datos_cientificos[2])
        print("Ap. Materno        : ",datos_cientificos[3])
        print("Numero de telefono : ",datos_cientificos[4])
        print("Correo             : ",datos_cientificos[5])
        lb.error(" ")
    cone_bd.close()

    # Probar
    # Checar la ortografia de los input y de los mensajes de error


# Op 4 - Cambios de cientificos
def cambios_cientificos():
    op=-1
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- CAMBIOS CIENTIFICOS --------------")
    print("--------------------------------------------------")

    # vid_ci=lb.pide_cadena(5, 5, "Indica el ID del cientifico : ")
    vid_ci=lb.pide_id("Indica el ID del cientifico : ")

    while op!=3:
        lb.limpia_pantalla()
        print("*************** ¿QUE DESEA CAMBIAR? **************")
        print("1)  Numero telefonico")
        print("2)  Correo")
        # print("n)  Ambos")
        print("3)  Terminar")
        print("**************************************************")
        op=lb.pide_entero(1, 3, "Indica la opcion deseada : ")
        if op==1:
            vtel_ci=lb.pide_telefono("Indica el NUEVO numero telefonico  : ")
            query="UPDATE cientificos SET tel_ci='"+vtel_ci+"' WHERE id_ci='"+vid_ci+"'"
            
        if op==2:
            vcor_ci=lb.pide_correo("Indica el NUEVO correo electronico :")
            query="UPDATE cientificos SET correo_ci='"+vcor_ci+"' WHERE id_ci='"+vid_ci+"'"
    
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)

    if x==0:
        lb.error("ERROR, el ID no existe en el archivo de cientificos")
    else:
        lb.error("El cambio ha sido realizado")
    cone_bd.commit()
    cone_bd.close()

    

    

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


