# -*- coding: utf-8 -*-
from src.db.Conn import Conn

class PersonaRepository:

    def info_persona_cuenta(numeroCuenta):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("select p.id_persona, p.telefono_persona, p.email_persona, p.nombre_persona, c.tipo_cuenta, c.numero_cuenta from persona p join cuenta c on c.id_persona = p.id_persona where c.numero_cuenta = %s;", (numeroCuenta,))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def info_cuentas_persona(id):
        try:
            with Conn.conectar() as conexion:  
                pgcursor = conexion.cursor()
                pgcursor.execute("select c.numero_cuenta, c.tipo_cuenta, c.saldo_cuenta from persona p join cuenta c on c.id_persona = p.id_persona where p.id_persona = %s;", (id,))
                return pgcursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return None


    def info_persona(id):
        try:
            with Conn.conectar() as conexion:  
                pgcursor = conexion.cursor()
                pgcursor.execute("select * from persona where p.id_persona = %s;", (id,))
                return pgcursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return None
