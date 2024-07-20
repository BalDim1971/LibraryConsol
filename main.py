"""
Основной файл программы 'Консольная библиотека'.
"""

from src.book import Book
from src.library import ListBook
from src.service import choosing_action, new_book


def main():
    """
    Головная функция программы.
    1. Запускаем бесконечный цикл работы.
    2. Запрашиваем у пользователя какую операцию выполнить:
    - добавить;
    - удалить;
    - найти;
    - вывести весь список;
    - изменить статус книги (в наличии или выдана)
    
    :return:
    """
    list_book = ListBook()
    while True:
        my_choice = choosing_action()
        if my_choice == 0:
            break
        match my_choice:
            case 1:
                print("Выводим список книг.")
                print(list_book.list_book())
            case 2:
                print("Добавляем книгу.")
                book: Book = new_book()
                list_book.add_book(book=book)
            case 3:
                print("Найти книгу.")
            case 4:
                print("Удалить книгу.")
            case 5:
                print("Сменить статус книги.")
            case _:
                print("Неверная команда.")


# Нажать зеленую кнопку слева для запуска скрипта.
if __name__ == '__main__':
    main()
