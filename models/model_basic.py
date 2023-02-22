import sqlite3
import db_api

class Model_basic:
    def try_create_db(self, db):
        try:
            db.create_table_notes()
        except sqlite3.OperationalError as e:
            print(e)
        except Exception as e:
            print(e)
