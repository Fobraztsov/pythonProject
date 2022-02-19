# 1 задание
def my_func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return "y не может равняться нулю"
    except ValueError:
        return "вводите только число"


print(my_func(int(input("Enter x = ")), int(input("Enter y = "))))

# 2
def my_f(name, age, city, email, phone):
    result = name + ', ' + age + ' лет, проживает в городе ' + city, email, phone
    return result
name = input('введите имя: ')
age = input('введите возраст: ')
city = input('введите название города: ')
email = input('введите электронную почту: ')
phone = input('введите номер телефона: ')
print(my_f(name, age, city, email, phone))

# 3 задание
def my_func(x, y, z):
    sequence = [x, y, z]
    total = []
    max_1 = max(sequence)
    total.append(max_1)
    sequence.remove(max_1)
    max_2 = max(sequence)
    total.append(max_2)
    print(sum(total))
my_func(-4, 2, 0)

# 4 задание
def my_func(x, y):
    return x ** y

print(my_func(2, -3))

# 5 задание
total = 0
while True:
    userinput = input('Input numbers or Q for quit - ').split()
    try:
        total += sum(map(int, userinput))
        print(total)
    except ValueError:
        break

# 6 задание
def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()
