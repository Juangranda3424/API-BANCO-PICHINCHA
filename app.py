# -*- coding: utf-8 -*-
# Importar configuración UTF-8 antes que nada
from src.config.utf8_config import configure_utf8
configure_utf8()

from flask import Flask
from src.controller.UsuarioController import UsuarioController
from src.controller.PersonaController import PersonaController
from src.controller.DepositoController import DepositoController
from src.controller.TransferenciaController import TransferenciaController
from src.controller.MovimientoController import MovimientoController
from src.controller.RetiroController import RetiroController

app = Flask(__name__)

# Configurar Flask para manejar UTF-8 correctamente
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False

# Configurar todas las respuestas con UTF-8
@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

# Devuelve solo un objeto
# [
#   {
#     'id': 1,
#     'username': 'jperez',
#     'password': 'jperez'
#   }
# ]
@app.route('/usuarios/<username>', methods=['GET'])
def getUserData(username):
    print(username)
    return UsuarioController.getInfo_Usuario_Username(username)

#Devuelve solo un objeto 
# [
#     {
#         "email": "juan.perez@gmail.com",
#         "id": 1,
#         "nombre": "Juan Pérez",
#         "numeroCuenta": "78261375012306853615",
#         "telefono": "0991234567",
#         "tipoCuenta": "CORRIENTE"
#     }
# ]

@app.route('/cuenta-info/<numeroCuenta>', methods=['GET'])
def getInfoCuentaPersona(numeroCuenta):
    return PersonaController.getInfoPerson_NumCuenta(numeroCuenta)

#Devuelve lista 
# [
#     {
#         "descripcion": "Depósito en efectivo",
#         "fecha": "Fri, 10 Jan 2025 00:00:00 GMT",
#         "id": "48fb1502-4a05-47e7-994c-177d1eb6be13",
#         "monto": "150.00",
#         "ubicacion": "Sucursal Quito"
#     },

# ]

@app.route('/movimientos-info/<numeroCuenta>', methods=['GET'])
def getMovimientoCuneta(numeroCuenta):
    return MovimientoController.getMovimientos_cuenta(numeroCuenta)

#Devuelve lista 
# [
#     {
#         "numeroCuenta": "78223131547506068536",
#         "saldo": "1342.34",
#         "tipoCuenta": "CORRIENTE"
#     },
#     {
#         "numeroCuenta": "78261375062342341530",
#         "saldo": "14.34",
#         "tipoCuenta": "CORRIENTE"
#     },
#     {
#         "numeroCuenta": "78261375060685361530",
#         "saldo": "1482.34",
#         "tipoCuenta": "CORRIENTE"
#     },
#     {
#         "numeroCuenta": "78261375012306853615",
#         "saldo": "100",
#         "tipoCuenta": "CORRIENTE"
#     }
# ]

@app.route('/cantidad-cuentas/<id>', methods=['GET'])
def getCuentasPersona(id):
    return PersonaController.getCuentas_persona(id)


# Datos que deben enviar en el body
#     numeroCuentaOrigen = string
#     numeroCuentaDestino = string
#     monto = float
#     motivo = string
#     ubicacion = string
#     telefono = string

@app.route("/deposito", methods=['POST'])
def updateSaldoDepositoController():
    return DepositoController.updateSaldo_Cuenta()


# Datos que deben enviar en el body
#     numeroCuentaOrigen = string
#     numeroCuentaDestino = string
#     monto = float
#     motivo = string
#     ubicacion = string
#     telefono = string

@app.route("/transferencia", methods=['POST'])
def updateSaldoTransferenciaController():
    return TransferenciaController.updateSaldo_Cuenta()

# Datos que deben enviar en el body
#     numeroCuenta = string
#     montoRetirar = float
#     email = string - email de la persona aquien se le va enviar el codigo
#     nombre_persona = string de la persona aquien se le va enviar el codigo

@app.route("/retiro-sin-tarjeta", methods=['POST'])
def retiroSinTarjetas():
    return RetiroController.getRetiro_sin_tarjeta()


if __name__ == '__main__':
    app.run(debug=True)
