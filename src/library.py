"""
Файл с функциями для работы программы 'Консольная библиотека'
Описание класса "ListBook" - список книг.
Реализовано:
- инициализация списка;
- инициализация списка книг из файла формата json.
"""
import json
import os.path

from src.book import Book
from data.config import BOOK_LIBRARY_FILE, FILE_ENCODING


class ListBook:
    """
    Класс работы со списком книг.
    """
    __slots__ = ('__books',)
    
    def __init__(self) -> None:
        """
        Инициализация списка книг.
        """
        self.__books: list[Book] = []
    
    def __repr__(self) -> None:
        """
        'Магический' метод для вывода списка книг в отладочном виде.
        :return:
        """
        list_book_repr: str = ''
        for book in self.__books:
            list_book_repr += book.__repr__()
        return list_book_repr
    
    def __str__(self) -> str:
        """
        'Магический' метод для вывода списка книг в пользовательском виде.
        Вывод осуществляется в виде таблицы.
        :return:
        """
        list_book_str: str = ''
        len_id: int = len(Book.name_fields[0])
        len_author: int = len(Book.name_fields[1])
        len_title: int = len(Book.name_fields[2])
        len_year: int = len(Book.name_fields[3])
        len_status: int = len(Book.name_fields[4])
        
        for book in self.__books:
            len_author = len(book.author) \
                if len(book.author) > len_author else len_author
            len_title = len(book.title)\
                if len(book.title) > len_title else len_title
            len_status = len(Book.status_dict[book.status]) \
                if len(Book.status_dict[book.status]) > len_status \
                else len_status
        
        print(f'{Book.name_fields[0]:{len_id}} |'
              f'{Book.name_fields[1]:{len_author}} |'
              f'{Book.name_fields[2]:{len_title}} |'
              f'{Book.name_fields[3]:{len_year}} |'
              f'{Book.name_fields[4]:{len_status}}')
        for book in self.__books:
            print(f'{book.id_book:{len_id}} |'
                  f'{book.author:{len_author}} |'
                  f'{book.title:{len_title}} |'
                  f'{book.year:{len_year}} |'
                  f'{book.status_str:{len_status}}')
        return list_book_str
    
    def list_book(self) -> list:
        """
        Возвращает список книг.
        :return:
        """
        return self.__books
    
    def clear(self) -> None:
        """
        Очистить список книг.
        :return:
        """
        self.__books.clear()
        
    def count(self) -> int:
        """
        Количество книг
        :return:
        """
        return len(self.__books)
    
    def find_index(self, id_book: int) -> int | None:
        """
        Ищем книгу по идентификатору.
        :param id_book: Уникальный идентификатор книги.
        :return: Индекс найденной книги или None.
        """
        for index in range(len(self.__books)):
            if self.__books[index].id_book == id_book:
                return index
        return None
    
    def add_book(self, book: Book) -> None:
        """
        Добавить книгу в словарь.
        :param book: Данные по добавляемой книге.
        :return:
        """
        self.__books.append(book)
    
    def add_list_book(self, books: list[Book]) -> None:
        """
        Добавить список книг в словарь.
        :param books: Список добавляемых книг.
        :return:
        """
        for book in books:
            self.__books.append(book)
    
    def remove_book(self, id_book: int) -> None:
        """
        Удаляем из списка книгу по идентификатору.
        :param id_book: Уникальный идентификатор книги.
        :return: Ничего. Или вернуть данные книги?
        """
        index = self.find_index(id_book)
        if index is not None:
            self.__books.pop(index)
    
    def find_book_author(self, author: str) -> list[Book]:
        """
        Ищем книгу по автору.
        :param author: Автор книги.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        list_book: list[Book] = []
        for book in self.__books:
            if author in book.author:
                list_book.append(book)
        return list_book
    
    def find_book_title(self, title: str) -> list[Book]:
        """
        Ищем книгу по названию.
        :param title: Название книги.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        list_book = []
        for book in self.__books:
            if title in book.title:
                list_book.append(book)
        return list_book
    
    def find_book_year(self, year: int) -> list[Book]:
        """
        Ищем книгу по году издания.
        :param year: Год издания, целое число, 4 цифры.
        :return: Список (словарь?) найденных книг или None (пустой список?)
        """
        list_book = []
        for book in self.__books:
            if book.year == year:
                list_book.append(book)
        return list_book
    
    def load_json(self) -> None:
        """
        Загружаем список словарей из json-файла
        :return:
        """
        if not os.path.exists(BOOK_LIBRARY_FILE):
            return
        with open(BOOK_LIBRARY_FILE, 'r', encoding=FILE_ENCODING) as f:
            books_json = json.load(f)
        for book_json in books_json:
            status = True
            if book_json['status'] == Book.status_dict[False]:
                status = False
            book = Book(
                book_json["title"],
                book_json["author"],
                book_json["year"],
                status,
                book_json["id"],
            )
            self.__books.append(book)
    
    def save_json(self) -> None:
        """
        Сохраняем список книг в json-файл
        :return:
        """
        books_json = []
        for book in self.__books:
            books_json.append(book.to_json())
        with open(BOOK_LIBRARY_FILE, 'w', encoding=FILE_ENCODING) as f:
            f.write(json.dumps(books_json, indent=2, ensure_ascii=False))
