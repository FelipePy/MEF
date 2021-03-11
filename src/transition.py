class Transition:

    def __init__(self, transition=0):
        self.transition_current = transition
        self.transitions = {1: '08:00' ,2: '12:00', 3: '13:00', 4: '18:00', 5: '22:00'}

    def get_transitions(self):
        return self.transitions
