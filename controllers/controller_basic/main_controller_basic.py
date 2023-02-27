from models import Model
from entities import Note


class MainController:
    model: Model

    def __init__(self, model: Model):
        self.model = model
        self.model.try_create_db()


    def get_all_notes(self) -> list:
        return self.model.get_all_notes()


    def add_note(self, title: str, text: str):
        note: Note = self.model.create_note(title= title, text= text)
        self.model.add_note_to_db(note= note)
