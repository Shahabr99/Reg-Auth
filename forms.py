from flask_wtf  import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField
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


class FeedbackForm(FlaskForm):

    topic = StringField('Topic:', validators=[InputRequired()])
    text = TextAreaField('Text:', validators=[InputRequired()], render_kw={'rows': 10, 'cols':50})
