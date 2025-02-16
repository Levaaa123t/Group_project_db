import sqlite3

class DatabaseManager:
    def __init__(self, database):
        self.database = database

    def get_genre(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT genre_id FROM genres WHERE genre = ?',)
            return cur.fetchall()[0]
    def get_year(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT id FROM movies WHERE vote_average > ?',)
            return cur.fetchall()[0]
    def get_title(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT title FROM movies',)
            return cur.fetchall()[0]
