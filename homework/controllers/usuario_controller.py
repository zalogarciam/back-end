from flask_restful import Resource, request
from dtos.usuario_dto import UsuarioDto
from homework.models.usuario_model import Usuario
from bcrypt import hashpw, gensalt

class UsuariosController(Resource):
    def post(self):
        data = request.json
        dto = UsuarioDto()
        try:
            data_valid = dto.load(data)
            salt = gensalt(rounds = 10)
            password = bytes(data_valid.get("password"), "utf-8")
            password_hashed = hashpw(password, salt)
            password_hashed_str = password_hashed.decode("utf-8")

            usuario = Usuario(correo = data_valid.get('correo'),
                              password = password_hashed_str,
                              nombre = data_valid.get('nombre'),
                              apellido = data_valid.get('apellido')
                              )

        except Exception as error:
            return {
                'message': 'Error al ingresar el usuario',
                'content': error.args
            }