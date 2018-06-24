from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PenForm(FlaskForm):

    name = StringField("Model", [validators.DataRequired(), validators.Length(min=1), validators.Length(max=50)])
    manufacturer = StringField("Manufacturer", [validators.DataRequired(), validators.length(min=2), validators.Length(max=50)])
    country = StringField("Country of Origin", [validators.DataRequired(), validators.length(min=2), validators.Length(max=50)])
 
    class Meta:
        csrf = False
   
