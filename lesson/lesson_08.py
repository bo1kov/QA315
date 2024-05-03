# ------------------------------- Циклы ----------------------------------#
# for - перебор чего-то

# for куда_записывать in где_перебираем:
#   Инструкции
'''
цикл перебора
for тарелка in [грязная_тарелка1, грязная_тарелка2, грязная_тарелка3]
    действие
    ....
'''

# for color in 'red', 'green', 'blue', 'black': # набор цветов
#     print(color)
#
# # for num in 345: # так не сработает и выдаст ошибку. Не подлежит перебору!
# #     print(num)
#
# for num in [345]: # а так сработает. Выведет этот элемент списка.
#     print(num, type(num))
#
# for num in '345': # и так сработает. Выведет все элементы строки.
#     print(num, type(num))
#—------------------------------- Задача —--------------------------------#
'''
Дана стоимость продуктов.
Это странный магазин, так как предоставляется скидка в 10% на каждый продукт, 
если его цена кратна 5. 
Показать цены со скидками. 
'''
# prices_products = [15, 25, 34, 50, 33] # список цен
# print(f'Цены на продукты: {prices_products}')
# for price in prices_products:
#     if price % 5 == 0:
#         print(f'Старая цена: {price}, новая цена: {price * 0.9}')
#     else:
#         print(f'Старая цена: {price}, новая цена: {price}')


#—------------------------- Наборы (коллекции) ---------------------------#
# () tuple кортеж
# [] list список
# {} set множества
# {} dict словарь (ассоциативный массив)
# range() - диапазон
#—------------------------------- Range —--------------------------------#
# range(стартовое значение (НЕобяз.), конечное (Обяз.), шаг (НЕобяз.))
# start = 10
# end = 2 # дойдет до 3, потому что 2 НЕ включительно
# step = -1
# for i in range(start, end, step):
#     print(i)

#------------------------------------------------------------------------#
# end = 5
# for i in range(end): # start = 0, step = 1
#     print(i)


# d = range(4, 10)
# print(d, type(d))
# for i in range(4, 10): # ! до 10 НЕ включительно
#     print(i, type(i))
#
# for i in d: # то же самое
#     print(i, type(i))

#—------------------------------- Задача —--------------------------------#
'''
Дан старт и стоп(включительно).
Посчитать кол-во четных чисел
'''
# start = 3 # допустим, мы не знаем, что на входе
# stop = 10 # допустим, мы не знаем, что на входе
# count_even = 0 # количество четных чисел изначально
# if start >= stop:
#     start, stop = stop, start # ракировка :)
#
# for i in range(start, stop+1):
#     if i % 2 == 0:
#         count_even += 1 # считам количество четных, прибавляя по 1 каждую итерацию
# print(count_even)

#—----------------------- другой вариант решения —------------------------#
# start = 3 # допустим, мы не знаем, что на входе
# stop = 10 # допустим, мы не знаем, что на входе
# count_even = 0 # количество четных чисел изначально
# if start >= stop:
#     start, stop = stop, start # ракировка :)
# if start % 2 != 0:
#     start += 1
# for i in range(start, stop+1, 2):
#     count_even += 1 # считам количество четных, прибавляя по 1 каждую итерацию
#     print(f'Количество четных: {count_even}, Число: {i}')


#—------------------------------- Задача —--------------------------------#
'''
Пользователь определяет начальное и конечное значение.
Посчитать кол-во чисел. 
Посчитать кол-во чисел кратных 3.
'''
# start = int(input('Начальное значение: '))
# stop = int(input('Конечное значение: '))
# count = 0
# count_mod_3 = 0
# for num in range(start, stop + 1): # считаем количество чисел
#     count += 1
#     if num % 3 == 0:
#         count_mod_3 += 1
# print(f'Количество чисел: {count}, а количество кратных 3: {count_mod_3}')



#—------------------------------- Задача —--------------------------------#
# Дан диапазон от start до end. End и start могут быть перепутаны.
# и найти сумму всех чисел в указанном диапазоне/

# start = int(input('Введите стартовое число: '))
# end = int(input('Введите конечное число: '))
# summa = 0
# if end <= start:
#     end, start = start, end
# for i in range(start, end+1):
#     summa += i
# print(summa)


#—------------------------------- Задача —--------------------------------#
# Описание задачи:
# Напишите программу, которая запрашивает у пользователя начальное число для обратного отсчета. Затем программа должна выводить числа в убывающем порядке каждую секунду до нуля, после чего выводится сообщение "Старт!".
# Пример работы программы:
# Введите начальное число для обратного отсчета: 5
# 5
# 4
# 3
# 2
# 1
# Старт!

# start = int(input("Начало отсчета: "))
# while start != 0:
#     start -=1
#     print(start+1) # ! без +1, отсчет пойдет с 9  до 0 и только потом выведет "Старт", что не совсем корректно
# print('Start')
#
#
# start = int(input("Введите число: "))
# for i in range(start, 0, -1): # для i в диапазоне(начало, конец, шаг)
#     print(i)
# print('Start')



#—------------------------------- Задача —--------------------------------#
''' У вас есть список ежедневных продаж в течение месяца. Найдите общую сумму продаж за месяц.
Запрещено использовать sum, map,...и тд.
'''
# sales = [300, 450, 100]
# summ = 0
# for sale in sales:
#     summ += sale
# print(f'summ: {summ}')

#—------------------------------- Логические задачи —--------------------------------#
# какие числа попадут в диапазон?
# for i in range(3, 9, 3): # 9 НЕ включительно
#     print(i) # 3, 6

# for i in range(10, 3, -3):
#     print(i) # 10, 7, 4

# for i in range(4):
#     print(i) # 0, 1, 2, 3

# for animal in 'cat', 'dog':
#     print(animal) # cat, dog