# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования ** лямбд, filter, map, zip, enumerate, list comprehension
# 3 Исправленные задачи на Отлично!
# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Пример:

# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
from re import I
from tkinter.ttk import Separator
from os import sep
n = int(input('Введите n'))
my_dict = {x: 3*x+1 for x in range(1, n+1)}  # list comprehension
print(my_dict)

print('***********************************************')

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите n:\n'))
# res = 1
# for i in range(1, n+1):
#     res = res*i
#     i += 1
#     print(res, end=',') for


n = int(input('Введите n:\n'))
res = []
res = [res[-1]
       for i in range(1, n+1) if not res.append(i*res[-1] if res else 1)]

print(res)
print('*******************************************************************')


def mygenerator():
    res = 1
    i = 1
    while True:
        res *= i
        yield res
        i += 1


n = int(input('Введите n:\n'))
factorial = mygenerator()
res = [next(factorial) for i in range(n)]
print(res)
print('*********************************************************')
