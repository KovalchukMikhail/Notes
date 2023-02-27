from data import DbRequests
from entities import Note
class ModelBasic:
    db: DbRequests

    def __init__(self, db: DbRequests):
        self.db = db
    def try_create_db(self):
        if not self.db.check_exist_table():
            self.db.create_table()


    def get_all_notes(self) -> list:
        return self.db.select_all_notes()


    def create_note(self, title: str, text: str) -> Note:
        note = Note(title= title, text= text)
        return note


    def add_note_to_db(self, note: Note):
        self.db.add_note(note= note)