from flask import Flask
from flask_migrate import Migrate
from bd import connection

app = Flask(__name__)
connection.init_app(app)

Migrate(app = app, db = connection)

if __name__ == '__main__':
    app.run(debug=True)