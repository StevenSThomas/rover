"""Robot."""
import time
from rover.ev3.motion import Motion
from rover.ev3.com import Com
import json

class Kernel:
    def __init__(self, broker):
        self.motion = Motion()
        self.com = Com(broker)
        self.com.subscribe(self.on_message)

        while True:
            self.com.client.loop()
            print(self.motion.leftMotor.duty_cycle)
            time.sleep(1)


    def on_message(self, userdata, msg):
        payload = msg.payload.decode()
        plan = json.loads(payload)
        self.processPlan(plan)

    def processPlan(self,plan):
        self.motion.acknowledge_command()
        for step in plan["commands"]:
            self.com.publish("step/done", step["id"] )
            self.com.client.loop()
            self.processCommand(step)
        self.motion.mission_complete()

    def processCommand(self,cmd):
        # load commands and process in nonblocking?
        if cmd["verb"] == "DRIVE":
            self.motion.drive(cmd["rotations"], cmd["speed"])
        elif cmd["verb"] == "TURN":
            self.motion.turn(cmd["rotations"], cmd["speed"])

if __name__ == "__main__":
    rover = Kernel("192.168.2.1")
