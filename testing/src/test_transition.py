from unittest import TestCase
from program.src.transition import Transition

class TestTransition(TestCase):

    def test_get_transitions(self):
        """
        Quando usado o método get_transitions deve-se retornar
        um dicionário com as chaves e os valores do dicionário
        transitions
        :return:
        """
        transition = Transition()
        self.assertIsInstance(transition.get_transitions(), dict)
        self.assertEqual(transition.get_transitions(), transition.transitions)

    def test_get_hour(self):
        """
        Quando usado o método get_hour inserindo o valor 2
        deve-se receber a string '12:00' que é o valor
        da chave 2
        """
        transition = Transition()
        self.assertEqual(transition.get_hour(2), transition.transitions[2])

    def test_get_hour_error(self):
        """
        Quando usado o método get_hour inserindo um valor inválido
        deve-se retornar False
        """
        transition = Transition()
        self.assertEqual(transition.get_hour(7), False)
