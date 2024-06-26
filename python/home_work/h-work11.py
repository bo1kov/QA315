# -------------- Задача --------------- #
'''
Условие: В мире фэнтези каждый герой имеет специальный артефакт, который приносит определенные бонусы. Словарь содержит имя героя и название его артефакта. Нужно написать программу, которая позволит узнать, какой артефакт принадлежит каждому герою.
Данные для примера: {"Артур": "Меч Света", "Мелиса": "Щит Тьмы", "Рон": "Посох Мудрости"}
'''
world_fantasy = {"Артур": "Меч Света", "Мелиса": "Щит Тьмы", "Рон": "Посох Мудрости"}
name = input('Введите имя героя: ') # принимаем на вход имя героя
if name in world_fantasy: # если имя (ключ) содержится в словаре, то:
    print(world_fantasy[name]) # выводим значение соответствующее ключу
else:
    print('Такого героя нет в словаре') # иначе выводим соответствующее сообщение


# -------------- Задача --------------- #
'''
Условие**: В зоопарке каждый вид животных обитает в своем секторе. 
Информация о животных хранится в словаре, где ключ — это вид животного, 
а значение — это количество этих животных в зоопарке. 
Требуется написать программу, которая посчитает общее количество животных в зоопарке.
Данные для примера: {"лев": 4, "тигр": 2, "слон": 3}
'''
zoo = {"лев": 4, "тигр": 2, "слон": 3}
total = 0
for animal in zoo:
    total += zoo[animal]
print(f'Всего в зоопарке {total} животных')


# -------------- Задача --------------- #
'''Даны два списка: [1, 3, 5, 7] и [2, 4, 6, 7].
Найти и вывести пересечение множеств.
Выходные данные: 7.
'''
list_1 = [1, 3, 5, 7]
list_2 = [2, 4, 6, 7]
print(set(list_1) & set(list_2)) # преобразуем списки в множества и находим пересечение



