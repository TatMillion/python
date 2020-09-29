# author = Миллионщикова Татьяна Дмитриевна
# 1
a_1 = input('Введите имя')
a_2 = input('Введите фамилию')
b = int(input('Сколько вам сейчас лет'))
print(f' {a_1} {a_2}, через 5 лет вам будет {b + 5}')

# 2
s = int(input("время в секундах"))
m = int(s / 60)
sec = s % 60  # сколько секунд в остатке
hours = int(m / 60)  # сколько часов
minutes = m % 60  # сколько минут
if sec < 10:
    sec = '0' + str(sec)
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)
print(f'{hours}:{minutes}:{sec}')
# вар.2 print('%s:%s:%s' % (hours, m, s))
# вар.3 print('{}:{}:{}'.format(hours, m, s))
# Вопрос. не нужно ли в данном случае знак целочисленного деления использовать '//'?

# 3
n = input()
y = n * 2  # or y = n + n
z = n * 3  # or z = n + n + n
print(int(n) + int(y) + int(z))

# 4
number = int(input())
max_number = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_number:
        max_number  = number % 10
    number = number // 10
print(max_number)

# 5
v = int(input('значение выручки'))
i = int(input('значение издержек'))
if v > i:
    p = (v - i) / v
    print(f'Финансовый результат - прибыль, рентабельность выручки: {p:.2f}')
    pop = int(input('Численость сотрудников:'))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {p / pop:.2f}')
else:
    print('Финансовый результат - убыток')

# 6
a = int(input())
b = int(input())
day = 1
while a < b:
    a = a + a * 0.1
    day = day + 1
print(day)
