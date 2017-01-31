"""Robot."""
from time import sleep,gmtime, strftime
from rover.ev3.motion import Motion
from rover.ev3.com import Com
import json



class Kernel:
    def __init__(self, motion, com):
        self._state = "ready"
        self.pendingCommands = []

        # setup sub-systems
        self.motion = motion
        self.com = com
        self.com.subscribe(self.on_new_plan)

        self.main_loop()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,value):
        self._state = value

    def main_loop(self):
        while not self.state == "shut_down":
            if self.state == "executing_command":
                # executing until motion system is no longer busy
                if not self.motion.is_busy:
                    self.state = "pending_command"

            if self.state == "pending_command":
                # get next command , if no more commands then "ready"
                if self.pendingCommands:
                    cmd = self.pendingCommands.pop()
                    self.state = "executing_command"
                    self._execute_command(cmd)
                else:
                    self.state = "ready"

            heartbeat_data = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            heartbeat_data = heartbeat_data + ":" + self.state
            print(heartbeat_data)
            self.com.heartbeat(heartbeat_data)

            self.com.send_receive()
            sleep(1)


    def on_new_plan(self, userdata, msg):
        """executes when a new plan is received."""
        payload = msg.payload.decode()
        plan = json.loads(payload)
        commands = plan["commands"]
        if(commands):
            self._load_plan(plan)

    def _load_plan(self, plan):
        self.state = "loading_plan"
        self.pendingCommands = []
        for step in plan["commands"]:
            cmd = Command(step["verb"],step["rotations"],step["speed"])
            self.pendingCommands.append(cmd)
        self.state = "pending_command"


    def _execute_command(self,cmd):
        # load commands and process in nonblocking?
        if cmd.verb == "DRIVE":
            self.motion.drive(cmd.rotations, cmd.speed)
        elif cmd.verb == "TURN":
            self.motion.turn(cmd.rotations, cmd.speed)

class Command:
    def __init__(self, verb, rotations, speed):
        self.verb = verb
        self.rotations = rotations
        self.speed = speed

if __name__ == "__main__":
    com = Com("192.168.2.1")
    motion = Motion()
    rover = Kernel(motion,com)
