import sqlite3
from functools import wraps

from database import Data

DATABASE_NAME = 'db.sqlite3'
db = DataBaseConnection(DATABASE_NAME)

@db.get_db_connection()
def create_user_table(cursor: sqlite3.Cursor) -> None:
    '''Function for creating user table'''
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS user (
                user_id BIGINT PRIMARY KEY
            )
        '''
    )


create_user_table()
