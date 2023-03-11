from flask import Flask
from flask_migrate import Migrate
from bd import connection
from dotenv import load_dotenv
from os import environ
from controllers.usuario_controller import LoginController, UsuariosController
from flask_restful import Api
from flask_jwt_extended import JWTManager
load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = 'secret'
api = Api(app)

connection.init_app(app)

Migrate(app = app, db = connection)
JWTManager(app)

api.add_resource(UsuariosController, '/registro')
api.add_resource(LoginController, '/login')

if __name__ == '__main__':
    app.run(debug=True)