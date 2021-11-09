import utilerias as lb


# Alta de proyectos
def altas_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- ALTA DE PROYECTOS ----------------")
    print("--------------------------------------------------")
    id_pro=lb.pide_cadena(5, 5,            "Indica el numero de proyecto : ")
    nombre_pro=lb.pide_cadena(1, 15,       "Indica el nombre del proyecto : ")
    area_pro=lb.pide_cadena(1, 15,         "Indica el area de investigacion del proyecto : ")
    descripcion_pro=lb.pide_cadena(1, 200, "Inserta una breve descripcion del proyecto : ")
    id_ci_pro=lb.pide_cadena(5, 5,         "Indica el ID del cientifico responsable del proyecto : ")

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    query="INSERT INTO proyectos VALUES ('"+id_pro+"','"+nombre_pro+"','"+area_pro+"','"+descripcion_pro+"')"



# Baja de proyectos
def bajas_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("--------------- BAJA DE PROYECTOS ----------------")
    print("--------------------------------------------------")
    id_pro=lb.pide_cadena(5, 5, "Indica el numero de proyecto a eliminar : ")

    query="DELETE FROM proyectos WHERE id_pro='"+id_pro+"'"

    seguro=lb.pide_cadena(1, 1, "¿Seguro de eliminar? [S/N] : ")
    seguro=seguro.upper()
    if seguro=="S":
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()
        x=cursor.execute(query)
        if x==0:
            lb.error("ERROR, numero de proyecto inexistente en el archvio de proyectos")
        else:
            lb.error("El registro ha sido eliminado correctamente")
        cone_bd.commit()
        cone_bd.close()
    else:
        lb.error("La accion de eliminar ha sido cancelada")

    # Checar que funcione
    # Checar y corregir la ortografia dentro de los mensajes de error y de los input


# Consulta de proyectos
def consulta_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("-------------- CONSULTA DE PROYECTOS -------------")
    print("--------------------------------------------------")
    id_pro=lb.pide_cadena(5, 5, "Indica el numero de proyecto a consultar : ")
    
    query="SELECT * FROM proyectos WHERE id_pro='"+id_pro+"'"

    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    if x==0:
        lb.error("ERROR, clave inexistente en el archivo de materias")
    else:
        datos_proyectos=cursor.fetchone()
        print("Nombre              : ", datos_proyectos[1])
        print("Area                : ", datos_proyectos[2])
        print("Descripcion         : ", datos_proyectos[3])
        print("Cientifico asignado : ", datos_proyectos[4])
        lb.error(" ")
    cone_bd.close()

    # Checar que funcione
    # Checar y corregir ortografia en los input y mensajes de error


# Cambios de proyectos
def cambios_proyectos():
    lb.limpia_pantalla()
    print("--------------------------------------------------")
    print("---------------- CAMBIO PROYECTOS ----------------")
    print("--------------------------------------------------")
    id_pro=lb.pide_cadena(5, 5, "Indica el numero de proyecto : ")
    id_ci_pro=lb.pide_cadena(5, 5, "Indica el ID del nuevo cientifico encargado del proyecto : ")

    query="UPDATE proyectos SET id_ci_pro='"+id_ci_pro+"' WHERE id_pro='"+id_pro+"'"
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    if x==0:
        lb.error("ERROR, el numero de proyecto no existe en archivo de proyectos")
    else:
        lb.error("El cambio ha sido realizado")
    cone_bd.commit()
    cone_bd.close()

    # Checar que sirva
    # Checar y corregir ortografia


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

    # Checar ortografia