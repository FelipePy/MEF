from program.src.transition import Transition

class Controller:

    def __init__(self):
        self.class_transition = Transition()

    def get_transition_possible(self, current_state: int, previous_state: int, states: dict, transition: Transition):
        """
        :param current_state: Estado atual
        :param previous_state: Estado anterior
        :param states: Dicionário dos estados
        :param transition: Transição
        :return: As possiveis transições para o estado atual
        """
        state = current_state
        for key_s, states in states.items():
            if state == key_s:
                if state == 3 and previous_state == 2:
                    value = states
                    states = []
                    for item in value:
                        if item != 3:
                            states.append(item)

                index = len(states)
                if index == 3:
                    list_states = [states[1], states[2]]
                    hour_transition = [transition.get_hour(states[1]),
                                       transition.get_hour(states[2])]
                    list_global = [list_states, hour_transition]
                    return list_global
                else:
                    return states[1], self.class_transition.get_hour(states[1])



    def do_transition(self, transition:  int, current_state:int) -> int:
        """
        :param transition: Transição que levará a um novo estado
        :param current_state: Estado atual
        :return: Um novo estado de acordo com a transição
        """
        state = 0

        if current_state == 1 and (transition == 2 or transition == 3):
            if transition == 2:
                state = 3
            elif transition == 3:
                state = 2

        if current_state == 2 and transition == 4:
            state = 3

        if current_state == 3 and (transition == 3 or transition == 5):
            if transition == 3:
                state = 2
                
            elif transition == 5:
                state = 4

        if current_state == 4 and transition == 1:
            state = 1

        return state

