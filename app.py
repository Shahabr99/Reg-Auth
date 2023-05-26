from flask import Flask, render_template, redirect, session, flash
from models import db, User, connect_db, Feedback
from forms import SignupForm, LoginForm, FeedbackForm
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WHATever'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug = True

with app.app_context():
    connect_db(app)
    db.create_all()



@app.route('/')
def go_home():
    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def show_form():
    """user creates an account via loaded form"""
    form = SignupForm()
    if form.validate_on_submit():
        try:
            firstname = form.firstname.data
            lastname = form.lastname.data
            email = form.email.data
            username = form.username.data
            password = form.password.data
            session['username'] = username

            hashed_pwd = User.register(username, password)

            new_user = User(username=username, password=hashed_pwd, email=email,  firstname=firstname, lastname=lastname)
        
        
            db.session.add(new_user)
            db.session.commit()
            flash("signing up successful!", "success")
            return redirect(f'/users/{username}')
        except IntegrityError:
            db.session.rollback()
            return redirect('/register')

    return render_template('signup.html', form=form)


@app.route('/users/<username>', methods=["GET", "POST"])
def show_user(username):
    if 'username' not in session:
        return redirect('/')
    
    form = FeedbackForm()

    # if form.validate_on_submit():   
    topic = form.topic.data
    text = form.text.data
    curr_user = User.query.filter_by(username=username).first()
    feedbacks = Feedback.query.all()
    return render_template('user.html', user=curr_user, feedbacks=feedbacks)
    



@app.route('/login', methods=["GET", "POST"])
def show_login():
    """renders the login form"""
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        

        user = User.authenticate(username, password)
        if user:
            flash(f"Welcome back {{user.name}}!", 'success')
            session['username'] == user.username
            return redirect(f'/users/{user.username}')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/register')


@app.route('/users/<username>/delete')
def delete_user(username):
    """deleting user and their feedbacks from database/session"""

    user = User.query.get_or_404(username)
    
    feedbacks = Feedback.query.filter_by(username=username).all()
      
        
    for feedback in feedbacks:
        db.session.delete(feedback)
    db.session.commit()


    session.pop('username')
    db.session.commit()

    return redirect('/')