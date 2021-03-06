#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Copyright (c) 2017 Steven S. Thomas <steventhomasnc@gmail.com>
#-------------------------------------------------------------------------------

# Motion represents the motor sub-system for the rover.
# This code runs on the EV3 brick

import ev3dev.ev3 as ev3
from time import sleep

class Motion:
    def __init__(self):
        self.motors = [ev3.LargeMotor(address) for address in ('outA','outB')]
        self.leftMotor = self.motors[0]
        self.rightMotor = self.motors[1]

    @property
    def is_busy(self):
        return any(m.state for m in self.motors)

    def acknowledge_command(self):
        ev3.Sound.speak("thank you, command sequence received").wait()

    def mission_complete(self):
        ev3.Sound.speak("Mission Complete!").wait()

    def drive(self,rotations,speed):
        self._rotate_motor(self.leftMotor,rotations,speed)
        self._rotate_motor(self.rightMotor,rotations,speed)


    def reverse(self,rotations,speed):
        drive(-rotations,speed)

    def turn(self,rotations,speed):
        self._rotate_motor(self.leftMotor, rotations, speed)
        self._rotate_motor(self.rightMotor, -rotations, speed)

    def turn_left(self,roations,speed):
        self.turn(-rotations,speed)

    def turn_right(self,rotations,speed):
        self.turn(rotations,speed)

    def _rotate_motor(self, motor, rotations, speed):
        rotationDegrees = self._convert_rotation_to_degrees(rotations)
        motor.run_to_rel_pos(position_sp = rotationDegrees, speed_sp=speed)

    def _convert_rotation_to_degrees(self, rotations):
        return rotations * 360


