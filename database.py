import sqlite3

CREATE_TABLES = 'CREATE TABLE IF NOT EXISTS ratings (id INTEGER PRIMARY KEY, name TEXT, cuisine TEXT, rating INTEGER);'

INSERT_DISHES = 'INSERT INTO ratings (name, cuisine, rating) VALUES (?, ?, ?);'

GET_EVERYTHING = 'SELECT * FROM ratings;'

GET_BY_NAME = 'SELECT * FROM ratings WHERE name = ?;'

GET_BY_CUISINE = '''
SELECT * FROM ratings
WHERE name = ?
LIMIT 1;
'''

def connect():
    return sqlite3.connect('dishes_data.db')

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLES)

def insert_dish(connection, name, cuisine, rating):
    with connection:
        connection.execute(INSERT_DISHES, (name, cuisine, rating))

def get_everything(connection):
    with connection:
        return connection.execute(GET_EVERYTHING).fetchall()

def get_by_name(connection, name):
    with connection:
        return connection.execute(GET_BY_NAME, (name,)).fetchall()

def get_by_cuisine(connection, name):
    with connection:
        return connection.execute(GET_BY_CUISINE, (name,)).fetchone()
