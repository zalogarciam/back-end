from flask_restful import Resource, request
from werkzeug.utils import secure_filename
from os import path

class CategoriasController(Resource):
    def post(self):

        print(request.form)
        print(request.files)

        imagen = request.files.get('imagen')
        secure_name = secure_filename(imagen.filename)
        imagen.save(path.join('images', secure_name))
        return {
            'message': 'Categoria creada'
        }