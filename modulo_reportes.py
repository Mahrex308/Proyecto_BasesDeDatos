import utilerias as lb

def espa(posiciones, elemento):
    x=(posiciones-len(elemento))*" "
    return x




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
            reportes_proyecto_area()
        if op==4:
            cientificos_proyecto_area()
        if op==5:
            proyectos_asignados_cientifico()
    lb.limpia_pantalla()

def reportes_proyecto_area():
    lb.limpia_pantalla()
    varea=lb.pide_cadena(1, 15,         "Indica el area de investigacion del proyecto : ")
    query="SELECT * FROM proyectos WHERE area_pro='"+varea+"' ORDER BY id_pro, nombre_pro, descripcion_pro, id_ci_pro"
    lb.limpia_pantalla()
    print("----------------------------------------------------------------------------------------------------")
    print("------------------------------ LISTADO DE PROYECTOS ORDENADOS POR AREA -----------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("Id     Nombre                        Descripción                  ID del Cientifico                 ")
    #      12345  123456789/12345  123456789/123456789/123456789/123456789/  12345
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    lista=cursor.fetchall()
    for reg in lista:
        print(reg[0]+espa(7,reg[0])+reg[1]+espa(17,reg[1])+reg[2]+espa(202,reg[2])+reg[3])
    lb.error("")
    cone_bd.close()

def cientificos_proyecto_area():
    lb.limpia_pantalla()
    varea=lb.pide_cadena(1, 15, "Indica el area de investigacion del proyecto : ")

    query="SELECT id_ci, nombre_ci, ap_ci, am_ci, tel_ci, correo_ci"
    query+="  FROM cientificos, proyectos"
    query+="  WHERE area_pro='"+varea+"'and id_ci=id_ci_pro"
    
    lb.limpia_pantalla()
    print("----------------------------------------------------------------------------------------------------")
    print("---------------------------------- LISTA DE CIENTIFICOS POR AREA -----------------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("ID     Nombre           Ap. Paterno      Ap. Materno      Telefono    Correo                        ")
    #      12345  123456789/12345  123456789/12345  123456789/12345  123456789/  123456789/123456789/123456789/
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    lista=cursor.fetchall()
    for reg in lista:
        print(reg[0]+espa(17,reg[0])+reg[1]+espa(17,reg[1])+reg[2]+espa(17,reg[2])+reg[3]+espa(12,reg[3])+reg[4])
    lb.error("")
    cone_bd.close()


def proyectos_asignados_cientifico():
    lb.limpia_pantalla()
    vid=lb.pide_cadena(1, 5,         "Indica el Id del cientifico : ")
    query="SELECT id_pro, nombre_pro, area_pro, descripcion_pro"
    query+="FROM proyectos"
    query+="WHERE id_ci_pro='"+vid+"'"
    lb.limpia_pantalla()
    print("----------------------------------------------------------------------------------------------------")
    print("--------------------------- LISTA DE PROYECTOS ASIGNADOS A UN CIENTIFICO ---------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("ID     Nombre           Area             Descripción                                                ")
    #      12345  123456789/12345  123456789/12345  123456789/123456789/123456789/123456789/
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    lista=cursor.fetchall()
    for reg in lista:
        print(reg[0]+espa(7,reg[0])+reg[1]+espa(17,reg[1])+reg[2]+espa(17,reg[2])+reg[3]+espa(202,reg[3])
    lb.error("")
    cone_bd.close()
