from controllers import Controller_basic
from db_api import Db_requests_basic
from models import Model_basic
from views import Tkinter_view_basic



if __name__ == '__main__':
    path = 'db_api\database\database_note.db'
    db = Db_requests_basic(path)
    view = Tkinter_view_basic()
    model = Model_basic()
    controller = Controller_basic(db, view, model)

    controller.run()
