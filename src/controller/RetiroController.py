from src.services.RetiroService import RetiroService
from src.repository.MovimientoRepository import MovimientoRepository
from flask import request, jsonify

class RetiroController:

    def getRetiro_sin_tarjeta():
        datos = request.get_json()  # Obtener datos del POST
        numeroCuenta = datos.get('numeroCuenta')
        montoRetirar = datos.get('montoRetirar')
        email = datos.get('email')
        nombre_persona = datos.get('nombre_persona')
        ubicacion = datos.get('ubicacion')
        tel = datos.get('telefono')


        resultado = RetiroService.retiro_sin_tarjeta(numeroCuenta,montoRetirar)

        if resultado:
            id_valor = MovimientoRepository.insertar_movimiento_sin_tarjeta_deposito(numeroCuenta,numeroCuenta,montoRetirar,'Retiro sin tarjeta',ubicacion,tel,None)
            codigo = RetiroService._enviar_codigo_acceso(email,nombre_persona)
            MovimientoRepository._insert_movimiento_retiro(id_valor,codigo)
            return jsonify({"mensaje": "Codigo generado correctamente"}), 200
        else:
            return jsonify({"mensaje": "Error al generar el codigo"}), 500




