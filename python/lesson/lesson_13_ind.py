# with open('1.py', 'r', encoding='UTF8') as file:
#     text = file.read()
# print(text)

#—------------------------------- Задача —--------------------------------#
'''дан файл, в каждой строке которого содержится стоимость товара.
Найти самый дорогой товар, самый дешевый товар и общую сумму покупки.'''
import json

# with open('prices.txt', 'r') as f:
#     prices = f.readlines() # получим список ['line1', line2', ...]
# print(prices, type(prices)) # ['100\n', '200\n', ...]
# prices_integer = []
# for price in prices:
#     print(prices, type(prices))
#     prices_integer.append(int(price))
# print(prices_integer, type(prices_integer))
# print(f'max: {max(prices_integer)} | min: {min(prices_integer)} | sum: {sum(prices_integer)}')

#—------------------------------- Задача —--------------------------------#
'''дан файл, в каждой строке которого содержится фамилия человека.
Найти всех людей фамилия, которых начинается на К (кириллица)'''

# with open('names.txt', 'r', encoding='utf8') as file:
#     names = file.readlines()
# print(names)
# otvet = []
# for i, name in enumerate(names):
#     if name[0] == 'К' or name[0] == 'к':
#        if i == len(name) - 1:
#            otvet.append(name)
#            print(name)
           # решить!


#—------------------------------- Задача —--------------------------------#
'''дан JSON файл. Напиши CLI для получение информации о товаре. ПРИМЕР файла
{
    "название": "Смартфон",
    "цена": 500,
    "категория": "Электроника"
}'''
import json
with open('products.json', 'r', encoding='utf-8') as f:
    product = json.load(f)
    print(product, type(product))
while True:
    command = input('''
    1. узнать название товара
    2. узнать цену
    3. узнать категорию
    4. выход
    ''')
    match command:
        case '1':
            print(product['название'])
        case '2':
            print(product['цена'])
        case '3':
            print(product['категория'])
        case '4':
            break



