from rover.web import web
from flask_socketio import SocketIO
from rover.planning import controller

class PlannerController:

    def __init__(self,socketio):
        self.socket = socketio
        self.socket.on_event('message', self.handle_message)
        self.planner = controller.Planner()
        self.planner.robot_status.attach(self.on_robot_status_change)


    def handle_message(self,message):
        self.planner.clearPlan()
        self.planner.addTurnStep(1, 300)
        self.planner.sendPlan()

    def on_robot_status_change(self, new_status):
        self.socket.emit('robot_status_change', {'data': new_status.value})
