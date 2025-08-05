from src.repository.DepositoRepository import DepositoRepository
from src.repository.RetiroRepository import RetiroRepository

class DepositoService:
    def updateSaldoCuenta(numeroCuentaOrigen, numeroCuentaDestino, monto):
        if monto > 10000:
            return False
        
        saldo_cuenta_destino = DepositoRepository.saldo_persona(numeroCuentaDestino)
        resultado_destino = float(saldo_cuenta_destino[0]) + monto
        actualizar_saldo_destino = DepositoRepository.actualizacion_saldo_persona(str(resultado_destino),numeroCuentaDestino)

        return actualizar_saldo_destino


        
