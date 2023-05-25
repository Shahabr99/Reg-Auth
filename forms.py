from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import Email, InputRequired, Length

class SignupForm(FlaskForm):

    firstname = StringField('First name:', validators=[InputRequired()])
    lastname = StringField('Last name:', validators=[InputRequired()])
    email = EmailField('Email:')
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])

class LoginForm(FlaskForm):

    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])
