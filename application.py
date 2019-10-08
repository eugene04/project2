import os
import requests

from flask import Flask,jsonify, render_template , Request , flash, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from forms import RegistrationForm , LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '760e32cf0f533875d24f777e3e70fa9f'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"






@app.route("/" ,methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/register" ,methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'congratulations {form.username.data} your account has been successfully created', 'success')
        return redirect (url_for('index'))
    
    return render_template('register.html',title = 'register',form=form)
    

@app.route("/login" ,methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ejemwa04@gmail.com' and form.password.data == 'ej123':
            flash('you are logged in!','success')
            return redirect (url_for('index'))
        else:
            flash('login unsuccesfull please check email address and password','danger')
    return render_template('login.html',title = 'login',form=form)

@socketio.on('send message')
def my_msg(chat , methods=['GET', 'POST']):
    #chat = data["chat"]
    emit('new message',chat, broadcast=True)





if __name__ == '__main__':
    socketio.run(app, debug=True)