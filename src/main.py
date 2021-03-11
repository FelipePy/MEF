from src.state import State
from src.transition import Transition


class Main:
    state = State()
    transition_initial = Transition()
    states = []
    keys = []

    response = 6
    while response > 5:
        print("\033[04:33mTransições\033[0m   \033[04:33mEstados\033[0m")
        for key, value in state.get_states().items():
            keys.append(key)
            states.append(value)

        cont = 0
        for key, value in transition_initial.get_transitions().items():
            print(f"{value} -> {key}", end="   ")
            try:
                print(f"{states[cont]}", (12-len(states[cont]))*"-"+ f"> {keys[cont]}")
                cont += 1
            except:
                cont = 5

        response = int(input("Digite a transição: "))
        if response > 5:
            print("\n\nTente novamente!")
        else:
            transition = Transition(response)
