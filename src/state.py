from src.transition import Transition


class State:

    def __init__(self, state=0, transition=0):
        self.states = {1: 'Acordado', 2: 'Trabalhando', 3: 'Descansando', 4: 'Dormindo'}
        self.transitions = Transition().get_transitions()

        self.state = state
        self.transition = transition

    def get_state(self):
        return self.state

    def get_transition(self):
        return self.transition

    def get_states(self):
        return self.states