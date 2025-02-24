import sqlite3
from config import DATABASE

class DatabaseManager:
    def __init__(self) -> None:
        global db, cur
        db = sqlite3.connect('database.db', check_same_thread=False)
        cur = db.cursor()

    def get_genre(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute('SELECT genre_id FROM genres WHERE genre = ?',)
            return cur.fetchall()[0]
    def get_id(self):
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

    def get_film(self):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(''' SELECT title
                            FROM movies
                            INNER JOIN movies_genres ON movies_genres.movie_id = movies.id
                            INNER JOIN genres ON genres.genre_id = movies_genres.genre_id
                            WHERE vote_average > ?
                            LIMIT 15
                        ''',)
            return cur.fetchall()[0]
        
if __name__ == '__main__':
    manager = DatabaseManager(DATABASE)
