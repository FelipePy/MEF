from unittest import TestCase
from program.src.controller import Controller
from program.src.state import State

class TestController(TestCase):

    def test_do_transition_1(self):
        """
        Quando usado o método do_transition inserindo os valores
        Transição -> 2
        Estado -> 1
        deve-se retornar o Estado -> 3

        Quando usado o método do_transition inserindo os valores
        Transição -> 3
        Estado -> 1
        deve-se retornar o Estado -> 2
        """
        controller = Controller()
        self.assertEqual(controller.do_transition(2, 1), 3)
        self.assertEqual(controller.do_transition(3, 1), 2)

    def test_do_transition_2(self):
        """
        Quando usado o método do_transition inserindo os valores
        Transição -> 4
        Estado -> 2
        deve-se retornar o Estado -> 3
        """
        controller = Controller()
        self.assertEqual(controller.do_transition(4, 2), 3)

    def test_do_transition_3(self):
        """
        Quando usado o método do_transition inserindo os valores
        Transição -> 3
        Estado -> 3
        deve-se retornar o Estado -> 2

        Quando usado o método do_transition inserindo os valores
        Transição -> 5
        Estado -> 3
        deve-se retornar o Estado -> 4
        """
        controller = Controller()
        self.assertEqual(controller.do_transition(3, 3), 2)
        self.assertEqual(controller.do_transition(5, 3), 4)

    def test_do_transition_4(self):
        """
        Quando usado o método do_transition inserindo os valores
        Transição -> 1
        Estado - > 4 deve-se retornar o Estado -> 1
        """
        controller = Controller()
        self.assertEqual(controller.do_transition(1, 4), 1)

    """
    Teste de erros do método do_transition:
        Sempre que um valor inserido de transição ou de estado forem
        incorretos o retorno deve ser 0
    """
    def test_do_transition_1_error(self):
        controller = Controller()
        self.assertEqual(controller.do_transition(4, 1), 0)
        self.assertEqual(controller.do_transition(4, 1), 0)

    def test_do_transition_2_error(self):
        controller = Controller()
        self.assertEqual(controller.do_transition(5, 2), 0)

    def test_do_transition_3_error(self):
        controller = Controller()
        self.assertEqual(controller.do_transition(4, 3), 0)
        self.assertEqual(controller.do_transition(4, 3), 0)

    def test_do_transition_4_error(self):
        controller = Controller()
        self.assertEqual(controller.do_transition(5, 4), 0)

    def test_get_transition_possible_1(self):
        """
        Quando usado o método get_transition_possible inserindo
        os valores
        Estado atual -> 2
        Estado anterior -> 3 e um dict(states)
        ele deve retornar uma tuple

        Quando usado o método get_transition_possible inserindo
        os valores
        Estado atual -> 1
        Estado anterior -> 5 e um dict(states)
        ele deve retornar uma list
        """
        state = State()
        controller = Controller()
        self.assertIsInstance(controller.get_transition_possible(2, 3, state.get_states()), tuple)
        self.assertIsInstance(controller.get_transition_possible(1, 5, state.get_states()), list)

    def test_get_transition_possible_1_error(self):
        """
        Quando usado o método get_transition_possible inserindo
        os valores
        Estado atual -> 5
        Estado anterior -> 2 um dict(states) e outros quaisquer valores incorretos
        ele deve retornar um int
        """
        state = State()
        controller = Controller()
        self.assertIsInstance(controller.get_transition_possible(5, 2, state.get_states()), int)


