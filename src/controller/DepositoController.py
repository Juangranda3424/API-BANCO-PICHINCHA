# -*- coding: utf-8 -*-
from src.services.DepositoService import DepositoService
from src.repository.MovimientoRepository import MovimientoRepository
from flask import request, jsonify

class DepositoController:
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
            
            resultado = DepositoService.updateSaldoCuenta(numeroCuentaOrigen,numeroCuentaDestino, monto)
            
            if resultado:
                MovimientoRepository.insertar_movimiento_sin_tarjeta_deposito(numeroCuentaOrigen,numeroCuentaDestino,monto,motivo,ubicacion,tel,False)
                return jsonify({"mensaje": "Se depositó correctamente"}), 200
            else:
                return jsonify({"error": "Error en el depósito del cliente"}), 500
        except Exception as e:
            return jsonify({"error": "Error en el servidor"}), 500



