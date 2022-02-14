
# 1 Задание
my_list = [10, None, -5, 'True', True, 3.2]

def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return


my_type(my_list)

# 2 Задание
element_count = int(input("Введите число элементов списка "))
my_list = []
i = 0
element = 0
while i < element_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[element], my_list[element + 1] = my_list [element + 1], my_list[element]
        element += 2
print(my_list)

#3 Задание
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца "))
if month ==12 or month == 1 or month == 2:
        print(seasons_list[0])
        print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])
    print(seasons_dict.get(4))

#4 Задание
my_str = input("Напишите фразу: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}  {el}")

#5 Задание
number = int(input("Введите число: "))
my_list = [7, 4, 3, 2]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i+a, number)
        break
    else:
        if number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)