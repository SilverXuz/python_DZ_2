"""
4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
"""

n = int(input('Введите натуральное число:'))
spisok_values = []
spisok_keys = []

# Это цикл очистки списка
for i in range(0, n * 2):
    with open('file.txt', 'w') as data:
        data.writelines(' ')

# # Это цикл записи значений списка.
for i in range(-n, n + 1):
    spisok_values.append(i)
print(f'Это список значений: {spisok_values}')

# Словарь значений и индексов
# slovar = {}
# for i in range(-n, n + 1):
#     keys = i + n
#     values = i
#     slovar[keys] = values
# print('Это словарь', slovar)

# Это цикл записи ВСЕХ индексов списка. Можно это задокументировать и ввести некоторые значния руками.
# for i in range(0, n * 2):
#     with open('file.txt', 'a') as data:
#         data.writelines(str(i))
#         data.writelines('\n')

# Запись индексов руками
data = open('file.txt', 'a')
x1 = int(input('Введите индекс для списка от -n до n: ')) # Не стал делать защиту от неверных чисел и цикл на ввод.
data.write(str(x1) + "\n")
x2 = int(input('Введите индекс для списка от -n до n: '))
data.write(str(x2) + "\n")
x3 = int(input('Введите индекс для списка от -n до n: '))
data.write(str(x3) + "\n")
data.close()

# Это цикл считывания данных о введенных индексах с файла.
path = 'file.txt'
data = open(path, 'r')
for line in data:
    spisok_keys.append(line.strip())
print(f'Это список индексов из файла: {spisok_keys}')
data.close()

mult = 1
for i in spisok_keys:
    mult *= spisok_values[int(i)]
print(mult)



# Цикл который будет считать произведение значений по списку индексов
# for i in range(len(spisok_keys)):
#     pr = pr * int(spisok_keys[i])
# print(pr)


