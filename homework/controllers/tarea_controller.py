from flask_restful import Resource, request, reqparse
from dtos.tarea_dto import TareaDto
from models.tarea_model import Tarea
from bd import connection
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
class TareasController(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.json
        dto = TareaDto()
        print(data)
        try:
            data_validated = dto.load(data)
            tarea = Tarea(**data_validated, usuarioId = user_id)
            connection.session.add(tarea)
            connection.session.commit()
            return {
                'message': 'Added successfully'
            }, 201
        except Exception as error:
            return {
                'message': 'Error to create tarea',
                'content': error.args
            }

class UsuarioTareaController(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.json
        dto = TareaDto()
        print(data)
        try:
            data_validated = dto.load(data)
            tarea = Tarea(**data_validated, usuarioId = user_id)
            connection.session.add(tarea)
            connection.session.commit()
            return {
                'message': 'Added successfully'
            }, 201
        except Exception as error:
            return {
                'message': 'Error to create tarea',
                'content': error.args
            }
    @jwt_required()
    def get(self):
        # usuario_id = get_jwt_identity()
        usuario_id = get_jwt_identity()
        print(usuario_id)

        query: Tarea = connection.session.query(Tarea)
        tareas = query.filter_by(usuarioId = usuario_id).all()
        print(tareas)
        if len(tareas) == 0:
            return {
                'message': "Found 0 tareas for this user"
            }    
        dto = TareaDto()
        result = dto.dump(tareas, many = True)
        return {
                'content': result
        }

class TareaController(Resource):
    @jwt_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type =str)
        parser.add_argument('description', type =str)
        parser.add_argument('fecha_vencimiento', type =str)
        parser.add_argument('estado', type =str)
        args = parser.parse_args()
        query: Tarea = connection.session.query(Tarea)

        tareas = query.all()
        print(tareas)
        if args['nombre'] is not  None:
          tareas = query.filter_by(nombre = args['nombre']).all()
        elif args['description'] is not  None:
          tareas = query.filter_by(nombre = args['description']).all()
        elif args['fecha_vencimiento'] is not  None:
          tareas = query.filter_by(nombre = args['fecha_vencimiento']).all()
        elif args['estado'] is not  None:
          tareas = query.filter_by(nombre = args['estado']).all()

        dto = TareaDto()
        result = dto.dump(tareas, many = True)

        return {
                'content': result
        }
