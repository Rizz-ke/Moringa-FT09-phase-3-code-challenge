from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return [Author(author['id'], author['name']) for author in authors]

    def __repr__(self):
        return f'<Author {self.name}>'
