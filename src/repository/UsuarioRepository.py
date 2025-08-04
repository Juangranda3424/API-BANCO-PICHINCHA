from src.db.Conn import Conn

class UsuarioRepository:

  @staticmethod
  def _user_data_by_username(username):
    try:
      with Conn.conectar() as conexion:  # Se cierra automáticamente
        # print("select u.username, u.password from usuarios u where u.username = %s;", (username,))
        pgcursor = conexion.cursor()
        pgcursor.execute("select u.id_usuario, u.username_usuario, u.password_usuario from usuarios u where u.username_usuario = %s;", (username,))

        return pgcursor.fetchone()

    except Exception as e:
      print(f"Error: {e}")
      return 0
