from rover.domain.models import MotorInstruction

class RobotForwardUseCase:

    def __init__(self, driver):
        self.driver = driver

    def execute(self,robot):
        # logic for driving forward
        # { MotorPort, Degrees to Rotate, Speed }
        instructions = [
            MotorInstruction(robot.leftMotor.port,360,90),
            MotorInstruction(robot.rightMotor.port,360,90)
        ]

        self.driver.drive(instructions)
