from controllers import MainController
from .menu import Menu
from entities import Note

class ViewConsoleBasic:
    main_menu_dict: dict
    controller: MainController
    menu: Menu

    def __init__(self, controller: MainController):
        self.controller = controller
        self.menu = Menu()
        self.main_menu_dict = {1: self.show_all_notes,
                               2: self.run_select_menu,
                               3: self.run_add_menu,
                               4: self.run_update_menu,
                               5: self.run_remove_menu}


    def run_main_menu(self):
        while True:
            self.__show_text(self.menu.main_menu)
            answer: int = self.__select_menu_item(min=0, max=5)
            if answer == 0:
                return
            elif answer == -1:
                self.__show_error()
                continue
            else:
                self.main_menu_dict.get(answer)()


    def show_all_notes(self):
        notes_list: list = self.controller.get_all_notes()
        if notes_list == []:
            self.__show_text("Заметки отсутсвуют")
        for n in notes_list:
            self.__show_text(n.to_string())
        input("для продолжения нажмите Enter")


    def run_select_menu(self):
        print("Select menu")

    def run_remove_menu(self):
        print("Remove menu")

    def run_update_menu(self):
        print("Update menu")

    def run_add_menu(self):
        title: str = 'Нет заголовка'
        text: str = 'Нет текста заметки'
        while True:
            self.__show_text(self.menu.add_menu)
            answer: int = self.__select_menu_item(min=0, max=3)
            if answer == 0:
                return
            elif answer == -1:
                self.__show_error()
                continue
            elif answer == 1:
                title = input("Введите текст заголовка\n")
            elif answer == 2:
                text = input("Введите текст заметки\n")
            elif answer == 3:
                self.run_prenote_menu(title= title, text= text)



    def run_prenote_menu(self, title: str, text: str):
        prenote: str = f'title: {title}\ntext:{text}'
        while True:
            self.__show_text('Предварительный просмотр заметки')
            self.__show_text(prenote)
            self.__show_text(self.menu.prenote_menu)
            answer: int = self.__select_menu_item(min=0, max=2)
            if answer == 0:
                return
            elif answer == -1:
                self.__show_error()
                continue
            elif answer == 1:
                self.controller.add_note(title=title, text=text)
                return



    def __show_text(self, text):
        print(text)

    def __select_menu_item(self, min: int, max: int) -> int:
            answer = int(input())
            if min <= answer <= max:
                return answer
            return -1


    def __show_error (self):
        print("Вы ввели некоректное значение")

