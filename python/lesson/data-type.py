# # В списки [] можно положить любые данные
# list = [123, "Hello", 'World!', 56.65]
# print(list) # выводим весь список
# print(list[1])  # выводим 2 элемент
# print(list[1:3]) # выводим со 2 по 3 элемент
# print(list[1:]) # выводим со 2 элемента до конца
#
# # кортеж ()
# tuple = (123, "Hello", 'World!', 56.65)
# print(tuple)
#
# # словарь {}
# dict = {'hello' : 'привет', 5 : 'пять'}
# print(dict)
# print(dict[5])
# print(dict['hello'])
#
# dict['apple'] = 'яблоко'
# print(dict.keys())
# print(dict.values())

# # множества {}
# st = {'5', 7, 8.5}
# print(st)   # нарушает очередность элементов при выводе
# print(type(st))
#
# # преобразование типов данных
# # str
# a = input('Введите А: ')
# b = input('Введите B: ')
# print(a + b)
#
# # int
# a = int(input('Введите А: '))
# b = int(input('Введите B: '))
# print(a + b)
#
# # float
# a = float(input('Введите А: '))
# b = float(input('Введите B: '))
# print(a + b)
#
# # float > int
# a = float(input('Введите А: '))
# b = float(input('Введите B: '))
# print(int(a + b))
#
# # str > list
# user_inp = input("Введите слово: ")
# user_inp_list = list(user_inp)
# print(user_inp_list) # смотрим что у нас в списке
#
# first_letter = user_inp_list[0]
# print(first_letter) # получаем первый элемент списка


st = str(list({'5', 7, 8.5, 0, 7, 5}))
print(st)   # нарушает очередность элементов при выводе
print(type(st))
print(st[0])
