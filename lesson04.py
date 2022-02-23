# 1 Задание
def sal():
    try:
        time = float(input('количество часов: '))
        salary = int(input('зарплата в час: '))
        bonus = int(input('премия сотрудника: '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')
sal()

# 2 Задание
my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')

# 3 Задание
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# 4 Задание
my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_list = [el for el in my_list if my_list.count(el)==1]
print(new_list)

# 5 Задание
from functools import reduce
def my_func(prev_el, el):
    return prev_el * el
print(f'{reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')

# 6 Задание
from itertools import count

for el in count(2):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle
с = 0
for el in cycle("123"):
    if с > 15:
        break
    print(el)
    с += 1

# 7 Задание
from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 7:
        print(i)
        x += 1
    else:
        break