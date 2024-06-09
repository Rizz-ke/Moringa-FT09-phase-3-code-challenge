from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM magazines')
        magazines = cursor.fetchall()
        conn.close()
        return [Magazine(magazine['id'], magazine['name'], magazine['category']) for magazine in magazines]

    def __repr__(self):
        return f'<Magazine {self.name}>'
