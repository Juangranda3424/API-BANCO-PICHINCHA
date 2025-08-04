from src.repository.UsuarioRepository import UsuarioRepository

class UsuarioService:
  def getInfo_Usuario_Username(username):
    data = UsuarioRepository._user_data_by_username(username)
    res = []
    infoTypeJSON = {
      'id': data[0],
      'username': data[1],
      'password': data[2]
    }
    res.append(infoTypeJSON)

    return res 