from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ
from bd import conn

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')


conn.init_app(app);
# conn = SQLAlchemy(app = app)

if __name__ == '__main__':
    app.run(debug=True)