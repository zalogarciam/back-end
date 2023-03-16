from bd import connection
from sqlalchemy import Column, types

class Usuario(connection.Model):
    id = Column(type_ = types.Integer, autoincrement = True, primary_key = True)
    correo = Column(type_ =types.Text, unique = True, nullable = False)
    password = Column(type_ = types.Text, nullable = False)
    nombres = Column(type_ = types.Text, nullable = False)
    apellido = Column(type_ = types.Text, nullable = False)

    __tablename__ = 'usuarios'