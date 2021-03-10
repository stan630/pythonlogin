from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login_post():
    username=request.form.get('username')
    password= request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again')
        return redirect(url_for('main.profile'))
    login_user(user,remember=remember)
    return redirect(url_for('main.profile'))

@auth.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user:
        flash('Username already exists')
        return redirect(url_for('auth.register'))
    
    # create a new user with the form data
    new_user = User(email=email, username=username,
    password=generate_password_hash(password,
    method= 'sha256'))

    ## add the new user to database
    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))