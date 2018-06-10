from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class PenForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    manufacturer = StringField("Manufacturer", [validators.length(min=2)])
    country = StringField("Country", [validators.length(min=2)])
 
    class Meta:
        csrf = False
