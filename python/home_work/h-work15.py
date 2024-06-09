'''
Сделайте функцию, которая параметром будет принимать букву и проверять, это буква кириллицы или латиницы.
'''

def is_cyrillic_or_latin(letter):
    if letter.isalpha():
        if letter.isascii():
            return 'Это латиница'
        else:
            return 'Это кириллица'
    else:
        return 'Это не буква'
msg = is_cyrillic_or_latin(input('Введите букву: '))
print(msg)