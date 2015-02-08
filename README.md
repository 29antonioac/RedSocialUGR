# RedSocialUGR
Práctica de Diseño y Desarrollo de Sistemas de Información del Doble Grado en Ingeniería Informática y Matemáticas de la UGR

Nuestro proyecto es una red social.

La base de datos está hecha en **MariaDB** aunque es posible que vaya sin problemeas en otras implementaciones.

El cliente está hecho en Python 3.

Para importar la base de datos a tu sistema MariaDB hay que ejecutar
      mysql -t -p < RedSocialUGR.sql
y después meter la contraseña (si la hay).

El cliente se ejecuta
      python cliente.py

Se conectará a la base de datos creada, aunque hay que cambiar el usuario (está puesto como **antonio**) y la contraseña (está puesta como ejemplo **archlinux**).      
