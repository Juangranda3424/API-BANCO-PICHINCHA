import psycopg2

class Conn:

    conexion = None;

    @staticmethod
    def conectar():
        # Conexión a la base de datos
        conexion = psycopg2.connect(
            host="localhost",  # Cambia por tu host
            database="BancoPichincha",  # Nombre de tu base de datos
            user="root",  # Usuario de PostgreSQL
            password="root"  # Contraseña del usuario
        )
        return conexion

    