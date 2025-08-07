from src.db.Conn import Conn
from datetime import datetime
class RetiroRepository:

    @staticmethod
    def _saldo_actual(numeroCuenta):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("select c.saldo_cuenta from cuenta c where c.numero_cuenta = %s;", (numeroCuenta,))
                return pgcursor.fetchone()
                
        except Exception as e:
            print(f"Error: {e}")
            return 0

    @staticmethod
    def _retirar_monto(codigo):
        try:
            with Conn.conectar() as conexion:
                pgcursor = conexion.cursor()
                fecha_actual = datetime.now()
                pgcursor.execute("SELECT id_movimiento, rst_codigogenerado, rst_fechahora FROM retirosintarjeta WHERE rst_codigogenerado = '%s' AND abs(extract(epoch from (rst_fechahora - %s::timestamp))) <= 300;", (codigo,fecha_actual))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def _getCuenta_monto_max(id):
        try:
            with Conn.conectar() as conexion:
                pgcursor = conexion.cursor()
                pgcursor.execute("SELECT m.mst_montomaximo, c.numero_cuenta FROM movimientosintarjeta m JOIN movimientos mo ON m.id_movimiento = mo.id_movimiento JOIN cuenta c ON mo.id_cuenta = c.id_cuenta WHERE m.id_movimiento = %s;", (id,))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def _validateNumMaxRetiro(codigo):
        try:
            with Conn.conectar() as conexion:
                pgcursor = conexion.cursor()
                pgcursor.execute("SELECT rst_nummaxretiros FROM retirosintarjeta WHERE rst_codigogenerado = '%s';",(codigo,))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def _updateNumMaxRetiro(numero,codigo):
        try:
            with Conn.conectar() as conexion:
                pgcursor = conexion.cursor()
                pgcursor.execute("UPDATE retirosintarjeta SET rst_nummaxretiros = %s WHERE rst_codigogenerado = '%s';",(numero-1,codigo))
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    

    
        




