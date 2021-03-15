class State:

    def __init__(self, state=4):
        self.states = {1: ['Acordado', 2, 3], 2: ['Trabalhando', 4], 3: ['Descansando', 3, 5], 4: ['Dormindo', 1]}
        self.state_initial = state
        self.previus_state = self.state_initial
        self.state = self.state_initial

    def set_state(self, state):
        """
        :param state: Novo valor para o estado
        :return:
        """
        self.state = state

    def set_state_actual(self, previus_state):
        """
        :param previus_state: Estado anterior ao atual
        :return:
        """
        self.previus_state = previus_state

    def get_state_name(self):
        """
        :return: O nome a ação do estado atual
        """
        state = self.state
        for key, name in self.states.items():
            if state == key:
                return name[0]

