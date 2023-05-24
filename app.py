from flask import Flask, render_template, redirect, session, flash
from models import db, User, connect_db
from forms import SignupForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WHATever'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug = True
connect_db(app)



@app.route('/')
def go_home():
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def show_form():
    """user creates an account via loaded form"""
    form = SignupForm()
    if form.validate_on_submit():

        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        hashed_pwd = User.register(username, password)

        new_user = User(firstname=firstname, lastname=lastname, email=email, username=username, password=hashed_pwd)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect('/secret')

    return render_template('signup.html', form=form)


@app.route('/secret')
def show_secret():
    return render_template('secret.html')