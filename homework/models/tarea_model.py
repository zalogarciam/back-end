from sqlalchemy import Column, types
from bd import connection
from enum import Enum
from sqlalchemy.sql.schema import ForeignKey
class EstadoTareaEnum(Enum):
    PENDIENTE = "PENDIENTE"
    REALIZANDOSE = "REALIZANDOSE"
    REALIZADA = "REALIZADA"
    CANCELADA = "CANCELADA"

class Tarea(connection.Model):
    id = Column(type_ = types.Integer, primary_key = True, autoincrement = True)
    nombre = Column(type_ = types.Text, nullable = False)
    nombre = Column(type_ = types.Text, default = "No description")
    fechaVencimiento = Column(type_ = types.DateTime, name = "fecha_vencimiento")
    estado = Column(type_ = types.Enum(EstadoTareaEnum), default = EstadoTareaEnum.PENDIENTE)

    usuarioId = Column(ForeignKey(column="usuarios.id"), type = types.Integer, nullable = False)

    __tablename__ = "tareas"