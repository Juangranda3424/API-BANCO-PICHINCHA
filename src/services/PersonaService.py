# -*- coding: utf-8 -*-
from src.repository.PersonaRepository import PersonaRepository

class PersonaService:
    def getInfo_Persona_Cuenta(numeroCuenta):
        info_persona = PersonaRepository.info_persona_cuenta(numeroCuenta)
        resultado = []
        infoTypeJSON = {
            'id': info_persona[0],
            'telefono': info_persona[1],
            'email': info_persona[2],
            'nombre': info_persona[3],
            'tipoCuenta': info_persona[4],
            'numeroCuenta': info_persona[5]
        }
        resultado.append(infoTypeJSON)
        return resultado  
    
    def getNumero_Cuentas(id):
        cuentas = PersonaRepository.info_cuentas_persona(id)
        resultado = []
        for cuenta in cuentas:
            infoTypeJSON = {
                'accountNumber': cuenta[0],
                'accountType': cuenta[1],
                'balance': cuenta[2]
            }
            resultado.append(infoTypeJSON)
        return resultado  
    
    def getInfo_Persona(id):
        info_persona =  PersonaRepository.info_persona(id)
        resultado = []
        infoTypeJSON = {
            'id': info_persona[0],
            'direccion': info_persona[1],
            'telefono': info_persona[2],
            'email': info_persona[3],
            'tipoPersona': info_persona[4],
            'nombrePersona': info_persona[5]
        }
        
        resultado.append(infoTypeJSON)
        return resultado

     
