from src.repository.MovimientoRepository import MovimientoRepository


class MovimientoService:
    @staticmethod
    def getMovimientos_cuenta(numeroCuenta):
        info_movimientos = MovimientoRepository.getMovimientos_cuenta(numeroCuenta)
        print(str(info_movimientos))

        resultado = []
        for movimiento in info_movimientos:
            infoTypeJSON = {
                'id': movimiento[0],
                'monto': movimiento[1],
                'fecha': movimiento[2],
                'descripcion': movimiento[3],
                'ubicacion': movimiento[4]
            }
            resultado.append(infoTypeJSON)
        
        return resultado  


