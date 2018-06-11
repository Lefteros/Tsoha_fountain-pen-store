from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.validators import InputRequired
from application.pens.models import Pen

class CollectionForm(FlaskForm):
    
    pens = Pen.query.all()
    list = []
    i = 0
    for pen in pens:
        list.insert(i, pen.name)
        i= i+1

    pen = SelectField('Pen', coerce=int, validators=[InputRequired()])
    nib = StringField("Nib", [validators.DataRequired(), validators.length(min=1)])
    color = StringField("Color", [validators.DataRequired(), validators.length(min=2)])

    class Meta:
        csrf = False
