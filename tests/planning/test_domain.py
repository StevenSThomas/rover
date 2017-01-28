import rover.planning.domain as m
import pytest
from unittest import mock,TestCase

class DomainTests(TestCase):

    def test_can_create_command(self):
        cmd = m.DriveCommand(1,900)
        self.assertEqual(cmd.verb,"DRIVE")
        self.assertEqual(cmd.rotations,1)
        self.assertEqual(cmd.speed,900)

    def test_can_create_step(self):
        cmd = m.DriveCommand(1,900)
        step = m.Step(cmd)
        self.assertIsNotNone(step.id)

    def test_step_status_starts_at_todo(self):
        cmd = m.DriveCommand(1,900)
        step = m.Step(cmd)

        self.assertEqual(step.status,m.Step.TO_DO)

    def test_can_create_plan(self):
        cmd = m.DriveCommand(1,900)
        step = m.Step(cmd)

        plan = m.Plan()
        self.assertIsNotNone(plan)

    def test_plan_status_starts_at_todo(self):
        cmd = m.DriveCommand(1,900)
        step = m.Step(cmd)

        plan = m.Plan()
        self.assertEqual(plan.status,m.Plan.TO_DO)

    def test_can_append_drive_command(self):
        plan = m.Plan()
        plan.appendDriveCommand(1,900)
