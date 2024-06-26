# ------------ Задача ------------- #
'''
Дано: Множество уникальных заказов и список выполненных заказов.
Найти: Невыполненные заказы.
Пример:
Входные данные:
Уникальные заказы: {1, 2, 3, 4, 5}
Выполненные заказы: [2, 4]

Выходные данные:
Невыполненные заказы: {1, 3, 5}
'''

# orders = {1, 2, 3, 4, 5} # все заказы
# completed_orders = [2, 4] # выполненные заказы
# unfulfilled_orders = orders.difference(completed_orders) # невыполненные заказы - это разница от
# # сравнения всех заказов и выполненных
# unfulfilled_orders1 = (orders - set(completed_orders)) # можно и так. Мы преобразуем список
# # выполненных заказов в множество и вычитаем его из множества всех заказов
# print(unfulfilled_orders) # печатаем результат с применением .difference
# print(unfulfilled_orders1) # печатаем результат с применением вычитания


# x = 1,000,000 # это будет кортеж (1, 0, 0)
# print(x[2:9]) # будет (0,), так как у кортежа (1, 0, 0) элемент с индексом 2 - это последний ноль
# print(x.count('1')) # тут не содержится строка '1' поэтому вывод будет: 0
# print(x*3) # выведет (1, 0, 0, 1, 0, 0, 1, 0, 0)
# print(int(x)) # кортеж нельзя преобразовать в int, поэтому будет ошибка
# print(x)


#