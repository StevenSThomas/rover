from rover.domain.models import MotorInstruction

class RobotForwardUseCase:

    def __init__(self, driver):
        self.driver = driver

    def execute(self,robot):
        instructions = [
            robot.rotate_left_motor(1,90),
            robot.rotate_right_motor(1,90)
        ]
        self.driver.drive(instructions)

class RobotTurnLeftUseCase:

    def __init__(self, driver):
        self.driver = driver

    def execute(self,robot):
        instructions = [
            robot.rotate_left_motor(-1,90),
            robot.rotate_right_motor(1,90)
        ]
        self.driver.drive(instructions)

class RobotTurnRightUseCase:

    def __init__(self, driver):
        self.driver = driver

    def execute(self,robot):
        instructions = [
            robot.rotate_left_motor(1,90),
            robot.rotate_right_motor(-1,90)
        ]
        self.driver.drive(instructions)

class RobotReverseUseCase:

    def __init__(self, driver):
        self.driver = driver

    def execute(self,robot):
        instructions = [
            robot.rotate_left_motor(-1,90),
            robot.rotate_right_motor(-1,90)
        ]
        self.driver.drive(instructions)
