from bd import conn
from sqlalchemy import Column, types

class Nivel(conn.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    numero = Column(type_=types.Integer, nullable=False, unique=True)
    descripcion = Column(type_=types.Text)

    __tablename__ = 'niveles'