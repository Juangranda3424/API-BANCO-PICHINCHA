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
    
    def getNumero_Cuentas(numeroCuenta):
        cuentas = PersonaRepository.info_cuentas_persona(numeroCuenta)
        resultado = []
        for cuenta in cuentas:
            infoTypeJSON = {
                'numeroCuenta': cuenta[0],
                'tipoCuenta': cuenta[1],
                'saldo': cuenta[2]
            }
            resultado.append(infoTypeJSON)
        return resultado  
     
