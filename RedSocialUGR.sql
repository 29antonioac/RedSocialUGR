 -- Sentencias para la creación de la BD del SI "Red Social UGR"

 -- Borrado de lo anterior (si existiera)
 DROP DATABASE IF EXISTS RedSocialUGR;
 CREATE DATABASE IF NOT EXISTS RedSocialUGR;
 USE RedSocialUGR;

 DROP TABLE IF EXISTS estudiantes,
                      carreras;

 -- La creación de tablas hay que hacerla en conjunto, pero las separo para comprender mejor el código

 -- Creación de la tabla de estudiantes

 CREATE TABLE estudiantes (
   Correo           VARCHAR(50) NOT NULL,
   Nombre           VARCHAR(50) NOT NULL,
   Apellidos        VARCHAR(50) NOT NULL,
   FechaNacimiento  DATE        NOT NULL,
   FotoPersonal     VARCHAR(70) DEFAULT NULL,
   Destrezas        VARCHAR(50) DEFAULT NULL,
   Hobbies          VARCHAR(50) DEFAULT NULL,
   EstadoActual     VARCHAR(30) DEFAULT NULL,
   Ocupacion        VARCHAR(30) DEFAULT NULL,
   PRIMARY KEY(correo)
 );

 CREATE TABLE carreras (
   Nombre         VARCHAR(30) NOT NULL,
   Centro         VARCHAR(30) NOT NULL,
   PRIMARY KEY(nombre)
 );

 CREATE TABLE cursa (
   Correo_alumno  VARCHAR(50) NOT NULL,
   Nombre_carrera VARCHAR(50) NOT NULL,
   KEY            (correo_alumno),
   KEY            (nombre_carrera),
   FOREIGN KEY    (correo_alumno)   REFERENCES estudiantes  (correo)  ON DELETE CASCADE,
   FOREIGN KEY    (nombre_carrera)  REFERENCES carreras     (nombre)  ON DELETE CASCADE
 );


 -- Creación de la tabla de asignaturas-centros


 -- Creación de la tabla actividades


 -- Creación de la tabla muros


 -- NOTA: Lo suyo es echar esto a otros archivos y traerlos con "source <file>;"
 -- Inserción de tuplas en estudiantes

 -- correo           VARCHAR(50) NOT NULL,
 -- nombre           VARCHAR(50) NOT NULL,
 -- apellidos        VARCHAR(50) NOT NULL,
 -- fechaNacimiento  DATE        NOT NULL,

 INSERT INTO estudiantes (correo,nombre,apellidos,fechaNacimiento) VALUES
 ('analca3@correo.ugr.es','Antonio','Álvarez Caballero',"29/11/1993"),
 ('evamariagg@correo.ugr.es','Eva María','González García',"08/07/1992"),
 ('cparadela@correo.ugr.es','Carlos','Paradela Pérez',"17/03/1992"),
 ('adrianranea@correo.ugr.es','Adrián','Ranea Robles',"07/12/1993");

 -- Inserción de tuplas en carreras

 -- nombre         VARCHAR(30) NOT NULL,
 -- centro         VARCHAR(30) NOT NULL,
 -- PRIMARY KEY(nombre)

 INSERT INTO carreras (nombre, centro) VALUES
 ('Doble Grado', 'ETSIIT/Ciencias');

 -- Inserción de tuplas en cursa
 -- correo_alumno  VARCHAR(50) NOT NULL,
 -- nombre_carrera VARCHAR(50) NOT NULL,

 INSERT INTO cursa (correo_alumno, nombre_carrera) VALUES
 ('analca3@correo.ugr.es','Doble Grado'),
 ('evamariagg@correo.ugr.es','Doble Grado'),
 ('cparadela@correo.ugr.es','Doble Grado'),
 ('adrianranea@correo.ugr.es','Doble Grado');
