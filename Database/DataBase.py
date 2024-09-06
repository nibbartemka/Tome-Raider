import sqlite3
from functools import wraps
from typing import Protocol

from config import DATABASE_NAME


class DataBaseProtocol(Protocol):
    '''
    Protocol for defining interface for
    particular database classes
    '''

    def execute_SQL(self):
        ...


class SQLiteDataBase(object):
    '''Class for working SQLite3 database'''

    __shared_state = {
        'name': DATABASE_NAME,
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_state

    def execute_SQL(self, func):
        '''Decorator for executing SQL query.'''

        @wraps(func)
        def wrapper(*args, **kwargs):
            conn = sqlite3.connect(self.name)
            cursor = conn.cursor()
            try:
                cursor.executescript(func(*args, **kwargs))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
        return wrapper
