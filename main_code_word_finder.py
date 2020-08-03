import re
import os

file_name = input("Введите имя файла: ")
"""Получение имени файла"""
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file_name)
"""Присваивание переменной file_path полного пути к файлу в котором будет производиться поиск""" #файл нужно положить
# в директорию к python файлу самой программы

frequency = {}
document_text = open(os.path.join(current_dir, file_name), 'r')
"""Присваивание переменной document_text открытого на чтение файла"""
document_text_lower = document_text.read().lower()
sorting_word_pattern = re.findall(input ("Введите слово, которое нужно найти: "), document_text_lower)
"""Создание переменной для поиска введенного пользователем слова"""

for word in sorting_word_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
"""Создание счетчика употребления слова в файле"""
frequency_list = frequency.keys()

for words in frequency_list:
    print(f'В файле {file_name} найдено {frequency[words]} слова {sorting_word_pattern[1]}')
"""Отображение информации о количестве найденных слов"""