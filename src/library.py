"""
Файл с функциями для работы программы 'Консольная библиотека'
Описание класса "ListBook" - список книг.
Реализовано:
- инициализация списка;
- инициализация списка книг из файла формата json.
"""
from src.book import Book


class ListBook:
    """
    Класс работы со списком книг.
    """
    __slots__ = ('__books__',)
    
    def __init__(self):
        self.__books__ = {}
    
    def list_book(self):
        return self.__books__
    
    def add_book(self, book: Book):
        """
        Добавить книгу в словарь.
        :param book: Данные по добавляемой книге.
        :return:
        """
        self.__books__[book.id_book] = book
    
    def remove_book(self, id_book: int):
        """
        Удаляем из списка книгу по идентификатору.
        :param id_book: Уникальный идентификатор книги.
        :return: Вернуть книгу?
        """
        self.__books__.pop(id_book)
    
    def find_book_author(self, author: str):
        """
        Ищем книгу по автору.
        :param author: Автор книги.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        pass
    
    def find_book_title(self, title: str):
        """
        Ищем книгу по названию.
        :param title: Название книги.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        pass
    
    def find_book_year(self, year: int):
        """
        Ищем книгу по году издания.
        :param year: Год издания, целое число, 4 цифры.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        pass
