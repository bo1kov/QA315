'''
Помогите Алексу собрать нужное количество монет для покупки подарка.
Вначале у Алекса нет монет.
Каждый день он может найти случайное количество монет от 1 до 5.
Подарок стоит 50 монет.
Программа должна симулировать процесс сбора монет до тех пор,
пока у Алекса не окажется достаточно монет для покупки подарка
и сообщить, сколько дней это заняло.
'''

# from random import randint # импорт функции randint из модуля random.
# # Можно импортировать полностью модуль random, но тогда надо будет обращаться
# # к нужной функции через random и точку. Вот так: random.randint(...)
# balance_coins = 0 # в начале нет монет
# random_count_coins = 0 # сюда будем записывать случайное кол-во монет
# price_gift = 50 # подарок стоит 50 монет
# days = 0 # кол-во дней
#
# while balance_coins < price_gift:
#     random_count_coins = randint(1, 5)
#     balance_coins += random_count_coins
#     days += 1
#     # print(f'Дни: {days}') # отладочный принт
#     # print(f'Текущий баланс: {balance_coins}') # отладочный принт
#     # print(f'Случайные монеты {random_count_coins}')
# print(f'Ура! Собрали на подарок {balance_coins} монет. Вам потребовалось {days} дней')


#--------------------------- Задача -----------------------------#
'''
Напишите программу, в которой компьютер "загадывает число от 1 до 100,
а пользователь пытается его угадать. Пользователь вводит числа до тех пор,
пока не угадывает правильное число. Как только число будет угадано,
программа должна вывести количество попыток, которые потребовались
для угадывания числа.
'''
# from random import randint
# random_num = randint(1, 100)
# user_num = None
# number_attempts = 0
# while random_num != user_num:
#     print('Сгенерировано случайное число от 1 до 100')
#     user_num = int(input("Попробуй его угадать: "))
#     if user_num < random_num:
#         print('Больше')
#         number_attempts += 1
#     elif user_num > random_num:
#         print('Меньше')
#         number_attempts += 1
#     else:
#         number_attempts += 1
#         print('##################################')
#         print(f'Ура! Ты угадал число {random_num}')
#         print(f'Количество попыток - {number_attempts}')
#         print('##################################')
#         break


'''
Теперь попробуем поднять накал и решить обратную задачу. 
Создадим программу которая "загадывает число от 1 до 100 
и даёт 5 попыток чтобы угадать его.
'''
from random import randint
random_num = randint(1, 100) # рандомное число
num_attempts = 5 # количество попыток
print('Сгенерировано случайное число от 1 до 100')
while num_attempts > 0:
    user_num = int(input(f'Осталось попыток {num_attempts}, соберись: '))
    if user_num < random_num:
        print('Больше')
        num_attempts -= 1
    elif user_num > random_num:
        print('Меньше')
        num_attempts -= 1
    else:
        print('##################################')
        print(f'Ура! Ты угадал число {random_num} :)')
        print('##################################')
        break
else:
    print('Не получилось :(')

