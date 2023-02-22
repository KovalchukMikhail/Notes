import sqlite3


class Db_requests_basic:
    def __init__(self, db_path):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_notes(self):
        sql = """
        CREATE TABLE Notes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date text,
        note text);
        """
        self.execute(sql, commit=True)


    def add_note(self, date: str, note: str):
        sql = 'INSERT INTO Notes(date, note) VALUES(?, ?)'
        parameters = (date, note)
        self.execute(sql, parameters, commit=True)

    def select_note_info_by_id(self, id: int) -> list:
        sql = 'SELECT * FROM Notes WHERE id=?'
        return self.execute(sql, parameters=(id, ), fetchone=True)

    def select_note_info_by_date(self, date: str) -> list:
        sql = 'SELECT * FROM Notes WHERE date=?'
        return self.execute(sql, parameters=(date, ), fetchone=True)

    def update_note_by_id(self, id: int, date: str, note: str):
        sql = 'UPDATE notes SET date=?, note=? WHERE id=?'
        return self.execute(sql, parameters=(date, note, id), commit=True)

    def select_all_note(self) -> list:
        sql = 'SELECT * FROM Notes'
        return self.execute(sql, fetchall=True)

    def delete_note_by_id(self, id: int):
        sql = "DELETE FROM Notes WHERE id=?"
        return self.execute(sql, parameters=(id, ), commit=True)
    def delete_all(self):
        self.execute("DELETE FROM Notes WHERE True", commit=True)
