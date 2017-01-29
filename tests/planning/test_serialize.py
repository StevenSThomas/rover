import rover.planning.domain as m
import pytest
from unittest import mock,TestCase
import pickle

class SerializeTest(TestCase):

    def test_can_serialize_plan(self):
        plan = m.Plan()
        plan.appendDriveCommand(5,900)
        plan.appendDriveCommand(2,900)
        s = pickle.dumps(plan)
        print(s)
