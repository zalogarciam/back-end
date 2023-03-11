from flask_restful import Resource, request
from dtos.usuario_dto import LoginDto, UsuarioDto
from models.usuario_model import Usuario
from flask_jwt_extended import create_access_token
from sqlalchemy.orm import Query
from bcrypt import checkpw, hashpw, gensalt
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
        
class LoginController(Resource):
    def post(self):
        data = request.json
        dto = LoginDto()
        try:
            data_validated = dto.load(data)
            query: Query = connection.session.query(Usuario)
            user_found: Usuario | None = query.filter_by(correo = data_validated.get('correo')).first()
            if not user_found:
                return {
                    'message': 'User does not exist'
                }
            
            hashed_password = bytes(user_found.password, 'utf-8')
            password = bytes(data_validated.get('password'), 'utf-8')
            result = checkpw(password, hashed_password)
            if result:
                token = create_access_token(identity = user_found.id)
                return {
                    'message': token
                }
            else:
                return{
                    'message': "Access denied"
                }

        except Exception as error:
            return {
                'message': 'Error al loguear',
                'content': error.args
            }