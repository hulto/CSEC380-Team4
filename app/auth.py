# auth.py

from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user
from .webserver import functiondb, initdb as db


auth = Blueprint('auth', __name__, template_folder='webserver/templates')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return 'Logout'


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

    user = db.User.query.filter_by(uname=username).first()

    if not functiondb.check_password(username, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
