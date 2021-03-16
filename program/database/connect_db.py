import mysql.connector


class ConnectDB:

    connection = None,
    cursor = None

    def __init__(self, host = 'localhost', database = 'mef', user = 'root', password = ''):
        self.host = host
        self.database = database
        self.user = user
        self.password = password


    def connect(self):
        """
        Método para criar uma conexão com o banco de dados
        :return: bool
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            return True
        except:
            return False

    def disconnect(self):
        """
        Método para desconecatar do banco de dados
        :return: bool
        """
        try:
            self.cursor.close()
            self.connection.close()
            return True
        except:
            return False

    def login(self, login, password):
        """
        Método para fazer login no sistema
        :param login: Nome do usuário
        :param password: Senha do usuário
        :return: tuple
        """
        if self.connection.is_connected():
            try:
                command_sql = "SELECT login, pass FROM cadastrados WHERE login=%s"
                self.cursor.execute(command_sql, (login,))
                logged = self.cursor.fetchone()
            except:
                return None, False

            if logged != None and logged[0] == login and logged[1] == password:
                return logged[0], True
            else:
                return 0, False
        else:
            return 1, False

    def cadaster(self, login, password):
        """
        Método para cadastrar-se no sistema
        :param login: Nome do usuário
        :param password: Senha do usuário
        :return: bool
        """
        if type(self.connection) != tuple:
            command_sql = "SELECT login, pass FROM cadastrados WHERE login=%s"
            self.cursor.execute(command_sql, (login,))
            logged = self.cursor.fetchone()

            if logged != None and login == logged[0]:
                return False
            else:
                command_sql = "INSERT INTO cadastrados (id, login, pass)VALUES(null, %s, %s)"
                self.cursor.execute(command_sql, (login, password))
                self.connection.commit()
                return True
        return 0