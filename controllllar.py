states = {1: ['Acordado', 2, 3], 2: ['Trabalhando', 4], 3: ['Descansando', 2, 5], 4: ['Dormindo', 1]}
transition = {1: '08:00', 2: '12:00', 3: '13:00', 4: '18:00', 5: '22:00'}

list = []

for state in states.values():
    index = len(state)
    if index > 2:
        print(state[1], end=' ')
        print(state[2])
    elif index == 2:
        print(state[1])