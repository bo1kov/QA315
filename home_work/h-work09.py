'''распечатайте все числа (должны быть только положительные),
которые делятся на 3 без остатка от start до end(включительно)
(start, end - могут быть перепутаны), start , end- гарантируется,
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
print(f'Количество элементов в списке: {count}') # итоговый вывод


