"""Starts up the CommandController for handling socketIO requests."""
from rover.web import web
from flask_socketio import SocketIO
from rover.web.controller import CommandController

socketio = SocketIO(web)
plannerController = CommandController(socketio)
socketio.run(web)
