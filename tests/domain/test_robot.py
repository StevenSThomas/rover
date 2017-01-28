from rover.domain import models as m

def test_robot_model_init():
    name = "testy"
    robot = m.Robot(name)
    assert robot.name == name
