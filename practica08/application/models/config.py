import web
'''
Parametros para conectarse a una BD MySQL o MariaDB
'''
DB = web.database(
    dbn='mysql', #motor de BD
    host='localhost', #ruta del server
    db='ria_iniciales', #Nombre de la BD
    user='ria', #usuario
    pw='ria.2019', #contrasenia
    port=3306 #puerto de mariadb
)