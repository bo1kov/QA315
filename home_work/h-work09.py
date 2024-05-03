'''распечатайте все числа (должны быть только положительные),
которые делятся на 3 без остатка от start до end(включительно)
(start, end - могут быть перепутаны), start, end- гарантируется,
что целые числа.
Найти в этом наборе числа, которые делится на три без остатка
'''

num_start = int(input('Введите начало диапазона: '))
num_end = int(input('Введите конец диапазона: '))
if num_start > num_end:
    num_start, num_end = num_end, num_start
for i in range(num_start, num_end+1):
    if i % 3 == 0:
        print(i)

print('--------------------------------------------------------------') # разделительная линия
# -------------------------------------------------------------- #
'''
Напишите программу, которая подсчитывает количество 
каждого элемента в списке и выводит результат.
'''
# по моему, условия написаны странно. Наверное нужно подсчитать количество элементов в списке
list_ = [1, 7, 'Start', 'Stop', '812', 'Basin Kings', 116, 843,] # Список. Может быть любым
count = 0 # счетчик элементов в списке
for i in range(len(list_)): # цикл по длине списка
    count += 1 # счетчик элементов в списке
    print(i, list_[i]) # отладочный вывод. Выводит индекс и содержание каждого элемента списка
print(f'Количество элементов в списке: {count}') # вывод

print('--------------------------------------------------------------') # разделительная линия
# -------------------------------------------------------------- #
'''
Руководство компании вводит новую политику уравнивания зарплат всех сотрудников.
●	Пример входных данных: [2500, 3200, 2700, 2900, 3100] (текущие зарплаты всех сотрудников компании).
●	Пример выходных данных: "Согласно новой политике, все зарплаты были уравнены до среднего значения 
в размере $2880."
'''

list_salary = [2500, 3200, 2700, 2900, 3100] # Список. Может быть любым
sum_salary = 0 # сумма элементов (зарплат)
for salary in list_salary:
    sum_salary += salary # счетчик элементов в списке
average_salary = sum_salary / len(list_salary) # среднее значение
print(f'Согласно новой политике, все зарплаты были уравнены до среднего значения в размере ${average_salary}')

print('--------------------------------------------------------------') # разделительная линия
# -------------------------------------------------------------- #
'''
Даны два списка. Список с доходами за определенное кол-во месяцев 
(длина списка = кол-во месяцев) и список с затратами за этот же срок. 
Найти прибыль компании за этот период
вход: 
[2000, 300, 1000]    
[3000, 100, 100]
выход: прибыль составила 100 за 3 месяца
'''
income = [2000, 300, 1000] # доходы
expenses = [3000, 100, 100] # расходы (затраты)
profit = 0 # прибыль
months = len(income) # количество месяцев
for i in range(len(income)): # цикл по длине списка
    profit += income[i] - expenses[i] # складываем в прибыль разницу между доходом и расходом за каждый месяц
print(f'Прибыль составила: {profit} за {months} месяца') # вывод

print('--------------------------------------------------------------') # разделительная линия
# -------------------------------------------------------------- #



