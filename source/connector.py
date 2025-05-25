from sqlite3 import connect, Connection

class Database:
    
    __connector: Connection
    
    def __init__(self, path: str = ':memory:'):
        self.__connector = connect(path)
    
    def execute(self, query: str, params: tuple = ()) -> tuple:
        cursor = self.__connector.cursor()
        try:
            cursor.execute(query, params)
            self.__connector.commit()
            return cursor.fetchall()
        finally:
            cursor.close()
