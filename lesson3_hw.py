# author = Миллионщикова Татьяна Дмитриевна
# 1
var_1 = int(input())
var_2 = int(input())
def first_func(var_1, var_2):
    try:
        result = var_1 / var_2
        return result
    except ZeroDivisionError:
        return 'На 0 делить нельзя'

print(first_func(var_1, var_2))

# 2
def param(name, surname, year, city, email, mobile):
    return ' '.join([name, surname, year, city, email, mobile])
print(param(input('enter name'), input('enter surname'), input('enter year'), input('enter city'), input('enter email'), input('enter mobile')))
# 3
def my_func(x_1, x_2, x_3):
    if x_1 >= x_3 and x_2 >= x_3:
        return x_1 + x_2
    elif x_1 >= x_2 and x_3 >= x_2:
        return x_1 + x_3
    else:
        return x_2 + x_3


print(f'Сумма наибольших двух аргументов: {my_func(int(input()), int(input()), int(input()))}')

# 4
def my_func(x, y):
    if x >= 0 and y < 0:
        return x ** y
    else:
        print('не удовлетворяет условию')


print(my_func(int(input()), int(input())))

#  5
import sys

result = 0
while True:
    line = input("Введите число или стопслово: ")
    stroka = line.split(" ")
    for i in stroka:
        try:
            number = float(i)
            result += number
        except:
            if i == 'q':
                print(f"Сумма чисел: {result}. Программа окончена")
                exit(0)
            else:
                print(f"Сумма чисел: {result}. Число введено некорректно", file=sys.stderr)
                exit(1)
print(result)


#  6
# 6.1
def int_func(a):
    return a.title()


print(int_func(input()))

# 6.2

def my_func(a):
    separate_word = a.split(' ')
    total = []
    for i in separate_word:
        string_element = str(i)
        first_letter = string_element[:1].upper()
        word = first_letter + string_element[1:]
        total.append(word)
    return total
print(my_func(input()))



