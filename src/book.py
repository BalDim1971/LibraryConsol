"""
Файл с классами для работы программы 'Консольная библиотека'.
Описание класса "Book" - Книга
Реализованы:
- инициализация новой книги.
"""


class Book:
    """
    Класс описания и работы с одной книгой.
    Атрибуты:
    int: __id_book - уникальный идентификатор, генерируется автоматически;
    str: __title - название книги;
    str: __author - автор книги;
    int: __year - год издания;
    bool: __status - статус книги: True - “в наличии”, False - “выдана”.
    Атрибуты реализованы как приватные, добавлены геттеры и сеттеры.
    На уровне класса глобальный счетчик для задания уникальных номеров и
    словарь для преобразования кодов статуса в наименования и обратно.
    
    """
    id: int = 1
    status_dict: dict = {True: 'в наличии', False: 'выдана'}
    name_fields: tuple = ('Идентификатор', 'Название', 'Автор',
                          'Год издания', 'Наличие')
    
    __slots__ = ('__id_book', '__title', '__author', '__year', '__status',)
    
    def __init__(self, title: str, author: str,
                 year: int, status: bool = True, id_book: int = 0) -> None:
        """
        Инициализация объекта.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        :param status: Статус книги. True - в наличии, False - выдана. По
        умолчанию True.
        :param id_book: Идентификатор книги. По умолчанию формируется из
        классового идентификатора.
        """
        self.__id_book = id_book if id_book != 0 else Book.id
        self.__title = title
        self.__author = author
        self.__year = year
        self.__status = status
        Book.id = id_book if (id_book != 0 and id_book > Book.id) \
            else Book.id + 1
    
    def __repr__(self):
        """
        'Магический' метод отладочного вывода.
        Формирует строку с полными данными объекта через табуляцию.
        :return:
        """
        return (f'{self.__id_book}\t{self.__title}\t{self.__author}\t'
                f'{self.__year}\t{self.__status}')
    
    def __str__(self):
        """
        'Магический' метод вывода данных.
        Формирует 'красивую' строку с полными данными объекта
        на отдельной строке для каждого параметра.
        :return:
        """
        return (f'Заголовок: {self.__title}\n'
                f'Автор: {self.__author}\n'
                f'Год издания: {self.__year}\n'
                f'Статус книги: {Book.status_dict[self.__status]}')
    
    # Блок геттеров
    # Геттер для идентификатора
    @property
    def id_book(self) -> int:
        return self.__id_book
    
    # Геттер для названия
    @property
    def title(self) -> str:
        return self.__title
    
    # Геттер для автора
    @property
    def author(self) -> str:
        return self.__author
    
    # Геттер для года издания
    @property
    def year(self) -> int:
        return self.__year
    
    # Геттер для статуса стандартный
    @property
    def status(self) -> bool:
        return self.__status
    
    # Геттер для статуса строка из status класса
    @property
    def status_str(self) -> str:
        return Book.status_dict[self.__status]
    
    # Блок сеттеров
    # Сеттер для идентификатора
    @id_book.setter
    def id_book(self, id_book: int):
        self.__id_book = id_book
    
    # Сеттер для названия
    @title.setter
    def title(self, title: str):
        self.__title = title
    
    # Сеттер для автора
    @author.setter
    def author(self, author: str):
        self.__author = author
    
    # Сеттер для года
    @year.setter
    def year(self, year: int):
        self.__year = year
    
    # Сеттер для статуса
    @status.setter
    def status(self, status: bool):
        self.__status = status
    
    @status_str.setter
    def status_str(self, status: str):
        is_status = True if status == Book.status_dict[True] else False
        self.__status = is_status
    
    def to_json(self) -> dict:
        json_data = {
            "id": self.__id_book,
            "title": self.__title,
            "author": self.__author,
            "year": self.__year,
            "status": Book.status_dict[self.__status]
        }
        return json_data
    
    def from_json(self, json_data: dict):
        self.__id_book = json_data["id"]
        self.__title = json_data["title"]
        self.__author = json_data["autor"]
        self.__year = json_data["year"]
        self.__status = [k for k, v in Book.status_dict.items()
                         if v == json_data['status']]
