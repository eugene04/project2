from flask import jsonify, render_template , Request , flash, redirect, url_for
from application import app , socketio
from application.models import User , Post
from application.forms import RegistrationForm , LoginForm
from flask_socketio import  emit


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

