from flask_restful import Resource, request
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
    def get(self):
        pass

class TareaController(Resource):
    def get(self, id):
        query: Tarea = connection.session.query(Tarea)
        tareas = query.filter_by(usuarioId = id).all()
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