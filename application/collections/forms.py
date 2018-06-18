from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.validators import InputRequired

class CollectionForm(FlaskForm):
    
    pen = SelectField('Pen', coerce=int, validators=[InputRequired()])
    nib = StringField("Nib", [validators.DataRequired(), validators.length(min=1)])
    color = StringField("Color", [validators.DataRequired(), validators.length(min=2)])

    class Meta:
        csrf = False
