from src.transition import Transition
from src.state import State


"Transições -> {" \
"1: '08:00', " \
"2: '12:00', " \
"3: '13:00', " \
"4: '18:00', " \
"5: '22:00'}"

"Estados -> {" \
"1: 'Acordado', " \
"2: 'Trabalhando', " \
"3: 'Descansando', " \
"4: 'Dormindo'}"


"acordado : descansando 3 - 18 ou 12 / trabalhando 2 - 13"
"trabalhando : descansando 3 - 18"
"descansando : trabalhando 2 - 13/ dormindo 4 - 22"
"dormindo : acordado 1 - 08"

class Controller:

    def __init__(self, initial_state=4, transition=0):
        self.class_state = State(initial_state)
        self.class_transition = Transition()

    """
    @get_transition_possible 
    Esse método retorna as possíveis transições para o estado atual
    """

    # Para quando as possiveis transições forem igual a transição, enviar transição junto
    def get_transition_possible(self):
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
        returned = 0 # Estado que será retornado

        if self.class_state.state == 1 and (transition == 2 or transition == 3):
            if transition == 2:
                returned = 3
            elif transition == 3:
                returned = 2

        if self.class_state.state == 2 and transition == 4:
            returned = 3

        if self.class_state.state == 3 and (transition == 3 or transition == 5):
            if transition == 3:
                returned = 2
                
            elif transition == 5:
                returned = 4

        if self.class_state.state == 4 and transition == 1:
            returned = 1

        return returned