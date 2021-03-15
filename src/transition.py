class Transition:

    def __init__(self):
        self.transitions = {1: '08:00', 2: '12:00', 3: '13:00', 4: '18:00', 5: '22:00'}

    def get_hour(self, arg1=0, arg2=0):
        if arg1 != 0 and arg2 != 0:
            return self.transitions[arg1], self.transitions[arg2]
        else:
            return self.transitions[arg1]
