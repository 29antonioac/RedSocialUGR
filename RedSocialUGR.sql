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
   NombreEstudiante VARCHAR(50) NOT NULL,
   Apellidos        VARCHAR(50) NOT NULL,
   FechaNacimiento  DATE        NOT NULL,
   FotoPersonal     VARCHAR(70) DEFAULT NULL,
   Destrezas        VARCHAR(50) DEFAULT NULL,
   Hobbies          VARCHAR(50) DEFAULT NULL,
   EstadoActual     VARCHAR(30) DEFAULT NULL,
   Ocupacion        VARCHAR(30) DEFAULT NULL,
   PRIMARY KEY  (correo)
 );

 CREATE TABLE carreras (
   Nombre         VARCHAR(30) NOT NULL,
   Centro         VARCHAR(30) NOT NULL,
   PRIMARY KEY  (nombre)
 );

 CREATE TABLE cursa (
   CorreoAlumno  VARCHAR(50) NOT NULL,
   NombreCarrera VARCHAR(50) NOT NULL,
   PRIMARY KEY    (CorreoAlumno, NombreCarrera),
   FOREIGN KEY    (CorreoAlumno)   REFERENCES estudiantes  (Correo) ON DELETE CASCADE,
   FOREIGN KEY    (NombreCarrera)  REFERENCES carreras     (Nombre) ON DELETE CASCADE
 );


 -- Creación de la tabla de asignaturas-centros


 -- Creación de la tabla actividades


 -- Creación de la tabla muros

 CREATE TABLE foro (
   IdentificadorForo  VARCHAR(50) NOT NULL,
   NombreForo         VARCHAR(50) NOT NULL,
   PRIMARY KEY  (IdentificadorForo)
 );

 CREATE TABLE tema (
   IdentificadorForo  VARCHAR(50) NOT NULL,
   IdentificadorTema  VARCHAR(50) NOT NULL,
   NombreTema         VARCHAR(50) NOT NULL,
   PRIMARY KEY  (IdentificadorForo, IdentificadorTema),
   FOREIGN KEY  (IdentificadorForo)   REFERENCES foro  (IdentificadorForo) ON DELETE CASCADE
 );

 CREATE TABLE post (
   IdentificadorForo  VARCHAR(50) NOT NULL,
   IdentificadorTema  VARCHAR(50) NOT NULL,
   IdentificadorPost  VARCHAR(50) NOT NULL,
   CotenidoPost       VARCHAR(200) NOT NULL,
   PRIMARY KEY    (IdentificadorForo, IdentificadorTema, IdentificadorPost),
   FOREIGN KEY    (IdentificadorForo, IdentificadorTema)   REFERENCES tema  (IdentificadorForo,IdentificadorTema) ON DELETE CASCADE

 );

 CREATE TABLE muro (
   IdentificadorMuro VARCHAR(50) NOT NULL,
   PRIMARY KEY  (IdentificadorMuro)
 );

 CREATE TABLE mensaje (
   IdentificadorMuro    VARCHAR(50) NOT NULL,
   IdentificadorMensaje VARCHAR(50) NOT NULL,
   CotenidoMensaje      VARCHAR(50) NOT NULL,
   PRIMARY KEY    (IdentificadorMuro, IdentificadorMensaje),
   FOREIGN KEY    (IdentificadorMuro)   REFERENCES muro  (IdentificadorMuro) ON DELETE CASCADE
 );

 CREATE TABLE crea (
   IdentificadorForo  VARCHAR(50) NOT NULL,
   IdentificadorTema  VARCHAR(50) NOT NULL,
   ContenidoMensaje   VARCHAR(200) NOT NULL,
   Correo             VARCHAR(50) NOT NULL,
   FechaCrea          DATE NOT NULL,
   PRIMARY KEY    (IdentificadorTema),
   FOREIGN KEY    (IdentificadorForo, IdentificadorTema)   REFERENCES tema  (IdentificadorForo,IdentificadorTema) ON DELETE CASCADE,
   FOREIGN KEY    (Correo)   REFERENCES estudiantes   (Correo) ON DELETE CASCADE
 );

  CREATE TABLE escribe1 (
    IdentificadorForo   VARCHAR(50) NOT NULL,
    IdentificadorTema   VARCHAR(50) NOT NULL,
    IdentificadorPost   VARCHAR(50) NOT NULL,
    Correo              VARCHAR(50) NOT NULL,
    FechaEscribe1       DATE NOT NULL,
    PRIMARY KEY     (IdentificadorForo, IdentificadorTema, IdentificadorPost),
    FOREIGN KEY     (IdentificadorForo, IdentificadorTema, IdentificadorPost)   REFERENCES post  (IdentificadorForo,IdentificadorTema, IdentificadorPost) ON DELETE CASCADE,
    FOREIGN KEY     (Correo)   REFERENCES estudiantes   (Correo) ON DELETE CASCADE
  );

  CREATE TABLE escribe2 (
    IdentificadorMuro     VARCHAR(50) NOT NULL,
    IdentificadorMensaje  VARCHAR(50) NOT NULL,
    Correo                VARCHAR(50) NOT NULL,
    FechaEscribe2         DATE NOT NULL,
    PRIMARY KEY     (IdentificadorMuro, IdentificadorMensaje),
    FOREIGN KEY     (IdentificadorMuro, IdentificadorMensaje)   REFERENCES mensaje  (IdentificadorMuro,IdentificadorMensaje) ON DELETE CASCADE,
    FOREIGN KEY     (Correo)   REFERENCES estudiantes   (Correo) ON DELETE CASCADE
  );

 -- Disparadores

 -- Eva
 -- SELECT max(IdentificadorForo) FROM foro
 -- Antonio

 -- Carlos

 -- Adrián

 -- NOTA: Lo suyo es echar esto a otros archivos y traerlos con "source <file>;"
 -- Inserción de tuplas en estudiantes

 INSERT INTO estudiantes (Correo,NombreEstudiante,Apellidos,FechaNacimiento) VALUES
 ('antonio@correo.ugr.es','Antonio','Álvarez Caballero',"1993-11-29"),
 ('evamaria@correo.ugr.es','Eva María','González García',"1992-09-01"),
 ('carlos@correo.ugr.es','Carlos','Parla Pérez',"1992-02-02"),
 ('adrian@correo.ugr.es','Adrián','Rho Rha',"1993-02-02");

 -- Inserción de tuplas en carreras

 -- nombre         VARCHAR(30) NOT NULL,
 -- centro         VARCHAR(30) NOT NULL,
 -- PRIMARY KEY(nombre)

 INSERT INTO carreras (Nombre, Centro) VALUES
 ('Doble Grado', 'ETSIIT/Ciencias');

 -- Inserción de tuplas en cursa
 -- correo_alumno  VARCHAR(50) NOT NULL,
 -- nombre_carrera VARCHAR(50) NOT NULL,

 INSERT INTO cursa (CorreoAlumno, NombreCarrera) VALUES
 ('antonio@correo.ugr.es','Doble Grado'),
 ('evamaria@correo.ugr.es','Doble Grado'),
 ('carlos@correo.ugr.es','Doble Grado'),
 ('adrian@correo.ugr.es','Doble Grado');
