from flask_socketio import SocketIO
from rover.planning.api import PlannerAPI
import json

class CommandController:

    def __init__(self,socketio):
        self.socket = socketio

        self.socket.on_event('transmit_command_sequence', self.transmit_command_sequence)
        self.planner = PlannerAPI()
        self.planner.robot_status.attach(self.on_robot_status_change)

    def on_robot_status_change(self, new_status):
        self.socket.emit('robot_status_change', {'data': new_status.value})

    def transmit_command_sequence(self, command_sequence):
        payload = json.dumps(command_sequence)
        self.planner.sendPlan(payload)
