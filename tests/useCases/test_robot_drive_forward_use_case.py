import pytest
from unittest import mock,TestCase
from rover.domain import models as m
from rover.use_cases import robot_drive_use_cases as uc

class RobotDriveTestCases(TestCase):
    def setUp(self):
        self.robot = m.Robot("Number5",m.Motor('A'),m.Motor('B'))

    def tearDown(self):
        self.robot = None

    def test_robot_drive_forward(self):
        driver = mock.Mock()
        driver.drive.return_value = None
        robot_forward = uc.RobotForwardUseCase(driver)
        robot_forward.execute(self.robot)

        driver.drive.assert_called_with(
          [ m.MotorInstruction("Number5","outA", 360 , 90),
            m.MotorInstruction("Number5","outB", 360 , 90) ]
        )

    def test_robot_drive_left(self):
            driver = mock.Mock()
            driver.drive.return_value = None
            robot_forward = uc.RobotTurnLeftUseCase(driver)
            robot_forward.execute(self.robot)

            driver.drive.assert_called_with(
              [ m.MotorInstruction("Number5","outA", -360 , 90),
                m.MotorInstruction("Number5","outB", 360 , 90) ]
            )

    def test_robot_drive_right(self):
            driver = mock.Mock()
            driver.drive.return_value = None
            robot_forward = uc.RobotTurnRightUseCase(driver)
            robot_forward.execute(self.robot)

            driver.drive.assert_called_with(
              [ m.MotorInstruction("Number5","outA", 360 , 90),
                m.MotorInstruction("Number5","outB", -360 , 90) ]
            )

    def test_robot_reverse(self):
            driver = mock.Mock()
            driver.drive.return_value = None
            robot_forward = uc.RobotReverseUseCase(driver)
            robot_forward.execute(self.robot)

            driver.drive.assert_called_with(
              [ m.MotorInstruction("Number5","outA", -360 , 90),
                m.MotorInstruction("Number5","outB", -360 , 90) ]
            )
