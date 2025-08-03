from flask import jsonify
from src.services.MovimientoService import MovimientoService

class MovimientoController:

    @staticmethod
    def getMovimientos_cuenta(numeroCuenta):
        try:
            resultado = MovimientoService.getMovimientos_cuenta(numeroCuenta)
            return jsonify(resultado)
        except Exception as e:
            print(f"Error en MovimientoController: {e}")
            return jsonify({"error": "Error al obtener información de movimientos"}), 500