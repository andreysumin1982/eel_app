# Импортируем модуль подключения к БД Postgres
import psycopg2
from psycopg2 import Error
#
class Connect_db:

    #
    # def __str__(self):
    #     return "* Класс Connect, для работы с базами данных PostgreSQL *"

    #
    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        # Подключение к базе данных
        try:
            self.connectdb = psycopg2.connect(f"host={host} "
                                              f"dbname={dbname} "
                                              f"user={user} "
                                              f"password={password}")
        except (Exception, Error) as error:
            print(f"[error] -> Ошибка соединения с БД {self.dbname}:\n", error)
            self.connectdb.close()
        else:
            print(f'[ok] -> Соединение установлено.\n'
                  f' Пользователь {self.user} '
                  f' подключен к базе данных "{self.dbname}"')

    #
    def executeRequest(self, request):
        """Метод выполняет запрос к бд."""
        try:
            # Курсор для выполнения операций с базой данных
            self.cursor = self.connectdb.cursor()
            if ('select' or 'SELECT') in request: # Если просмотр
                # Выполнение SQL-запроса
                self.cursor.execute(request)
                # Получить результат
                result = self.cursor.fetchall()
                print(f' [+] -> Выполнен запрос: {request}')
                return result
            else:
                # Выполнение SQL-запроса
                self.cursor.execute(request) # Если редактирование
                self.transactionCommit()  # commit
        except(Exception, Error) as error:
            print(f"[error] -> {error}")
            return error

    #
    def transactionCommit(self):
        self.connectdb.commit()
        print("[ok] -> Транзакция успешно завершена.")

    #
    def convertResult(self, request):
        "* Метод преобразовывает структуру данных в словарь *"
        result = {}
        try:
            for key, value in enumerate(request):
                if key not in result:
                    result[key] = list(map(lambda x: str(x), value))
            return result
        except (Exception, Error) as error:
            print(f'[error] -> {error}')
            return error

    #
    def __del__(self): \
            # Закрыть соединение с базой
        try:
            self.cursor.close()
            self.connectdb.close()
            print(f'[info] -> Соединение закрыто.\n'
                  f' Пользователь {self.user} отключен от базы данных "{self.dbname}"')
        except (Exception, Error) as error:
            print(f'[error] -> {error}')
            return error


#
if __name__ == '__main__':
    pass