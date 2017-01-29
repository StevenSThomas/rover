from rover.web import web
from flask_socketio import SocketIO
from rover.planning import services
from rover.web import plannerController

socketio = SocketIO(web)
plannerController =  plannerController.PlannerController(socketio)
socketio.run(web)
