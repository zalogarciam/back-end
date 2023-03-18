from os import path
from flask_restful import Resource, request
from db import connection
from dtos.producto_dto import ProductoDto
from models.producto_model import Producto

class ProductoController(Resource):
    def post(self):
        data = request.form
        imagen = request.files.get('imagen')
        data['imagen'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serialized = dto.load(data)
            prod = Producto(**data_serialized)

            connection.session.add(prod)
            imagen.save(path.join('images', data['imagen']))
            connection.session.commit()
            return {
                'message': 'Producto creado'
            }
        except Exception as error:
            connection.session.rollback()
            return {
                'message': 'Error al crear producto',
                'content': error.args
            }