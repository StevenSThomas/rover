from rover.domain import models as m

def test_robot_model_init():
    name = "Number5"
    leftMotor = m.Motor("A")
    rightMotor = m.Motor("B")
    robot = m.Robot(name, leftMotor, rightMotor)
    assert robot.name == name
