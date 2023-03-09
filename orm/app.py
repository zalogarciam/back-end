from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api

from bd import conn
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController, UnNivelController
from controllers.maestro_controller import MaestroController

load_dotenv() 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

flask_api = Api(app=app)


conn.init_app(app)


Migrate(app=app, db=conn)

# defino las rutas de mi API
flask_api.add_resource(NivelController, '/nivel')
flask_api.add_resource(UnNivelController, '/nivel/<id>')
flask_api.add_resource(MaestroController, '/maestro/')

if __name__ == '__main__':
    app.run(debug=True)