
class Robot:

    def __init__(self, name, leftMotor, rightMotor):
        self._name = name
        self._leftMotor = leftMotor
        self._rightMotor = rightMotor

    @property
    def name(self):
        return self._name

    @property
    def leftMotor(self):
        return self._leftMotor

    @property
    def rightMotor(self):
        return self._rightMotor

    def rotate_left_motor(self,rotations,speed):
        return MotorInstruction(self.name, self._leftMotor.port, rotations * 360, speed)

    def rotate_right_motor(self, rotations, speed):
        return MotorInstruction(self.name, self._rightMotor.port, rotations * 360, speed)

class Motor:

    def __init__(self, port):
        self._port = port

    @property
    def port(self):
        return 'out' + self._port

class MotorInstruction:

    def __init__(self, robot_name, port, rotation, speed):
        self._robot_name = robot_name
        self._port = port
        self._rotation = rotation
        self._speed = speed

    def __eq__(self, other):
        return ((self._robot_name, self._port, self._rotation,self._speed) ==
                (other._robot_name, other._port, other._rotation, other._speed))

    def __repr__(self):
        return self._port + ":" + str(self._rotation)

    @property
    def robot_name(self):
        return self._robot_name

    @property
    def port(self):
        return self._port

    @property
    def rotation(self):
        return self._rotation

    @property
    def speed(self):
        return self._speed
