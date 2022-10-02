"""
5) Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
"""

import datetime
import time

spisok_random = [1, 2, 3, 4, 5, 6]
n = len(spisok_random)
print("Оригинальный список: ", spisok_random)

for i in range(n):
    # Искусственный рандомайзер
    j = datetime.datetime.now().microsecond % n
    time.sleep(0.2)
    i_shuffle=spisok_random.pop(j)
    spisok_random.append(i_shuffle) 
print("Перемешанный список: ", spisok_random)
