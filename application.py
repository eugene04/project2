import os
import requests

from flask import Flask,jsonify, render_template , Request , flash, redirect, url_for
from flask_socketio import SocketIO, emit
from forms import RegistrationForm , LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '760e32cf0f533875d24f777e3e70fa9f'
socketio = SocketIO(app)



@app.route("/" ,methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/register" ,methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'congratulations {form.username.data} your account has been successfully created', 'success')
        return redirect (url_for('index')
    
    return render_template('register.html',title = 'register',form=form)
    

@app.route("/login" ,methods = ['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html',title = 'login',form=form)

@socketio.on('send message')
def my_msg(chat , methods=['GET', 'POST']):
    #chat = data["chat"]
    emit('new message',chat, broadcast=True)





if __name__ == '__main__':
    socketio.run(app, debug=True)