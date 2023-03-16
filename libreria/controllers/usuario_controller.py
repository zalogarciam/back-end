from bcrypt import gensalt, hashpw
from flask_restful import Resource, request
from dtos.usuario_dto import UsuarioDto
from db import connection
from models.usuario_model import Usuario

class RegistroController(Resource):
    def post(self):
        data = request.json
        try:
            dto = UsuarioDto()
            data_serialized = dto.load(data)

            salt = gensalt()
            password = bytes(data_serialized.get('password'), 'utf-8')
            hashed_password = hashpw(password, salt).decode('utf-8')
        
            data_serialized['password'] = hashed_password
            user = Usuario(**data_serialized)
            connection.session.add(user)
            connection.session.commit()
            return {
                'message': 'Usuario creado',
            }

        except Exception as error:
            return {
                'message': 'Error al registrar usuario',
                'content': error.args
            }
        