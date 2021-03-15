class State:

    def __init__(self, state=4):
        self.states = {1: ['Acordado', 2, 3], 2: ['Trabalhando', 4], 3: ['Descansando', 3, 5], 4: ['Dormindo', 1]}
        self.state_initial = state
        self.previous_state = self.state_initial
        self.current_state = self.state_initial

    def set_current_state(self, state):
        """
        :param state: Novo valor para o estado
        :return:
        """
        self.current_state = state

    def set_previous_state(self, previous_state):
        """
        :param previus_state: Estado anterior ao atual
        :return:
        """
        self.previous_state = previous_state

    def get_current_state_name(self):
        """
        :return: O nome da ação do estado atual
        """
        state = self.current_state
        for key, name in self.states.items():
            if state == key:
                return name[0]

    def get_previous_state(self):
        return self.previous_state

    def get_current_state(self):
        return self.current_state

    def get_states(self):
        return self.states
