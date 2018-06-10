from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired(), validators.Length(min=4)]) 
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=4)])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired(), validators.Length(min=1)])
    username = StringField("Username", [validators.DataRequired(), validators.Length(min=4)]) 
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=4)])
    
    class Meta:
        csrf = False
