##############################################################################################################
"""
Файл с сервисными функциями.
1. Основное меню, запрашиваем операцию: choosing_action
2. Функция ввода данных по книге: new_book
3. Функция выбора и поиска книги: choosing_find
"""
##############################################################################################################

from src.book import Book
from src.library import ListBook


def choosing_action() -> int:
    """
    Запрашиваем у пользователя какую операцию выполнить:
    1 - вывести весь список;
    2 - добавить;
    3 - найти;
    4 - удалить;
    5 - изменить статус книги (в наличии или выдана).
    :return: Введенный номер или символ.
    """

    print("\nВыберите операцию работы с библиотекой.")
    print("1. Вывести список книг.")
    print("2. Добавить книгу.")
    print("3. Найти книгу.")
    print("4. Удалить книгу.")
    print("5. Изменить статус книги.")
    print("0. Выход из работы с библиотекой.")
    my_choice = input('Введите нужную цифру и нажмите Enter: ')
    if my_choice.isdigit():
        my_choice = int(my_choice)
    return my_choice


def new_book() -> Book:
    """
    Вводим данные по книге.
    :return:
    """
    title = input('Название книги: ')
    author = input('Автор книги: ')
    year = int(input('Год издания книги: '))
    book = Book(title, author, year)
    return book


def choosing_find(list_book: ListBook) -> ListBook:
    """
    Запрашивает у пользователя, по какому полю ищем.
    1 - Название;
    2 - автор;
    3 - год издания.
    :return:  Введенный номер.
    """
    list_book_find = {}
    while True:
        print("\nВыберите по какому параметру ищем.")
        print("1. Название.")
        print("2. Автор.")
        print("3. Год издания.")
        print("0. Выход из поиска. Вернуть результат.")
        my_choice = input('Введите нужную цифру и нажмите Enter: ')
        if my_choice.isdigit() and 0 <= int(my_choice) <= 3:
            match int(my_choice):
                case 1:
                    title = input("Введите название: ")
                    list_book_find = list_book.find_book_title(title)
                case 2:
                    author = input("Введите автора: ")
                    list_book_find = list_book.find_book_author(author)
                case 3:
                    while True:
                        year = input("Введите год: ")
                        if year.isdigit():
                            list_book_find = (
                                list_book.find_book_year(int(year)))
                            break
                        print("Неверный формат года.")
                case 0:
                    return list_book_find
            print(f"Найдено книг: {len(list_book_find)}")
            if len(list_book_find) > 0:
                print(list_book_find)
        else:
            print("\nНеверная команда.")


def change_status(list_book: ListBook):
    """
    Запросит идентификатор книги.
    Предложить изменить статус книги.
    :param list_book: Список книг в наличии.
    :return:
    """
    while True:
        id_book = input('Введите идентификатор книги (число): ')
        if id_book.isdigit():
            id_book = int(id_book)
            index = list_book.find_index(id_book)
            if index is None:
                print(f'Книги с таким {id_book} нет.')
                continue
            print(f'Для книги с идентификатор={id_book} '
                  f'статус={list_book.list_book()[index].status_str}')
            is_change = input('Меняем статус? 1 - Да, 2 - Нет ')
            if is_change.lower() == 'да' or is_change == '1':
                is_status: bool = not list_book.list_book()[index].status
                print(is_status)
                list_book.list_book()[index].status = bool(is_status)
            print(list_book.list_book()[index].status)
            break

##############################################################################################################
