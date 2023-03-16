from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import Schema, fields
from models.usuario_model import Usuario

class UsuarioDto(SQLAlchemyAutoSchema):
    password = auto_field(load_only = True)
    class Meta:
        model = Usuario

class LoginDto(Schema):
    correo = fields.Email(required = True, error_message = {'required': 'El correo es requerido'})
    password = fields.Str(required =True, error_messages={'required': 'El password es requerido'})