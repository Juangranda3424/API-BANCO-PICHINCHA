from src.db.Conn import Conn
from datetime import date

class MovimientoRepository:
    
    def insertar_movimiento_sin_tarjeta_deposito(numeroCuentaOrigen, numeroCuentaDestino, monto, motivo, ubicacion, numeroCelular,tipo):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()

                id = MovimientoRepository._getId_numero_cuenta(numeroCuentaOrigen)

                # Obtener el ID del movimiento insertado usando RETURNING
                pgcursor.execute("insert into movimientos (id_cuenta,m_monto,m_fecha,m_contajgeta,m_descripcion,m_estado,m_ubicacion) values (%s,%s,%s,%s,%s,%s,%s) RETURNING id_movimiento",(id[0],str(monto),date.today(),False,f'Deposito {motivo}','COMPLETADO',ubicacion))
                
                # Obtener el ID generado
                id_movimiento = pgcursor.fetchone()[0]
                
                conexion.commit()  # Confirmar la transacción
                
                # ORDEN IMPORTANTE: Primero insertar en movimientosintarjeta, luego en deposito
                if tipo == True:
                    MovimientoRepository._insert_movimiento_sin_tarjeta(id_movimiento,monto,numeroCelular,'Transferencia')
                    MovimientoRepository._insert_movimiento_transferencia(id_movimiento,numeroCuentaOrigen,numeroCuentaDestino)

                elif tipo == False:
                    MovimientoRepository._insert_movimiento_sin_tarjeta(id_movimiento,monto,numeroCelular,'Deposito')
                    MovimientoRepository._insert_movimiento_deposito(id_movimiento,numeroCuentaOrigen,numeroCuentaDestino)
                else:
                    MovimientoRepository._insert_movimiento_sin_tarjeta(id_movimiento,monto,numeroCelular,'Retiro sin tarjeta')
                return id_movimiento
        except Exception as e:
            print(f"Error: {e}")
            return None     
    
    
    def _getId_numero_cuenta(numeroCuentaOrigen):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("select id_cuenta from cuenta where numero_cuenta = %s;", (numeroCuentaOrigen,))
                return pgcursor.fetchone()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def _insert_movimiento_sin_tarjeta(id,monto,numeroCelular,tipo):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                # Corregir: 4 valores necesitan 4 placeholders
                pgcursor.execute("insert into movimientosintarjeta values (%s,%s,%s,%s);", (id,monto,tipo,numeroCelular))
                conexion.commit()
                #print("Movimiento sin tarjeta insertado")
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def _insert_movimiento_deposito(id,numeroCuentaOrigen,numeroCuentaDestino):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("insert into deposito values (%s,%s,%s);", (id,numeroCuentaOrigen,numeroCuentaDestino))
                conexion.commit()
                #print("Depósito insertado")
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    @staticmethod
    def _insert_movimiento_transferencia(id,numeroCuentaOrigen,numeroCuentaDestino):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("insert into transferencia values (%s,%s,%s,'Banco Pichincha');", (id,numeroCuentaOrigen,numeroCuentaDestino))
                conexion.commit()
                #print("Depósito insertado")
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def _insert_movimiento_retiro(id,codigo):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("insert into retirosintarjeta values (%s,%s,%s);", (id,codigo,1))
                conexion.commit()
                #print("Depósito insertado")
        except Exception as e:
            print(f"Error: {e}")
            return None

    def getMovimientos_cuenta(numeroCuenta):
        try:
            with Conn.conectar() as conexion:  # Se cierra automáticamente
                pgcursor = conexion.cursor()
                pgcursor.execute("select m.id_movimiento, m.m_monto, m.m_fecha, m.m_descripcion, m.m_ubicacion from movimientos m join cuenta c on c.id_cuenta = m.id_cuenta where c.numero_cuenta = %s;", (numeroCuenta,))
            return pgcursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")
            return None




              
