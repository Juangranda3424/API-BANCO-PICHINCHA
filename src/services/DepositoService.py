from src.repository.DepositoRepository import DepositoRepository
from src.repository.RetiroRepository import RetiroRepository

class DepositoService:
    def updateSaldoCuenta(numeroCuentaOrigen, numeroCuentaDestino, monto):
        if monto > 10000:
            return False
        
        if float(RetiroRepository._saldo_actual(numeroCuentaOrigen)[0]) < float(monto):
            return False
        else:        
            saldo_cuenta_destino = DepositoRepository.saldo_persona(numeroCuentaDestino)
            resultado_destino = float(saldo_cuenta_destino[0]) + monto;
            actualizar_saldo_destino = DepositoRepository.actualizacion_saldo_persona(str(resultado_destino),numeroCuentaDestino)
            
            saldo_cuenta_origen = DepositoRepository.saldo_persona(numeroCuentaOrigen)
            resultado_origen = float(saldo_cuenta_origen[0]) - monto;
            DepositoRepository.actualizacion_saldo_persona(str(resultado_origen),numeroCuentaOrigen)

            return actualizar_saldo_destino


        
