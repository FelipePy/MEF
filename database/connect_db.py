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
                self.cursor.execute("SELECT login, pass FROM cadastrados WHERE login=%s", (login,))
                logged = self.cursor.fetchone()
            except:
                return None, False

            if logged != None and logged[1] == password and logged[0] == login:
                return logged[0], True
            else:
                return 0, False
        else:
            return 1, False

    def cadaster(self, login, password):
        self.cursor.execute("SELECT login FROM cadastrados WHERE login=%s", (login,))
        logged = self.cursor.fetchone()
        if logged != None and login == logged[0]:
            return True
        else:
            self.cursor.execute("INSERT INTO cadastrados (id, login, pass)VALUES(null, %s, %s)", (login, password))
            self.connection.commit()
            return False
