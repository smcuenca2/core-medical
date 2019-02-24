# core-medical
this project will allow get a analysis medical of a patient across to the use of the semantic web.
# Install
1. Para construir los contenedores se ejecuta el comando docker-compose -up
2. Ingresar al contenedor de la base de datos ejecutar docker exec -i -t core-medical-db bash
3. Para ingresar a la base de datos mysql ejecutar mysql -u root -proot
4. Seleccionar base de datos con el comando sql 'use mysql;'
5. Actualizar clave de usuario root con el siguiente comando ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY 'root'; 
6. Salir del contenedor de la base de datos y ubicarse en la raíz del proyecto
7. Parar los contenedores con el comando docker-compose stop
8. Importar la base de datos umls en el contenedor de base de datos del proyecto con el siguiente comando
docker exec -i core-medical-db mysql -uroot -proot umls < umls_20181020.sql
9. Volver a levantar los contenedores con el comando docer-compose up -d
