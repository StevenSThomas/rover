#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Copyright (c) 2017 Steven S. Thomas <steventhomasnc@gmail.com>
#-------------------------------------------------------------------------------

# robot

from rover.robotController.motion import Motion
from rover.robotController.communication import Com
import json

class Robot:
    def __init__(self, broker):
        self.motion = Motion()
        self.com = Com(broker)
        self.com.subscribe(self.on_message)
        self.com.start()

    def on_message(self, userdata, msg):
        self.processPlan(msg.payload.decode())

    def processPlan(self,plan):
        planObject = json.loads(plan)
        steps = planObject["steps"]
        for step in steps:
            self.processCommand(step["command"])
            self.com.client.publish("step/done", step["id"])

    def processCommand(self,cmd):
        verb = cmd["verb"]
        speed = cmd["speed"]
        rotations = cmd["rotations"]
        if verb == "DRIVE":
            self.motion.drive(rotations,speed)
        elif verb == "TURN":
            self.motion.turn(rotations,speed)






if __name__ == "__main__":
    robot = Robot("pro.local")
