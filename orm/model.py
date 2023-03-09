from bd import conn
from sqlalchemy import Column, types

class Level(conn.Model):
    id = Column(type = types.Integer, primary_key=True, autoincrement=True)
    number = Column(type = types.Integer, nullable=False, unique=True)
    description = Column(type = types.Text)
    __tablename__ = 'niveles'