import pytest
from unittest import mock
from rover.domain import models as m
from rover.use_cases import robot_drive_use_cases as uc

def test_robot_drive_forward():
    driver = mock.Mock()
    driver.drive.return_value = None
    robot_forward = uc.RobotForwardUseCase(driver)

    leftMotor = m.Motor('A')
    rightMotor = m.Motor('B')
    robot = m.Robot("Number5", leftMotor, rightMotor)

    robot_forward.execute(robot)

    driver.drive.assert_called_with(
      [ m.MotorInstruction("outA", 360 , 90),
        m.MotorInstruction("outB", 360 , 90) ]
    )
