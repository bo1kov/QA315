"""
Дан список элементов 1, 3, 22, 7, 12, 8, 2 (могут быть какие-то другие значения, ввод данных делать не нужно)

1. показать каждый элемент, последняя цифра которого 2
2. показать произведение чисел, последняя цифра которого 2
"""
elements = [1, 3, 22, 7, 12, 8, 2]
product_of_numbers = 1
for i in elements:
    if i % 10 == 2:
        print(i)
        product_of_numbers *= i
print(product_of_numbers)
print() # просто отступ

"""распечатайте все числа, которые делятся на 3 от start до end(включительно) 
(start, end - могут быть перепутаны), start , end- гарантируется, что целые числа"""
start = int(input("Введите первое число: "))
end = int(input("Введите последнее число: "))
if start > end:
    start, end = end, start
for i in range(start, end +1):
    if i % 3 == 0:
        print(i)
