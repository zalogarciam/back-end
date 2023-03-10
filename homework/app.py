from flask import Flask
from flask_migrate import Migrate
from bd import connection
from dotenv import load_dotenv
from os import environ
from controllers.usuario_controller import UsuariosController
from flask_restful import Api

load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
api = Api(app)

connection.init_app(app)

Migrate(app = app, db = connection)

api.add_resource(UsuariosController, '/registro')

if __name__ == '__main__':
    app.run(debug=True)