'''Создайте функцию, которая принимает список и элемент,
и возвращает индекс этого элемента в списке (если он есть),
или сообщение о его отсутствии.'''

def index_elements():
    element = None
    elements = []
    while element != 'x' or element != 'X' or element != 'х' or element != 'Х':
        element = input()
        elements.append(element)
    return elements