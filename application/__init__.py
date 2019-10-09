import os
import requests

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO



app = Flask(__name__)
app.config["SECRET_KEY"] = '760e32cf0f533875d24f777e3e70fa9f'
socketio = SocketIO(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from application import routes