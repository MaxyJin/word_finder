import re
import os

#файл в котором будем искать нужно положить в директорию к файлу с кодом
#Работает с поиском по английскому тексту

file_name = input("Введите имя файла(с указанием расширения): ") #Получение имени файла
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, file_name)

frequency = {}
document_text = open(os.path.join(current_dir, file_name), 'r') #Присваивание переменной document_text открытого на чтение файла
document_text_lower = document_text.read().lower()
sorting_word_pattern = re.findall(input ("Введите слово, которое нужно найти: "), document_text_lower)
#Создание переменной для поиска введенного пользователем слова

for word in sorting_word_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
#Создание счетчика употребления слова в файле

frequency_list = frequency.keys()

for words in frequency_list:
    print(frequency[words])
#Отображение информации о количестве найденных слов