from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api

from db import connection


load_dotenv() 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

flask_api = Api(app=app)


connection.init_app(app)


Migrate(app=app, db=connection)

if __name__ == '__main__':
    app.run(debug=True)