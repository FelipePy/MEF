from unittest import TestCase
from program.src.state import State


class TestState(TestCase):
    def test_get_current_state(self):
        """
        Quando usado o método get_current_state deve-se retornar o valor
        já salvo na variável current_state
        """
        state = State(4)
        self.assertEqual(state.get_current_state(), state.current_state)

    def test_get_previous_state(self):
        """
        Quando usado o método get_previous_state deve-se retornar o valor
        já salvo na variável previous_state
        """
        state = State()
        state.set_previous_state(3)
        self.assertEqual(state.get_previous_state(), state.previous_state)

    def test_get_current_state_name(self):
        """
        Quando usado o método get_current_state_name deve-se retornar
        o nome do estado presente no dicionário de acordo com a chave
        presente na váriavel current_state
        """
        state = State(3)
        self.assertEqual(state.get_current_state_name(), "Descansando")

    def test_get_states(self):
        """
        Quando usado o método get_states deve-se retornar um dicionário
        com todos os valores presentes no dicionário states
        """
        state = State()
        self.assertIsInstance(state.get_states(), dict)
        self.assertEqual(state.get_states(), state.states)

