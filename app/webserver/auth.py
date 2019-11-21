# auth.py

from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, login_manager, logout_user, current_user
from webserver import functiondb as db


auth = Blueprint('auth', 'auth', template_folder='webserver/templates')


@auth.route('/login')
def login():
    print("Current user")
    print(current_user)
    if(current_user.is_authenticated):
        return redirect('/')
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    #user = db.session.query(User).filter_by(uname=username).first()
    user = None
    user = db.check_password(username, password)
    if not user:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('profile'))
