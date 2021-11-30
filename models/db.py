import sqlite3

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('library.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn



