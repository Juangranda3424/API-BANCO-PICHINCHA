# -*- coding: utf-8 -*-
from flask import jsonify
from src.services.PersonaService import PersonaService

class PersonaController:

    def getInfoPerson_NumCuenta(numeroCuenta):
        try:
            print("Hola")
            resultado = PersonaService.getInfo_Persona_Cuenta(numeroCuenta)
            return jsonify(resultado)
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Error al obtener información del cliente"}), 500

    def getCuentas_persona(id):
        try:
            resultado = PersonaService.getNumero_Cuentas(id)
            return jsonify(resultado)
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": "Error al obtener información del cliente"}), 500

