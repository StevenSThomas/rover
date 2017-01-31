import pytest
from unittest import mock,TestCase
from rover.ev3.kernel import Kernel

class TestKernel(TestCase):

    def test_kernel_starts_in_ready_state(self):
        motion = mock.Mock()
        com = mock.Mock()
        rover = Kernel(motion,com)
        rover.state = "shutdown"
        self.assertEqual(rover.state,"ready")
