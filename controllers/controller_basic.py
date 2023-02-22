import db_api
import models
import views


class Controller_basic:

    def __init__(self, db, view, model):
        self.db = db
        self.view = view
        self.model = model

    def run(self):
        self.model.try_create_db(self.db)
