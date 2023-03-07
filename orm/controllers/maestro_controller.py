from flask_restful import Resource, request
from sqlalchemy.orm import Query
from bd import conn
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto

class MaestroController(Resource):
    def get(self):
        query: Query = conn.session.query(Maestro)
        resultado = query.all()
        dto = MaestroDto()
        maestros = dto.dump(resultado, many = True)
        return {
            'content': maestros
        }

    def post(self):
        data = request.json
        try:
            dto = MaestroDto()
            validated_data = dto.load(data)
            maestro = Maestro(nombre = data.get('nombre'), 
                            apellidos = data.get('apellidos'), 
                            correo = data.get('correo'), 
                            direccion = data.get('direccion'))
            conn.session.add(maestro)
            conn.session.commit()
            return {
            'message': 'Maestro created successfully'
        }
        except Exception as error:
            return {
            'message': 'Error',
            'content': error.args
        }
