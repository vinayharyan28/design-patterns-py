from abc import abstractmethod, ABC


class IDatabase(ABC):
    @staticmethod
    @abstractmethod
    def get_database_connection(): ...


class RealDataBaseConnection(IDatabase):
    def __init__(self, user_id, user_password):
        self.user_id = user_id
        self.password = user_password

    def get_database_connection(self):
        return f'Connection execute successfully for user id = {self.user_id}, password = {self.password}'


class DatabaseProxy(IDatabase):
    def __init__(self, user_id, user_password):
        self.user_id, self.user_password, self.connection = user_id, user_password, None

    def get_database_connection(self):
        if not self.connection:
            self.connection = RealDataBaseConnection(self.user_id, self.user_password)
            print('using real database: ')
            return self.connection
        print('using proxy: ')
        return self.connection


if __name__ == '__main__':
    connection = DatabaseProxy('28', 'vinayharyan28')
    connection.get_database_connection()
    connection.get_database_connection()
    connection.get_database_connection()
