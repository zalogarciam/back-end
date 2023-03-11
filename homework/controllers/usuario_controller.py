from flask_restful import Resource, request
from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario
from bcrypt import hashpw, gensalt
from bd import connection

class UsuariosController(Resource):
    def post(self):
        data = request.json
        dto = UsuarioDto()
        try:
            data_valid = dto.load(data)
            print(data)
            salt = gensalt(rounds = 10)
            password = bytes(data_valid.get("password"), "utf-8")
            password_hashed = hashpw(password, salt)
            password_hashed_str = password_hashed.decode("utf-8")

            usuario = Usuario(correo = data_valid.get('correo'),
                              password = password_hashed_str,
                              nombres = data_valid.get('nombres'),
                              apellido = data_valid.get('apellido')
                              )
            connection.session.add(usuario)
            connection.session.commit()
            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al ingresar el usuario',
                'content': error.args
            }