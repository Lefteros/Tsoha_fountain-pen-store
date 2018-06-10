from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class PenForm(FlaskForm):
    name = StringField("Model", [validators.DataRequired(), validators.Length(min=2)])
    manufacturer = StringField("Manufacturer", [validators.DataRequired(), validators.length(min=2)])
    country = StringField("Country of Origin", [validators.DataRequired(), validators.length(min=2)])
 
    class Meta:
        csrf = False


