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

orders = {1, 2, 3, 4, 5} # все заказы
completed_orders = [2, 4] # выполненные заказы
unfulfilled_orders = orders.difference(completed_orders) # невыполненные заказы - это разница от сравнения всех заказов и выполненных
print(unfulfilled_orders)

# ------------ Задача ------------- #
'''
Дан список целых или дробных чисел
Найдите количество уникальных элементов данного массива.
'''

list_ = [3.14, 15, 27, 15, 0.1, 100, 100, 15, 27] # список
count_unique_elements = 0 # количество уникальных элементов (не повторяющихся) у которых нет дубликатов
for i in list_: # пробегаем по элементам списка
    if list_.count(i) == 1: # если количество элемента (i) равно 1, т.е. он в единственном экземпляре, то:
        count_unique_elements += 1 # количество уникальных элементов увеличивается на 1

print(f'Количество уникальных элементов: {count_unique_elements}')


# если элемент повторяется, то мы его не учитываем. Уникальными считаем числа которые не повторяются в списке


# ------------ Задача ------------- #
'''
Дан список целых или дробных чисел
Найдите количество различных элементов данного массива.
'''
list_ = [3.14, 15, 27, 15, 0.1, 100, 100, 15, 27] # список
different_elements = len(set(list_)) # преобразуем список в множество, тем самым избавляемся от повторяющихся элементов и на всякий случай присваиваем ему переменную
print(f'Количество различных элементов: {different_elements}')



# ------------ Задачи "на подумать дома" ------------- #
# t1 = (5, [3, 4, 6])
# t1[1][0] = 0 # Почему не будет ошибки?
# # элемент под индексом 1 - это список [3, 4, 6]
# # элемент списка под индексом 0 - это число 3, которое мы меняем (переназначаем) на 0
# print(t1) # (5, [0, 4, 6])
# #
# t2 = 5, 4, 6
# t2 = 3, 4, 6 # Почему не будет ошибки?
# # потому что мы не изменяем этот кортеж, а перезаписываем (переопределяем).
# print(t2) # (3, 4, 6)
