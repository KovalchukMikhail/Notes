from data import DBJsonRequests
from models import Note

db = DBJsonRequests('database_json\database_note.json')
# db.create_table()


# for i in range(10):
#     note = Note(title=f"запись {i}", text="Hello")
#     db.add_note(note)
#
# for i in db.select_all_notes():
#     print(i.to_string())

# print(db.select_note_by_id(25).to_string())

# for i in db.select_notes_by_date("13:41:21"):
#     print(i.to_string())

# note = db.select_note_by_id(4)
# print(note.to_string())
# note.set_text("поменял опять")
# db.update_note(note)
# print(db.select_note_by_id(4).to_string())

print(db.remove_note_by_id(4))

for i in db.select_all_notes():
    print(i.to_string())

