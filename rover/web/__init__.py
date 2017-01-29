from flask import Flask
from flask_socketio import SocketIO

web = Flask(__name__)
web.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(web)

from rover.web import views
