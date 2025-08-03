from src.db.Conn import Conn


class DepositoRepository:

    def saldo_persona(numeroCuenta):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("select c.saldo_cuenta from cuenta c where c.numero_cuenta = %s;", (numeroCuenta,))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def actualizacion_saldo_persona(monto, numeroCuenta):
        try:
            with Conn.conectar() as conexion: 
                pgcursor = conexion.cursor()
                pgcursor.execute("update cuenta set saldo_cuenta = %s where numero_cuenta = %s;", (monto,numeroCuenta))
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False    
    

