import mysql.connector


class Connect_db:

    host = 'localhost'
    database = 'mef'
    user = 'root'
    password = ''
    connection = None
    cursor = None

    def connect(self):
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
        self.cursor.close()
        self.connection.close()

    def login(self, login, password):
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
        command_sql = "SELECT login, pass FROM cadastrados WHERE login=%s"
        self.cursor.execute(command_sql, (login,))
        logged = self.cursor.fetchone()
        if logged != None and login == logged[0]:
            return True
        else:
            command_sql = "INSERT INTO cadastrados (id, login, pass)VALUES(null, %s, %s)"
            self.cursor.execute(command_sql, (login, password))
            self.connection.commit()
            return False
