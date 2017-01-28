import ev3dev.ev3 as ev3

class Motion()
    def __init__(self):
        self.leftMotor = ev3.LargeMotor('outA')
        self.rightMotor = ev3.LargeMotor('outB')

    def forward(self):
        self.leftMotor.run_to_rel_pos(position_sp=360, speed_sp=700)
        self.rightMotor.run_to_rel_pos(position_sp=360, speed_sp=700)

    def reverse(self):
        self.leftMotor.run_to_rel_pos(position_sp=-360, speed_sp=700)
        self.rightMotor.run_to_rel_pos(position_sp=-360, speed_sp=700)

    def right(self):
        self.leftMotor.run_to_rel_pos(position_sp=360, speed_sp=700)

    def left(self):
        self.rightMotor.run_to_rel_pos(position_sp=360, speed_sp=700)
