'''
Задача:
Дан текстовый файл. Посчитать кол-во букв в файле.
'''
with open('file.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    count = 0
    for i in text:
        if i.isalpha():
            count += 1
    print(f'Количество букв в файле: {count}')

