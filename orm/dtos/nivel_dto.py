from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.nivel_model import Nivel

class NivelDto(SQLAlchemyAutoSchema): 
    class Meta:
       model = Nivel 