from sqlite3 import connect, Connection

class Database:
    
    __connector: Connection
    
    def __init__(self, path: str = ':memory:'):
        self.__connector = connect(path)
