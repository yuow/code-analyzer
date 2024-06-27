import psycopg2
import dotenv
import os


class Database:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        dotenv.load_dotenv()
        dbname = os.environ.get("DBNAME")
        host = os.environ.get("HOST")
        user = os.environ.get("USER")
        password = os.environ.get("PASSWORD")
        port = os.environ.get("PORT")
        try:
            self._connection = psycopg2.connect(
                dbname=dbname, host=host, user=user, password=password, port=port)
            self._connection.autocommit = True
        except Exception as e:
            print(f'error occured while connecting to database: {e}')

    def execute(self, query, params=None):
        if self._connection is None:
            print("error occured while executing query: database connection is none")
            return

        cursor = self._connection.cursor()
        cursor.execute(query, params)
        try:
            return cursor.fetchall()
        except:
            return
        finally:
            cursor.close()

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None
