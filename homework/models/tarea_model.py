from sqlalchemy import Column, types
from bd import connection
from enum import Enum
from sqlalchemy.sql.schema import ForeignKey
class EstadoTareaEnum(str, Enum):
    PENDIENTE: str = "PENDIENTE"
    REALIZANDOSE: str = "REALIZANDOSE"
    REALIZADA: str = "REALIZADA"
    CANCELADA: str = "CANCELADA"

class Tarea(connection.Model):
    id = Column(type_ = types.Integer, primary_key = True, autoincrement = True)
    nombre = Column(type_ = types.Text, nullable = False)
    description = Column(type_ = types.Text, default = "No description")
    fechaVencimiento = Column(type_ = types.DateTime, name = "fecha_vencimiento")
    estado = Column(type_ = types.Enum(EstadoTareaEnum), default = EstadoTareaEnum.PENDIENTE)

    usuarioId = Column(ForeignKey(column="usuarios.id"), type_ = types.Integer, nullable = False, name="usuario_id")

    __tablename__ = "tareas"