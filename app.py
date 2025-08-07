# -*- coding: utf-8 -*-
# Importar configuración UTF-8 antes que nada
from src.config.utf8_config import configure_utf8
from flask_cors import CORS
configure_utf8()

from flask import Flask
from src.controller.UsuarioController import UsuarioController
from src.controller.PersonaController import PersonaController
from src.controller.DepositoController import DepositoController
from src.controller.TransferenciaController import TransferenciaController
from src.controller.MovimientoController import MovimientoController
from src.controller.RetiroController import RetiroController
from flasgger import Swagger

app = Flask(__name__)
CORS(app)

app.config['SWAGGER'] = {
    'title': 'API Banco Pichincha',
    'uiversion': 3
}
swagger = Swagger(app)


# Configurar Flask para manejar UTF-8 correctamente
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False


@app.route('/usuarios/<username>', methods=['GET'])
def getUserData(username):
    """
    Obtener información de usuario por username
    ---
    parameters:
      - name: username
        in: path
        type: string
        required: true
        description: Nombre de usuario
    responses:
      200:
        description: Información del usuario
        examples:
          application/json: 
            {
              "id": 1,
              "username": "jperez",
              "password": "jperez"
            }
    """
    print(username)
    return UsuarioController.getInfo_Usuario_Username(username)

@app.route('/cuenta-info/<numeroCuenta>', methods=['GET'])
def getInfoCuentaPersona(numeroCuenta):
    """
    Obtener información de cuenta por número
    ---
    parameters:
      - name: numeroCuenta
        in: path
        type: string
        required: true
        description: Número de cuenta bancaria
    responses:
      200:
        description: Información de la cuenta
        examples:
          application/json: 
            {
              "email": "juan.perez@gmail.com",
              "id": 1,
              "nombre": "Juan Pérez",
              "numeroCuenta": "78261375012306853615",
              "telefono": "0991234567",
              "tipoCuenta": "CORRIENTE"
            }
    """
    return PersonaController.getInfoPerson_NumCuenta(numeroCuenta)

@app.route('/movimientos-info/<numeroCuenta>', methods=['GET'])
def getMovimientoCuneta(numeroCuenta):
    """
    Obtener historial de movimientos de una cuenta
    ---
    parameters:
      - name: numeroCuenta
        in: path
        type: string
        required: true
        description: Número de cuenta bancaria
    responses:
      200:
        description: Lista de movimientos
        examples:
          application/json: 
            [
              {
                "descripcion": "Depósito en efectivo",
                "fecha": "Fri, 10 Jan 2025 00:00:00 GMT",
                "id": "48fb1502-4a05-47e7-994c-177d1eb6be13",
                "monto": "150.00",
                "ubicacion": "Sucursal Quito"
              }
            ]
    """
    return MovimientoController.getMovimientos_cuenta(numeroCuenta)

@app.route('/cantidad-cuentas/<id>', methods=['GET'])
def getCuentasPersona(id):
    """
    Obtener todas las cuentas de una persona
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la persona
    responses:
      200:
        description: Lista de cuentas de la persona
        examples:
          application/json: 
            [
              {
                "numeroCuenta": "78223131547506068536",
                "saldo": "1342.34",
                "tipoCuenta": "CORRIENTE"
              },
              {
                "numeroCuenta": "78261375062342341530",
                "saldo": "14.34",
                "tipoCuenta": "CORRIENTE"
              }
            ]
    """
    return PersonaController.getCuentas_persona(id)

@app.route('/persona-info/<id>', methods=['GET'])
def getPersonaInfo(id):
    """
    Obtener información de persona por ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la persona
    responses:
      200:
        description: Información de la persona
        examples:
          application/json: 
            {
              "id": 1,
              "nombre": "Juan Pérez",
              "email": "juan.perez@gmail.com",
              "telefono": "0991234567"
            }
    """
    return PersonaController.getInf_persona(id)

@app.route("/deposito", methods=['POST'])
def updateSaldoDepositoController():
    """
    Realizar depósito en cuenta
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            numeroCuentaOrigen:
              type: string
              example: "78261375012306853615"
            numeroCuentaDestino:
              type: string
              example: "78261375012306853615"
            monto:
              type: number
              example: 100.50
            motivo:
              type: string
              example: "Depósito de prueba"
            ubicacion:
              type: string
              example: "Quito"
            telefono:
              type: string
              example: "0991234567"
    responses:
      200:
        description: Depósito realizado exitosamente
        examples:
          application/json: {"success": True, "mensaje": "Depósito realizado"}
    """
    print("Actualizando Saldo por Depósito")
    return DepositoController.updateSaldo_Cuenta()

@app.route("/transferencia", methods=['POST'])
def updateSaldoTransferenciaController():
    """
    Realizar transferencia entre cuentas
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            numeroCuentaOrigen:
              type: string
              example: "78261375012306853615"
            numeroCuentaDestino:
              type: string
              example: "78261375012306853615"
            monto:
              type: number
              example: 50.00
            motivo:
              type: string
              example: "Pago de servicios"
            ubicacion:
              type: string
              example: "Quito"
            telefono:
              type: string
              example: "0991234567"
    responses:
      200:
        description: Transferencia realizada exitosamente
        examples:
          application/json: {"success": True, "mensaje": "Transferencia realizada"}
    """
    return TransferenciaController.updateSaldo_Cuenta()

@app.route("/retiro-sin-tarjeta", methods=['POST'])
def retiroSinTarjetas():
    """
    Solicitar retiro sin tarjeta (envía código por email)
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            numeroCuenta:
              type: string
              example: "78261375012306853615"
            montoRetirar:
              type: number
              example: 50.00
            email:
              type: string
              example: "usuario@email.com"
            nombre_persona:
              type: string
              example: "Juan Pérez"
    responses:
      200:
        description: Código de retiro enviado exitosamente
        examples:
          application/json: {"success": True, "mensaje": "Código enviado"}
    """
    return RetiroController.getRetiro_sin_tarjeta()

@app.route("/retirar-monto-sin-trajeta", methods=['POST'])
def retirarMontoSinTarjetas():
    """
    Confirmar retiro con código recibido por email
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            codigo:
              type: string
              example: "123456"
    responses:
      200:
        description: Retiro realizado exitosamente
        examples:
          application/json: {"success": True, "mensaje": "Retiro realizado"}
    """
    return RetiroController.retirarMonto_sin_tarjeta()

if __name__ == '__main__':
    app.run(debug=True)
