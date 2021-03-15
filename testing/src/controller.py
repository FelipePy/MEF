from unittest import TestCase
from program.src.controller import Controller

class TestController(TestCase):
    def test_do_transition_correct(self):
        controller = Controller()
        self.assertEqual(controller.do_transition(3), 0)

    def test_do_transition_error(self):
        controller = Controller()
        self.assertFalse(controller.do_transition(3), 1)
