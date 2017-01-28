import uuid
from enum import Enum



class Plan:
    TO_DO = "todo"

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.status =  self.TO_DO
        self.steps = []

    def appendCommand(self,cmd):
        step = Step(cmd)
        self.steps.append(step)

    def appendDriveCommand(self,rotations,speed):
        cmd = DriveCommand(rotations,speed)
        self.appendCommand(cmd)

    def appendTurnCommand(self,rotations,speed):
        cmd = TurnCommand(rotations,speed)
        self.appendCommand(cmd)


class Step:
    TO_DO = "todo"

    def __init__(self,command):
        self.id = str(uuid.uuid4())
        self.command = command
        self.status = self.TO_DO

class DriveCommand:

    def __init__(self,rotations,speed):
        self.verb = "DRIVE"
        self.rotations = rotations
        self.speed = speed


    def verb(self):
        return self.verb


    def rotations(self):
        return self.rotations


    def speed(self):
        return self.speed

class TurnCommand:

    def __init__(self,rotations,speed):
        self.verb = "TURN"
        self.rotations = rotations
        self.speed = speed


    def verb(self):
        return self.verb


    def rotations(self):
        return self.rotations


    def speed(self):
        return self.speed
