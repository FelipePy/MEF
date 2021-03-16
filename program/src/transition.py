class Transition:

    def __init__(self):
        self.transitions = {1: '08:00', 2: '12:00', 3: '13:00', 4: '18:00', 5: '22:00'}

    def get_hour(self, arg1: int):
        """
        :param arg1: Recebe uma chave
        :return: O valor do dicionário correspondente a chave recebida
        """
        if arg1 in range(1, 6):
            return self.transitions[arg1]
        else:
            return False

    def get_transitions(self):
        return self.transitions
