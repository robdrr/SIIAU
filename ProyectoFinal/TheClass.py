import mysql.connector
import abc

class DB(abc.ABC):
    def __init__(self):
        self.user='root'
        self.password='1234'
        self.database='siiau'
        self.host = 'localhost'

#importante que recuerden cambiar su contrasenha para cuando quieran hacer pruebas en su equipo

    def open(self):
        self.conexion = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor1=self.conexion.cursor()
        self.cursor2=self.conexion.cursor()
        self.cursor3=self.conexion.cursor()

    def close(self):
        self.conexion.close()
    
    @abc.abstractmethod
    def create(self, object):
        pass

    @abc.abstractmethod
    def read(self, object):
        pass

    @abc.abstractmethod
    def update(self, object):
        pass
    @abc.abstractmethod
    def delete(self, object):
        pass