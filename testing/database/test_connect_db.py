from unittest import TestCase
from program.database.connect_db import ConnectDB

class TestConnectDb(TestCase):

    def test_connect(self):
        """
        Quando usado o método connect ele deve retornar True
        """
        connect_db = ConnectDB()
        self.assertEqual(connect_db.connect(), True, "Servidor desativado")

    def test_connect_error(self):
        """
        Quando usado o método connect ele deve retornar False
        """
        connect_db = ConnectDB(host="Aleatorio")
        self.assertEqual(connect_db.connect(), False, "Servidor ativado")

    def test_disconnect(self):
        """
        Quando usado o método disconnect ele deve retornar True
        """
        connect_db = ConnectDB()
        connect_db.connect()
        self.assertEqual(connect_db.disconnect(), True, "Servidor desconectado")

    def test_disconnect_error(self):
        """
        Quando usado o método disconnect ele deve retornar False
        :return:
        """
        connect_db = ConnectDB()
        self.assertEqual((connect_db.disconnect()), False, "Servidor conectado")

    '''def test_cadaster(self):
        """
        Quando usado o método cadaster ele deve retornar True
        """
        connect_db = ConnectDB()
        connect_db.connect()

        # Para realizar o teste abaixo certifique-se de que o usuário passado não esteja cadastrado
        self.assertEqual(connect_db.cadaster("Usuario", "Senha"), True, "Servidor desativado ou usuário ja cadastrado")

        # Para realizar o teste abaixo certifique-se que usuário ja esteja cadastrado
        self.assertEqual(connect_db.cadaster("Usuario", "Senha"), False, "Servidor desativado ou usuário não cadastrado")'''

    def test_cadaster_error(self):
        connect_db = ConnectDB()
        self.assertEqual(connect_db.cadaster("Usuario", "Senha"), 0, "Servidor conectado")

    def test_login(self):
        connect_db = ConnectDB()
        connect_db.connect()
        # Se o usuário existir e a senha estiver correta
        self.assertEqual(connect_db.login("Usuario", "Senha"), ("Usuario", True))
        # Se o usuario ou senha não estiverem corretos
        self.assertEqual(connect_db.login("UsuarioInexistente", "SenhaErrada"), (0, False))
        # Se o servidor estiver desconectado
        connect_db.disconnect()
        self.assertEqual(connect_db.login("Usuario", "Senha"), (1, False))

    '''def test_login_error(self):
        # Error de MySQL 
        connect_db = ConnectDB()
        connect_db.connect()
        self.assertEqual(connect_db.login("User", "Senha"), (None, False), "ErrorSQL")'''