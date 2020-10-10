#  1
from sys import argv
script_name, work, time, money = argv

def salary(work, time, money):
    return float(work)*float(time) + float(money)
print(salary(work, time, money))

#  2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [num for num in my_list if num > my_list[my_list.index(num)-1]]
print(new_list)

#  3
new_list = [num for num in range(20, 241) if num % 20 == 0 or num % 21 == 0]
print(new_list)

#  4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [num for num in my_list if my_list.count(num) == 1]
print(new_list)

#  5
from functools import reduce
my_list = [num for num in range(100, 1001) if num % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, my_list))

# 6
from itertools import count, cycle
# 6.1
num = int(input('Enter your number'))
for el in count(num):
    if el > 10:
        break
    else:
        print(el)

# 6.2
num = str(input('Enter your number'))
num_list = [int(numi) for numi in list(num)]
print(num_list)
for ind, el in enumerate(cycle(num_list)):
    if (ind > 10) and (ind % len(num_list) == 0):
        break
    print(el)

# 7
num = int(input('Enter your number'))
def calc_fact(n):
    fac = 1
    if n == 0:
        return 1
    else:
        for x in range(1, n+1):
            fac *= x
        return fac
def fact(n):
    for el in range(0, n+1):
        yield calc_fact(el)
for el in fact(num):
    print(el)
from math import factorial

# or
def fact(n):
    for el in range(0, n+1):
        yield factorial(el)
for el in fact(num):
    print(el)