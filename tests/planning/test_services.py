import rover.planning.domain as m
import rover.planning.services as s
import pytest
from unittest import mock,TestCase

class ServiceTest(TestCase):

    def test_can_create_planner(self):
        planner = s.Planner()
        self.assertIsNotNone(planner.currentPlan)

    def test_can_send_plan(self):
        planner = s.Planner()
        planner.currentPlan.appendDriveCommand(5,900)
        planner.currentPlan.appendTurnCommand(-3,900)
        planner.currentPlan.appendDriveCommand(5,900)
        planner.currentPlan.appendTurnCommand(-3,900)
        planner.currentPlan.appendDriveCommand(5,900)
        planner.currentPlan.appendTurnCommand(-3,900)
        planner.sendPlan()
