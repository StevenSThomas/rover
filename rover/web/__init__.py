from flask import Flask
from flask_socketio import SocketIO

web = Flask(__name__)
web.config['SECRET_KEY'] = 'secret!'
from rover.web import views
