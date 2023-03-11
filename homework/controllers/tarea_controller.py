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

    def get(self):
        pass