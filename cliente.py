#!/usr/bin/python
import pymysql
import datetime

"""
Para sacar los nombres de las columnas de una tabla se usa
SELECT `COLUMN_NAME`
FROM `INFORMATION_SCHEMA`.`COLUMNS`
WHERE `TABLE_SCHEMA`='yourdatabasename'
AND `TABLE_NAME`='yourtablename';
"""

"""
Funciones auxiliares
"""

def imprimeEstudiante(estudiante):
    for atributo in estudiante:
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
        imprimeEstudiante(fila)
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
        imprimeEstudiante(fila)

def consultaPersonalizada():
    consulta = input("Introducir consulta: ")
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    for fila in resultado:
        imprimeEstudiante(fila)

def guardarCambios():
    conexion.commit()

"""
Función principal
"""

def main():
    global cursor, conexion
    # Nos conectamos a la BD
    conexion = pymysql.connect(user='antonio', password='archlinux', database='RedSocialUGR')
    # Tomamos un cursor (no sé muy bien qué es pero supongo que será lo que hace las consultas)
    cursor = conexion.cursor()

    menu = {}
    menu[1] = ("Alta de estudiante", altaEstudiante)
    menu[2] = ("Baja de estudiante", bajaEstudiante)
    menu[3] = ("Modificar estudiante", modificarEstudiante)
    menu[4] = ("Buscar estudiantes por carrera", buscarEstudiantesPorCarrera)
    menu[5] = ("Buscar estudiantes por centro", buscarEstudiantesPorCentro)
    menu[6] = ("Buscar estudiantes por asignatura", buscarEstudiantesPorAsignatura)
    menu[7] = ("Buscar estudiantes por nombre", buscarEstudiantesPorNombre)
    menu[8] = ("Matricular asignatura", matricularAsignatura)
    menu[9] = ("Superar asignatura", superarAsignatura)
    menu[10] = ("Abandonar asignatura", abandonarAsignatura)
    menu[11] = ("Consultar estudiante", consultarEstudiante)
    menu[12] = ("Consulta personalizada", consultaPersonalizada)
    menu[13] = ("Guardar cambios", guardarCambios)

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
