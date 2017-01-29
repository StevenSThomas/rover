import json
import rover.planning.domain as m
import rover.messaging.bus as bus


class Planner:

    def __init__(self):
        self.currentPlan = m.Plan()
        self.bus = bus.Bus("pro.local")

    def addDriveStep(self, rotations, speed):
        self.currentPlan.appendDriveCommand(rotations, speed)

    def addTurnStep(self, rotations, speed):
        self.currentPlan.appendTurnCommand(rotations, speed)

    def clearPlan(self):
        self.currentPlan = m.Plan()

    def sendPlan(self):
        payload = json.dumps(self.currentPlan, default= lambda o: o.__dict__,separators=(',', ':'))
        self.bus.publish("robot/newplan",payload)
