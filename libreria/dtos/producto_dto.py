from models.producto_model import Producto
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Producto