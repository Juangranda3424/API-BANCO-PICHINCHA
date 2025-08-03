from src.db.Conn import Conn

class RetiroRepository:

    @staticmethod
    def _saldo_actual(numeroCuenta):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                print("select c.saldo_cuenta from cuenta c where c.numero_cuenta = %s;", (numeroCuenta,))
                pgcursor.execute("select c.saldo_cuenta from cuenta c where c.numero_cuenta = %s;", (numeroCuenta,))
                return pgcursor.fetchone()
                
        except Exception as e:
            print(f"Error: {e}")
            return 0
        




