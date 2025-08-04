from flask import jsonify
from src.services.UsuarioService import UsuarioService

class UsuarioController:

  @staticmethod
  def getInfo_Usuario_Username(username):
    try:
      resultado = UsuarioService.getInfo_Usuario_Username(username)
      return jsonify(resultado)
    except Exception as e:
      print(f"Error en MovimientoController: {e}")
      return jsonify({"error": "Error al obtener información del usuario"}), 500