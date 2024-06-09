'''
# - Задача: написать функцию, которая будет вычислять периметр для правильных многоугольников
'''

# def polygon_P(n, a):
#     if n >= 3 and a > 0:
#         return n * a
#     else:
#         return -1
#
# P = polygon_P(7, 10)
# if P == -1:
#     print('Ошибка')
# else:
#     print(f'P = {P}')

# —------------------------------- Задача —--------------------------------#
'''Сделайте функцию, которая будет возвращать сколько дней осталось до ближайшего 29 февраля.'''
year = int(input('Введите текущий год: '))
vis_year = None
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
    vis_year = year
else:
    for i in range(3):
        year += 1
        print(year)
        if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
            vis_year = year
            print(f'Високосный год {vis_year}')
            break
        
month = int(input('Введите текущий месяц: '))
day = int(input('Введите текущий день: '))