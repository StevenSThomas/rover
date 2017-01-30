"""Robot."""
import time
from rover.robotController.motion import Motion
from rover.robotController.com import Com
import json

class Robot:
    def __init__(self, broker):
        self.motion = Motion()
        self.com = Com(broker)
        self.com.subscribe(self.on_message)
        self.com.start()
        while True:
            time.sleep(1)


    def on_message(self, userdata, msg):
        self.processPlan(msg.payload.decode())

    def processPlan(self,splan):
        plan = json.loads(splan)
        for step in plan["steps"]:
            self.com.publish("step/done", step["id"] )
            self.com.client.loop()
            self.processCommand(step["command"])

    def processCommand(self,cmd):
        # load commands and process in nonblocking?
        if cmd["verb"] == "DRIVE":
            self.motion.drive(cmd["rotations"], cmd["speed"])
        elif cmd["verb"] == "TURN":
            self.motion.turn(cmd["rotations"], cmd["speed"])


if __name__ == "__main__":
    robot = Robot("pro.local")
