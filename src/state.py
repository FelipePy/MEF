class State:

    def __init__(self, state=4):
        self.states = {1: ['Acordado', 2, 3], 2: ['Trabalhando', 4], 3: ['Descansando', 3, 5], 4: ['Dormindo', 1]}
        self.state_initial = state
        self.previus_state = self.state_initial
        self.state = self.state_initial

    def set_state(self, state):
        self.state = state

    def set_state_actual(self, state_actual):
        self.previus_state = state_actual

    def get_state_name(self):
        state = self.state
        for key, name in self.states.items():
            if state == key:
                return name[0]

    def get_name_state(self):
        list_states = []
        for value in self.states.values():
            list_states.append(value[0])

        return list_states

    def get_key_state(self):
        list_keys = []
        for key in self.states.keys():
            list_keys.append(key)

        return list_keys
