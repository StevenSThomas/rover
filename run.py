from rover.web import web
from flask_socketio import SocketIO

socketio = SocketIO(web)
socketio.run(web)
