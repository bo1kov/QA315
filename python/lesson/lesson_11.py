# # Задание 1
# '''
# Описание задание
# '''
# from time import sleep
#
# print("решение")
#
# # -------- разбор задач  ------ #
# # задача
# # Дано:
# # n - кол-во сторон (гарантируется, что число целое)
# # a - сторона многоугольника
# # is_fill - нужно залить фигуру (гарантируется, что будет использован только логический тип данных)
# # нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным характеристикам
# #
# # УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную, хочет ли пользователь,
# # чтобы каждая сторона многоугольника была разного цвета)
#
#
# from turtle import *
# from random import *
# n = 4#int(input('Введите количество сторон многоугольника: '))
# a = 100#int(input('Введите длину стороны многоугольника: '))
# col = 'red'#input('Введите название цвета на английском или значение в формате #RRGGBB: ')
# line_color = 1#int(input('Хотите ли вы чтобы каждая сторона многоугольника была разного цвета? \n 1. Да \n 2. Нет \n'))
# b = 1
# c = 0
# colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'yellow']
# fillcolor(col)
# begin_fill()
# right(90)
# for i in range(n):
#     forward(a)
#     right(360 / n)
#     if line_color == 1:
#         for count in range(n):
#             color_line = choice(colors)
#             color(color_line)
# color(col)
# end_fill()
# sleep(5)








# # ---------- Словари ----------- #
# # Словарь dict - ассоциативный массив
# d = {'ключ': 'значение*',
#      'ключ1': 'значение#'} # ключ - должен быть уникальный
#
# чтение
# print(d['ключ']) # выведет 'значение*'
# print(d['Ключ']) # KeyError: 'Ключ' - несуществующий ключ
# print('все значения:', d.values()) # выведет все значения которые лежат в словаре
# в формате: dict_values(['значение*', 'значение#'])
# print('Все ключи: ', d.keys()) # выведет все ключи которые лежат в словаре
# в формате: dict_keys(['ключ', 'ключ1'])
#
# добавление
# d[5] = [0, 67] # добавит в словарь ключ 5 и его значение [0, 67]
# print(d) # выведет {'ключ': 'значение*', 'ключ1': 'значение#', 5: [0, 67]}
#
# # редактирование
# d['ключ1'] = 1 # для ключа 'ключ1', изменит значение на 1 (перезапишет)
# print(d) # выведет {'ключ': 'значение*', 'ключ1': 1, 5: [0, 67]}. У ключа 'ключ1' - значение 1
#
# # удаление
# d.pop(5) # удаление по ключу 5
# print(d) # выведет без ключа 5 и его значения - {'ключ': 'значение*', 'ключ1': 1}


# ------------------------------------- Задача ------------------------------------------------#
# пользователь вводит номер месяца, необходимо
# отобразить кол-во дней (нельзя использовать сторонние модули)
# months = {1: 31,
#           2: [28, 29],
#           3: 31,
#           4: 30,
#           5: 31,
#           6: 30,
#           7: 31,
#           8: 31,
#           9: 30,
#           10: 31,
#           11: 30,
#           12: 31}
# month = 0
# if month in months.keys():
#     print(f'Месяц {month} : {months[month]}')
# else:
#     print("Invalid month")



#—------------------------------- Задача —--------------------------------#
'''
дан  словарь. Напиши CLI(консольную программу) для получение информации о товаре.
ПРИМЕР словаря.
    {
      "название": "Смартфон",
      "цена": 500,
      "категория": "Электроника"
    }
    
входные: Смартфон
выходные: цена: 500, категория: Электроника

входные: Телефон
выходные: Такого товаре нет
'''
# product = {"название": "Смартфон",
#            "цена": 500,
#            "категория": "Электроника"}
#
# name = "Смартфон2" #input
# if name in product.values():# product.values() -> ["Смартфон", 500, "Электроника"]
#     print(f'цена: {product["цена"]}, категория: {product["категория"]}')
# else:
#     print('Такого товаре нет')

# ------------------------------------- Задача ------------------------------------------------#
'''
Условие: В лесу живут разные животные, и у каждого есть свой домик с номером. 
Информация о животных и номерах их домиков записана в словаре, где ключ — это имя животного, 
а значение — номер домика. Нужно написать программу, которая поможет найти, 
в каком домике живет заданное животное.
Данные для примера: {"Заяц": 23, "Волк": 45, "Медведь": 77}
'''
# animals = {"Заяц": 23, "Волк": 45, "Медведь": 77}
# animal = "Медведь"
# if animal in animals.keys():
#     print(f'Животное {animal} живет в домике {animals[animal]}')
# else:
#     print('Такого животного нет')


# ------------------------------------- Задача ------------------------------------------------#
'''
У каждого пирата есть карта, которая представлена в виде словаря, 
где ключ — это остров, а значение — это количество зарытых сокровищ на этом острове. 
Необходимо написать программу, которая найдёт остров с максимальным количеством сокровищ.
- ** Данные для примера **: `{"Остров Сокровищ": 5, "Необитаемый остров": 3, "Остров Снов": 7}`
'''
# islands = {"Остров Сокровищ": 5,
#            "Необитаемый остров": 3,
#            "Остров Снов": 7}
# max_treasures = 0 # максимальные сокровища пока 0
# max_islands = "" # остров с максимальными сокровищами пока пустая строка
# for island in islands: # для острова в словаре островов:
#     if islands[island] > max_treasures: # если значение по каждому ключу(острову) в словаре,
#         # больше переменной максимального сокровища
#         max_treasures = islands[island] # то переменная максимального сокровища перезаписывается
#         max_islands = island # переменная максимального острова принимает значение ключа острова
#         # с максимальным сокровищем (значением)
# print(f'"{max_islands}" - остров с максимальным количеством сокровищ: {max_treasures}')

# а можно сократить код
# for island in islands.keys():
#     if islands[island] == max(islands.values()):
#         print(f'Остров с максимальным количеством сокровищ: {island}')

# --------- Методы max, min, sort, sorted --------- #
s = [56, 67, 89, 78]
# разобраться с sort
print(max(s))
print(min(s))
print(sorted(s))

# ------------------------------------Задача------------------------------#
# Дан список чисел, необходимо посчитать кол-во каждого уникального числа
# и сформировать из этих данных словарь

# nums = [56, 56, 60, 34, 60, 60]
# new_nums = list(set(nums))
# count_nums = len(new_nums)
# print(new_nums)
# print(count_nums)

# ------------------------------------Задача------------------------------#
'''
**Задача: "Управление финансами счетовода Карла"**

Карл - счетовод в небольшой компании, но его математические навыки оставляют желать лучшего. Ему необходимо создать программу для учета финансов компании за месяц. Напишите программу, которая поможет Карлу вычислить общий доход, общие расходы и остаток средств за месяц на основе предоставленных списков доходов и расходов.

**Пример:**

*Входные данные:*

```
Список доходов: [1000, 500, 700]
Список расходов: [300, 200, 400]
```

*Выходные данные:*

```
Общий доход: 2200
Общие расходы: 900
Остаток средств: 1300
```

В этой задаче Карлу необходимо просто ввести списки доходов и расходов, а программа сама вычислит общий доход, общие расходы и остаток средств.

'''
# income = [1000, 500, 700]
# expenses = [300, 200, 400]
# total_income = sum(income)
# total_expenses = sum(expenses)
# balance = total_income - total_expenses
# dict = {'income': total_income,
#         'expenses': total_expenses,
#         'balance': balance}
# print(dict)
