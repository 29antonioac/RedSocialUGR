#!/usr/bin/python
import pymysql
import datetime

"""
Funciones auxiliares
"""

def imprime(fila):
    for atributo in fila:
        if isinstance(atributo,datetime.date):
            print(atributo.strftime('%d/%m/%Y'),end=" | "),
        else:
            print(atributo,end=" | "),

    print()



"""
Funciones principales
"""
def altaEstudiante():

    # Cogemos las columnas disponibles (para pedir todos los datos disponibles)
    cursor.execute('SELECT COLUMN_NAME  \
    FROM INFORMATION_SCHEMA.COLUMNS \
    WHERE TABLE_SCHEMA= \'RedSocialUGR\' \
    AND TABLE_NAME=\'estudiantes\'')

    # Tomamos para cada columna el valor deseado por teclado
    argumentos = []
    for columna in cursor:
        valor = input(columna[0] + ": ")
        if valor == "":
            valor = None
        argumentos.append(valor)

    # Lo convertimos a tupla y lanzamos la consulta
    entrada = tuple(argumentos)
    cursor.execute("INSERT INTO estudiantes VALUES %s",(entrada,))


def bajaEstudiante():
    correo = input("Correo del estudiante a buscar: ")
    cursor.execute("DELETE FROM estudiantes WHERE correo=%s",(correo))

def crearForo():
    idForo = int(input("Id foro: "))
    nombreForo = input("Nombre del Foro: ")

    cursor.execute("INSERT INTO foro VALUES (%s,%s)",(idForo,nombreForo))


def modificarCentroCarrera():
    nombreCarrera = input("Nombre de la carrera a modificar: ")
    valorAtributo = input("Nombre del centro: ")

    cursor.execute("UPDATE carrera SET Centro=%s WHERE NombreCarrera=%s", (valorAtributo,nombreCarrera))

def modificarDescripcionActividad():
    NombreActividad = input("Nombre de la actividad a modificar: ")
    CorreoCreador = input("Correo del creador: ")
    descripcion = input("Descripción: ")

    cursor.execute("UPDATE actividad SET Descripcion=%s WHERE CorreoCreador=%s AND NombreActividad=%s", (descripcion,CorreoCreador,NombreActividad))


def modificarEstudiante():
    pass
def buscarEstudiantesPorCarrera():
    pass
def buscarEstudiantesPorCentro():
    pass
def buscarEstudiantesPorAsignatura():
    pass
def buscarEstudiantesPorNombre():
    nombre = input("Nombre del estudiante a buscar: ")
    cursor.execute("SELECT * FROM estudiantes WHERE nombre=%s",(nombre))
    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)

def matricularAsignatura():
    pass
def superarAsignatura():
    pass
def abandonarAsignatura():
    pass
def consultarEstudiante():
    correo = input("Correo del estudiante a buscar: ")
    cursor.execute("SELECT * FROM estudiantes WHERE correo=%s",(correo))
    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)

def consultarCarrera():
    carrera = input("Carrera a consultar: ")
    cursor.execute("SELECT * FROM carrera WHERE NombreCarrera=%s",(carrera))

    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)

def consultarActividad():
    actividad = input("Actividad a consultar: ")
    correo = input("Creador: ")
    cursor.execute("SELECT * FROM actividad WHERE NombreActividad=%s AND CorreoCreador=%s",(actividad,correo))

    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)

def consultarForo():
    foro = int(input("Identificador a consultar: "))
    cursor.execute("SELECT * FROM foro WHERE IdentificadorForo=%s",(foro))

    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)


def consultaPersonalizada():
    consulta = input("Introducir consulta: ")
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    for fila in resultado:
        imprime(fila)

def guardarCambios():
    conexion.commit()

"""
Función principal
"""

def main():
    global cursor, conexion
    # Nos conectamos a la BD
    conexion = pymysql.connect(user='antonio', password='archlinux', database='RedSocialUGR')
    # Tomamos un cursor
    cursor = conexion.cursor()

    menu = {}
    menu[1] = ("Alta de estudiante",    altaEstudiante)
    menu[2] = ("Baja de estudiante",    bajaEstudiante)
    menu[3] = ("Crear foro",            crearForo)
    menu[4] = ("Modificar centro de carrera",     modificarCentroCarrera)
    menu[5] = ("Modificar descripción una actividad", modificarDescripcionActividad)

    menu[11] = ("Consultar estudiante",     consultarEstudiante)
    menu[12] = ("Consultar carrera",        consultarCarrera)
    menu[13] = ("Consultar actividad",      consultarActividad)
    menu[14] = ("Consultar foro",           consultarForo)
    menu[30] = ("Consulta personalizada",   consultaPersonalizada)
    menu[31] = ("Guardar cambios",          guardarCambios)

    while True:
        # Ordenamos las opciones del menú
        opciones = sorted(menu, key=menu.get)
        opciones.sort()
        # Imprimimos las opciones del menú
        print("---------------------------")
        for item in opciones:
            print(str(item) + " -> " + menu[item][0])
        print("Q para salir")

        # Seleccionamos una opción
        seleccion = input("\nQué quieres hacer? ")

        if seleccion == "":
            print("No has seleccionado nada")
        elif seleccion == "Q" or seleccion == "q":
            # Salir
            break
        elif int(seleccion) in menu.keys():
            # Tomamos el segundo elemento de la tupla ítem de menu (es una función)
            menu[int(seleccion)][1]()
        else:
            # Opción inválida
            print("No es una buena opción")

    # Si se pulsa Q, cerrar la conexión
    print("Cerrando conexión")
    conexion.close()


if __name__ == "__main__":
    main()
