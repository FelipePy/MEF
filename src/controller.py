from src.transition import Transition
from src.state import State

class Controller:

    def __init__(self, initial_state=4):
        self.class_state = State(initial_state)
        self.class_transition = Transition()

    def get_transition_possible(self):
        """
        :return: As possiveis transições para o estado atual
        """
        state = self.class_state.state
        for key_s, states in self.class_state.states.items():
            if state == key_s:
                if state == 3 and self.class_state.previus_state == 2:
                    value = states
                    states = []
                    for item in value:
                        if item != 3:
                            states.append(item)

                index = len(states)
                if index == 3:
                    list_states = [states[1], states[2]]
                    hour_transition = [self.class_transition.get_hour(states[1]),
                                       self.class_transition.get_hour(states[2])]
                    list_global = [list_states, hour_transition]
                    return list_global
                else:
                    return states[1], self.class_transition.get_hour(states[1])



    def do_transition(self, transition):
        """
        :param transition: Transição que levará a um novo estado
        :return: Um novo estado de acordo com a transição
        """
        state = 0

        if self.class_state.state == 1 and (transition == 2 or transition == 3):
            if transition == 2:
                state = 3
            elif transition == 3:
                state = 2

        if self.class_state.state == 2 and transition == 4:
            state = 3

        if self.class_state.state == 3 and (transition == 3 or transition == 5):
            if transition == 3:
                state = 2
                
            elif transition == 5:
                state = 4

        if self.class_state.state == 4 and transition == 1:
            state = 1

        return state