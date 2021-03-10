from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost/login'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db.init_app(app)

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        results = db.session.execute
        ("SELECT * FROM accounts WHERE username = %s AND password = %s", (username, password))
    return render_template('index.html',msg='')