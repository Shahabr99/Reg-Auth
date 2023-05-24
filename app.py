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
    return render_template('signup.html', form=form)