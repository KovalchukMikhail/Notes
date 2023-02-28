
class Menu:
    main_menu: str = """
    ________________________________________________
    Выберити пункт меню
    1 - отобразить все заметки
    2 - поиск заметок
    3 - добавление заметок
    4 - изменение заметок
    5 - удаление заметок
    0 - Выход из приложения
    """

    add_menu: str = """
    ________________________________________________
    Выберити пункт меню
    1 - ввод заголовка
    2 - ввод текста заметки
    3 - Перейти к предварительному просмотру и сохранению
    0 - назад в главное меню
    """

    prenote_menu: str = """
    ________________________________________________
        Выберити пункт меню
        1 - подтведить действие
        0 - назад в меню
    """

    select_menu: str = """
    ________________________________________________
    Выберити пункт меню
    1 - выбор по Id
    2 - выбор по дате
    3 - выбор по заголовку
    0 - назад в главное меню
    """

    remove_menu: str = """
    ________________________________________________
    Выберити пункт меню
    1 - удалить по Id
    2 - удалить все заметки
    0 - назад в главное меню
    """

    update_menu: str = """
    ________________________________________________
    Выберити пункт меню
    1 - изменить заголовок
    2 - изменить текст заметки
    3 - Перейти к предварительному просмотру и сохранению
    0 - назад в главное меню
    """