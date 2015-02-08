#!/usr/bin/python
import pymysql

# Realizamos consultas
#some_name = 'Georgi'
#cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (some_name))
#cursor.execute("SELECT correo,nombre,nombre_carrera FROM estudiantes,cursa WHERE estudiantes.correo=cursa.correo_alumno ")

    # Con los datos obtenidos hacemos lo que queramos
    # for correo,nombre,carrera in cursor:
    #     print(correo + " -> " + nombre + " -> " + carrera)


"""
Para sacar los nombres de las columnas de una tabla se usa
SELECT `COLUMN_NAME`
FROM `INFORMATION_SCHEMA`.`COLUMNS`
WHERE `TABLE_SCHEMA`='yourdatabasename'
AND `TABLE_NAME`='yourtablename';
"""

"""
Funciones auxiliares para no recargar el main
"""
def altaEstudiante():

    cursor.execute('SELECT COLUMN_NAME  \
    FROM INFORMATION_SCHEMA.COLUMNS \
    WHERE TABLE_SCHEMA= \'RedSocialUGR\' \
    AND TABLE_NAME=\'estudiantes\'')


    # Probamos con correo y nombre solo

    for columna in cursor:
        print(columna[0])

    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")

    cursor.execute("INSERT INTO estudiantes(correo,nombre,apellidos) VALUES (%s,%s,%s)",(correo,nombre,apellidos))





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
        print(fila)
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
        print(fila)

def consultaPersonalizada():
    consulta = input("Introducir consulta: ")
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    for fila in resultado:
        print(fila)

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
    menu[1] = "Alta de estudiante"
    menu[2] = "Baja de estudiante"
    menu[3] = "Modificar estudiante"
    menu[4] = "Buscar estudiantes por carrera"
    menu[5] = "Buscar estudiantes por centro"
    menu[6] = "Buscar estudiantes por asignatura"
    menu[7] = "Buscar estudiantes por nombre"
    menu[8] = "Matricular asignatura"
    menu[9] = "Superar asignatura"
    menu[10] = "Abandonar asignatura"
    menu[11] = "Consultar estudiante"
    menu[12] = "Consulta personalizada"
    menu[13] = "Guardar cambios"

    funcion = {}
    funcion["1"] = altaEstudiante
    funcion["2"] = bajaEstudiante
    funcion["3"] = modificarEstudiante
    funcion["4"] = buscarEstudiantesPorCarrera
    funcion["5"] = buscarEstudiantesPorCentro
    funcion["6"] = buscarEstudiantesPorAsignatura
    funcion["7"] = buscarEstudiantesPorNombre
    funcion["8"] = matricularAsignatura
    funcion["9"] = superarAsignatura
    funcion["10"] = abandonarAsignatura
    funcion["11"] = consultarEstudiante
    funcion["12"] = consultaPersonalizada
    funcion["13"] = guardarCambios

    while True:
        opciones = sorted(menu, key=menu.get)
        opciones.sort()
        print("---------------------------")
        for item in opciones:
            print(str(item) + " -> " + menu[item])

        seleccion = input("\nQué quieres hacer? ")
        if seleccion in funcion.keys():
            funcion[seleccion]()
        elif seleccion == "Q" or seleccion == "q":
            break
        else:
            print("No es una buena opción")

    print("Cerrando conexión")
    # Cerrar conexión a la BD
    conexion.close()


if __name__ == "__main__":
    main()
