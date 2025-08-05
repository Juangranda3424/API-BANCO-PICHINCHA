# -*- coding: utf-8 -*-
import psycopg2

class Conn:

    conexion = None

    @staticmethod
    def conectar():
        # Conexión a la base de datos con UTF-8
        conexion = psycopg2.connect(
            host="localhost",  # Cambia por tu host
            database="bancoPichincha",  # Nombre de tu base de datos
            user="root",  # Usuario de PostgreSQL
            password="root",  # Contraseña del usuario
            client_encoding='utf8'  # Configurar encoding UTF-8
        )
        return conexion

    
