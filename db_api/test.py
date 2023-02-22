import sqlite3

import db_requests
from pathlib import Path



db = db_requests.Db_requests_basic('database\database_note.db')

db.create_table_notes()

db.add_note("12.12.22", "Заплатить за квартиру")
db.add_note("12.12.23", "Заплатить за квартиру")
db.add_note("12.12.24", "Заплатить за квартиру")
db.add_note("12.12.25", "Заплатить за квартиру")
db.add_note("12.12.26", "Заплатить за квартиру")
db.add_note("12.12.26", "Заплатить за квартиру2")
db.add_note("12.12.26", "Заплатить за квартиру3")
db.add_note("12.12.26", "Заплатить за квартиру4")
db.add_note("12.12.26", "Заплатить за квартиру5")
db.add_note("12.12.26", "Заплатить за квартиру6")

# print(db.select_note_info_by_id(2))
# print(db.select_note_info_by_date("12.12.25"))
# db.update_note_by_id(3, "13.12.99", "Ох уж это все")
# print(db.select_note_info_by_id(3))
# print('---------------------------------')
# print(db.select_all_note())
# print('---------------------------------')
# db.delete_note_by_id(2)
# print(db.select_all_note())
# print('---------------------------------')
# db.delete_all()
# db.add_note("12.12.22", "Новая2")
# print(db.select_all_note())

# print(db.select_note_info_by_date("12.12.26"))