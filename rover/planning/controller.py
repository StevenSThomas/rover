"""Planning Services."""
import json
import rover.planning.domain as m
from rover.com import com


class Planner:
    """Implement Planner functionaility."""

    def __init__(self):
        """Create a new planner service."""
        self.currentPlan = m.Plan()
        self.robot_status = m.RobotStatus()
        self.com = com.Com()
        self.com.subscribe("robot/status", self.on_robot_status)


    def addDriveStep(self, rotations, speed):
        self.currentPlan.appendDriveCommand(rotations, speed)

    def addTurnStep(self, rotations, speed):
        self.currentPlan.appendTurnCommand(rotations, speed)

    def clearPlan(self):
        self.currentPlan = m.Plan()

    def sendPlan(self):
        payload = json.dumps(self.currentPlan,
                             default = lambda o: o.__dict__,
                             separators = (',', ':'))
        self.com.publish("robot/newplan", payload)

    def on_robot_status(self, payload):
        self.robot_status.value = payload
