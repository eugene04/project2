import os
import requests

from flask import Flask,jsonify, render_template , Request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/" ,methods = ['GET','POST'])
def index():
    return render_template('index.html')

@socketio.on('send message')
def msg(chat):
    emit('new message',{'chat': chat}, broadcast=True)





if __name__ == '__main__':
    socketio.run(app, debug=True)