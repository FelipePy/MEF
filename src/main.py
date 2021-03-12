from src.state import State
from src.transition import Transition
from database.connect_db import Connect_db


class Main:
    state = State()
    transition_initial = Transition()
    states = []
    keys = []

    is_logged = False
    connection = Connect_db()
    is_connected = connection.connect()

    if is_connected:
        login = str(input("Digite seu login: "))
        password = str(input("Digite sua senha: "))

        is_logged = connection.login(login, password)

        while is_logged:

            if is_logged[1]:
                print(f"\n\nSeja bem vindo {is_logged[0]}")
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
                    try:
                        response = int(input("Digite a transição: "))
                    except:
                        print("Argumento inserido incorretamente - Valor esperado -> int")
                    if response > 5:
                        print("\n\nTente novamente!")
                    else:
                        transition = Transition(response)


            elif is_logged[0] == 0 and not is_logged[1]:
                print("Usuário ou senha incorreta!")
                response = ''

                while response != 's' and response != 'n':
                    response = str(input("Deseja cadastrar-se? [s/n]: ")).lower()

                    if response == 's':
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

                    elif response == 'n':
                        print("Até mais")
                        exit(0)

                    else:
                        print("Reposta incorreta, tente novamente!")


            elif is_logged[0] == 1 and not is_logged[1]:
                print("{1}Impossível se conectar com o banco de dados")
                exit()

            elif is_logged == None and not is_logged:
                print("Algo deu errado, tente novamente mais tarde!")
            else:
                print("Error")
                exit()


    else:
        print("Impossível se conectar com o banco de dados")
        exit()
    connection.disconnect()
