import json
from json import JSONEncoder
import rover.planning.domain as m
import rover.messaging.bus as bus


class Planner:

    def __init__(self):
        self.currentPlan = m.Plan()
        self.bus = bus.Bus("pro.local")

    def sendPlan(self):
        payload = json.dumps(self.currentPlan, default=lambda o: o.__dict__,
                             separators=(',',':'))
        self.bus.publish("robot/newplan",payload)
