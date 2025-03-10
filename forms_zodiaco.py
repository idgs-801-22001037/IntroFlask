from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class zodiacoForm(FlaskForm):
    nombre = StringField('nombre', [
        DataRequired('El nombre es requerido'),
        Length(min=3, message='El minimo es 3 caracteres')
    ])
    apellido = StringField('apellido', [
        DataRequired('El apellido es requerido'),
        Length(min=3, message='El minimo es 3 caracteres')
    ])
    apellidoM = StringField('apellidoM',[
        DataRequired('El apellido materno es requerido'),
        Length(min=3,message='El minimo es de 3 caracteres')
    ])
    anio = IntegerField('anio',[
        DataRequired('El anio es requerido'),
        NumberRange(min=1, message='El numero no puede ser menor a uno')
    ])
    mes = IntegerField('mes', [
        DataRequired('El mes es requerido'),
        NumberRange(min=1, message='El numero no puede ser menor a uno')
    ])
    dia = IntegerField('dia', [
        DataRequired('El dia es requerido'),
        NumberRange(min=1, message='El numero no puede ser menor a uno')
    ])
