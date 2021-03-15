from program.src.state import State
from program.database.connect_db import Connect_db
from program.src.controller import Controller
from program.src.transition import Transition

class Main:
    is_logged = False
    connection = Connect_db()
    is_connected = connection.connect()
    controller = Controller()
    class_transition = Transition()
    if is_connected:
        login = str(input("Digite seu login: "))
        password = str(input("Digite sua senha: "))

        is_logged = connection.login(login, password)

        if is_logged[1]:
            print(f"===== Seja bem vindo {is_logged[0]} =====")
            print("\nOBS: Estado padrão 0\n")

            while True:
                print("Estados ->")
                state_initial = State()
                for key, name in state_initial.get_states().items():
                    print(f"{key} - {name[0]}")
                try:
                    initial_state = int(input("Digite o estado inicial: "))
                    if initial_state in range(1, 5):
                        break
                    elif initial_state == 0:
                        initial_state = 4
                        break

                except:
                    print("Tipo esperado -> int")

            class_state = State(initial_state)
            transition = 0
            while True:
                transition_possible = controller.get_transition_possible(class_state.get_current_state(),
                                                                         class_state.get_previous_state(),
                                                                         class_state.get_states(),
                                                                         class_transition)

                print(f"\n\n\nEstado atual -> {class_state.get_current_state_name()}")
                if type(transition_possible[0]) == list:
                    print(f"Transições possíveis -> \033[32m({transition_possible[0][0]} - {transition_possible[1][0]}) "
                          f"e ({transition_possible[0][1]} - {transition_possible[1][1]})\033[0m")

                    while True:
                        try:
                            transition = int(input("Digite a transição: "))
                        except:
                            print("Tipo esperado -> int")

                        if transition in transition_possible[0]:
                            state = controller.do_transition(transition, class_state.get_current_state())
                            class_state.set_previous_state(class_state.get_current_state())
                            class_state.set_current_state(state)
                            break
                        else:
                            print("\n\n\033[31mTransição incorreta! Tente novamente\033[0m", end='')
                            break

                else:
                    print(f"Transição possível -> \033[32m({transition_possible[0]} - {transition_possible[1]})\033[0m")
                    while True:
                        try:
                            transition = int(input("Digite a transição: "))
                        except:
                            print("Tipo esperado -> int")
                        if transition in transition_possible:
                            state = controller.do_transition(transition, class_state.get_current_state())
                            class_state.set_previous_state(class_state.get_current_state())
                            class_state.set_current_state(state)

                            break
                        else:
                            print("\n\n\033[31mTransição incorreta! Tente novamente\033[0m", end='')
                            break

        elif is_logged[0] == 0 and not is_logged[1]:
            print("Usuário ou senha incorreta!")
            register = ''
            while register != 's' and register != 'n':
                register = str(input("Deseja cadastrar-se? [s/n]: ")).lower()

                if register == 's':
                    login = str(input("Digite seu login: "))
                    password = str(input("Digite sua senha: "))
                    is_cadaster = connection.cadaster(login, password)

                    if is_cadaster:
                        print("Usuário ja cadastrado, reinicie e tente fazer o login novamente\n\n")
                        exit(0)

                    else:
                        print("Cadastrado com sucesso!")
                        print("Reinicie e faça o login")
                        exit(0)

                elif register == 'n':
                    print("Até mais")
                    exit(0)

                else:
                    print("Reposta incorreta, tente novamente!")

        elif is_logged[0] == 1 and not is_logged[1]:
            print("{1}Impossível se conectar com o banco de dados")
            exit()

        elif is_logged == None and not is_logged:
            print("Algo errado! tente novamente mais tarde.")
        else:
            print("Error")
            exit()

    else:
        print("Impossível se conectar com o banco de dados")
        exit()
    connection.disconnect()
