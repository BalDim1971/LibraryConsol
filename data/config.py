"""
Файл с настроечными данными библиотеки.
Наименование файла для хранения книг.
Кодировка для сохранения файла json.
"""
import os.path

BOOK_LIBRARY_FILE = os.path.join(os.getcwd(), 'data', 'library.json')
FILE_ENCODING = "utf-8"
