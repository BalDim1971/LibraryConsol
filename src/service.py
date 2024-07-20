##############################################################################################################
"""
Файл с сервисными функциями.

1. Функция записи файла с проверкой пути: save_one_file
"""
##############################################################################################################

from data.config import BOOK_LIBRARY_FILE
import os
import json

from src.book import Book

def save_one_file(name_file_par: str, json_data):
    """
    Функция для записи файла с проверкой наличия пути.

    Функция принимает на вход имя файла и данные для записи, json-формат
    Если имя файла не содержит в пути 'data', добавляем.
    Если имя пустое, возвращаем -1.
    Параметры:
    :param name_file_par: имя файла, будет располагаться в каталоге data,
    относительно текущего каталога
    :param json_data: данные для записи

    :return: -1, если передали пустое значение
    """
    
    if name_file_par is None or len(name_file_par) == 0:
        return -1
    
    name_file = name_file_par
    path_list = name_file.split(os.sep)
    if len(path_list) == 0:
        return -1
    
    if not ('data' in path_list):
        name_file = os.path.join('data', name_file_par)
    
    if not os.path.exists('data'):
        name_file = os.path.join('..', name_file)
    
    with open(name_file, "w", encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


def choosing_action() -> int:
    """
    Запрашиваем у пользователя какую операцию выполнить:
    1 - вывести весь список;
    2 - добавить;
    3 - найти;
    4 - удалить;
    5 - изменить статус книги (в наличии или выдана)
    """

    print("\nВыберите операцию работы с библиотекой.")
    print("1. Вывести список книг.")
    print("2. Добавить книгу.")
    print("3. Найти книгу.")
    print("4. Удалить книгу.")
    print("5. Изменить статус книги.")
    print("0. Выход из работы с библиотекой.")
    my_choice = int(input('Введите нужный номер или 0 и нажмите Enter: '))
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

    
##############################################################################################################
