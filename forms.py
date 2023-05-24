from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import Email, InputRequired

class SignupForm(FlaskForm):

    firstname = StringField('First name:', validators=[InputRequired()])
    lastname = StringField('Last name:', validators=[InputRequired()])
    email = EmailField('Email:', validators=[InputRequired(), Email()])
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])