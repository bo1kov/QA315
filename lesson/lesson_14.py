#---------------------Файлы---------------------------#
# Запись данных в  файл
# !!! Старые данные будут перезаписаны !!!
# with open('data.txt', 'w', encoding='UTF-8') as f:
#     # s = 'это строка'
#     prices = ['1000', '2000', '340']
#     s = '\n'.join(prices) #  prices[0] + '\n' +....
#     f.write(s) #  write() argument must be str

# # Дозапись данных
# with open('data.txt', 'a', encoding='UTF-8') as f: # a - add
#     s = '\nэто строка'
#     f.write(s)

# import json
# # # запись данных в json
# # with open('data.json', 'a', encoding='UTF-8') as file:
# #     d = {'product1': 1000,
# #          'product2': 2300}
# #     json.dump(d, file)


# ------------------- функции -------------------------- #
# функция - это сохраненный алгоритм(кусок кода, который решает поставленную задачу)

# from turtle import*
# from time import sleep
#
# left(45)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
# right(180)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
# right(180)
# forward(100)
# right(90)
#
# # нарисовать квадрат
# for side in range(4):
#     forward(100)
#     left(90)
#
#
# sleep(5)


# #--------------------------#
# from turtle import*
# from time import sleep
#
# # def name_function(arguments):
# #     actions
#
# def draw_square(): #Определяем функцию
#     for side in range(4):
#         forward(100)
#         left(90)
#
# left(45)
#
# # нарисовать квадрат
# draw_square() # вызов функции
#
# right(180)
#
# # нарисовать квадрат
# draw_square()
#
# right(180)
# forward(100)
# right(90)
#
# # нарисовать квадрат
# draw_square()
#
#
# sleep(5)

# -------------- Задача ---------------- #
# from turtle import *
# from time import sleep
# def draw_triangle():
#     for side in range(3):
#         forward(100)
#         right(120)
# left(90)
# draw_triangle()
# right(90)
# draw_triangle()
# right(60)
# draw_triangle()
# right(60)
# draw_triangle()
# sleep(5)


# ----------------- Задача ---------------- #
'''Напишите функцию для создания 8-угольника с параметрами размер стороны и цвет стороны.
* Создать функцию которая будет рисовать правильный многоугольник
(кол-во сторон, цвет стороны, размер стороны)'''
from turtle import *
from time import sleep

# from turtle import *
# from time import sleep
# def draw_octagon(a, col = 'blue'):
#     color(col)
#     for side in range(8):
#         forward(a)
#         left(45)
# draw_octagon(50)
# left(45)
# draw_octagon(50,'red')
# left(45)
# draw_octagon(50, 'green')
# left(45)
# draw_octagon(50,'black')
# left(45)
# draw_octagon(50, 'yellow')
# left(45)
# draw_octagon(50, 'orange')
# left(45)
# draw_octagon(50, 'red')
# left(45)
# draw_octagon(50)
# left(45)
# sleep(5)


# ----------------- Задача ---------------- #
'''
Создайте функцию для расчета общей стоимости товаров с учетом скидки. 
Функция должна принимать на вход список цен и процент скидки, а затем возвращать общую стоимость.'''
# def total_cost_discount_products(list_of_cost: list, discount: float):
#     total_cost = sum(list_of_cost)  # найти общую сумму
#     total_cost = total_cost * (1 - discount/100)  # вычислить сумму с учетом скидки
#     return total_cost  # вернуть результат
# print(f'Общая стоимость с учетом скидки {total_cost_discount_products()}')  #не работает


# ----------------- Задача ---------------- #
'''
Создайте функции для ввода оценок студентов, расчета средней оценки по 
предмету и выдачи рекомендации (например, "хорошо", "удовлетворительно"). 
Функция расчета средней оценки может использовать результаты функции ввода оценок.
'''


def input_grades():
    grades = []
    while True:
        grade = input('Введите оценку: ')
        if grade == 'q':
            break
        grades.append(int(grade))
    return grades


print(input_grades())


def average_grade(grades):
    return sum(grades) / len(grades)

grades = input_grades()
print(average_grade(grades))
