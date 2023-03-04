from flask_restful import Resource, request
from sqlalchemy.orm import Query
from bd import conn
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    # GET, POST, PUT 
    def get(self):
        query: Query = conn.session.query(Nivel)
        # SELECT * FROM niveles;
        resultado = query.all()
        print(resultado[0].numero)
        print(resultado[0].descripcion)

        dto = NivelDto()
        niveles = dto.dump(resultado, many = True)

        # niveles = []
        # for nivel in resultado:
        #     niveles.append({
        #         'id': nivel.id,
        #         'numero': nivel.numero,
        #         'descripcion': nivel.descripcion
        #     })
        return {
            'content': niveles
        }

    def post(self):
        data = request.json
        nivel = Nivel(numero = data.get('numero'), descripcion = data.get('descripcion'))
        conn.session.add(nivel)
        conn.session.commit()

        return {
            'message': 'Nivel created successfully'
        }
                                                                          