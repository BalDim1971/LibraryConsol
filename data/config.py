"""
Файл с настроечными данными библиотеки.
Наименование файла для хранения книг.
"""
import os.path

BOOK_LIBRARY_FILE = os.path.join(os.getcwd(), 'data', 'library.json')
FILE_ENCODING = "utf-8"
