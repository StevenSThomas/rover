from rover.web import web
from flask_socketio import SocketIO
from rover.planning import services

class PlannerController:

    def __init__(self,socketio):
        self.socketio = socketio
        self.socketio.on_event('message',self.handle_message)
        self.planner = services.Planner()

    def handle_message(self,message):
        self.planner.clearPlan()
        self.planner.addDriveStep(5,900)
        self.planner.sendPlan()
        
