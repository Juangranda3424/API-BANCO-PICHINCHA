from src.services.TransferenciaService import TransferenciaService
from src.repository.MovimientoRepository import MovimientoRepository
from flask import request, jsonify

class TransferenciaController:
    @staticmethod
    def updateSaldo_Cuenta():
        try:
            datos = request.get_json()  # Obtener datos del POST
            numeroCuentaOrigen = datos.get('numeroCuentaOrigen')
            numeroCuentaDestino = datos.get('numeroCuentaDestino')
            monto = datos.get('monto')
            motivo = datos.get('motivo')
            ubicacion = datos.get('ubicacion')
            tel = datos.get('telefono')
            
            if not numeroCuentaOrigen or not monto:
                return jsonify({"error": "Faltan datos requeridos"}), 400
            
            resultado = TransferenciaService.updateSaldoCuenta(numeroCuentaOrigen,numeroCuentaDestino, monto)
            
            if resultado:
                MovimientoRepository.insertar_movimiento_sin_tarjeta_deposito(numeroCuentaOrigen,numeroCuentaDestino,monto,motivo,ubicacion,tel,True)
                return jsonify({"mensaje": "Se realizo la transferencia correctamente"}), 200
            else:
                return jsonify({"error": "Error en la transferencia del cliente"}), 500
        except Exception as e:
            return jsonify({"error": "Error en el servidor"}), 500



