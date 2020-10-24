#1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def ext(cls, day_month_year):
        new_date = []

        for i in day_month_year.split('-'):
            if i != '-': new_date.append(i)

        return int(new_date[0]), int(new_date[1]), int(new_date[2])

    @staticmethod
    def val(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return 'right'
                else:
                    return 'wrong'
            else:
                return 'wrong'
        else:
            return 'wrong'
    def __str__(self):
        return f'Текущая дата {Data.ext(self.day_month_year)}'

my = Data('24-10-2020')
print(my.ext('24-10-2020'))

print(Data.ext('24-10-2020'))
print(my.val(24, 10, 2020))
print(Data.val(24, 10, 2020))


# 2
class ZeroDivisionEr(Exception):

    def __init__(self, txt):
        self.txt = txt
divider = int(input('didiver:'))
denominator = int(input('denominator:'))
try:

    if denominator == 0:
        raise ZeroDivisionEr('Divide by zero')
    else:
        print(divider / denominator)
except ZeroDivisionEr as err:
    print(err)


# 3
class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt

num_ls = []
while True:
    inp = input('Введите число: ')
    if inp == 'stop':
        break
    try:
        if inp.replace('.', '').isdigit() == False:
            raise OwnException('Вы ввели не число :(')
        else:
            num_ls.append(int(inp))
    except OwnException as err:
        print(err)
    else:
        print('Число добавлено в список. Для остановки программы введите "stop"')
print(f'Введённые числа: {num_ls}')


# 4 - 6
class Storage:
    def __init__(self, width, height, volume, item):
        self.width = width
        self.height = height
        self.volume = volume
        self.item = item

    def get_equipment(self, name, num):
        eq_dict = {}
        try:
            int(num)
            eq_dict.update({name: num})
            return eq_dict
        except ValueError:
            return 'Вы ввели не число'

    def move_eq(self, name_eq, num_eq, name_dep):
        dep_eq = {}
        try:
            int(num_eq)
            dep_eq.update({name_dep: {name_eq: num_eq}})
            return dep_eq
        except ValueError:
            return 'Вы ввели не число'


class OfficeEquipment():
    def __init__(self, cost, size, sid):
        self.cost = cost
        self.size = size
        self.sid = sid


class Scaner(OfficeEquipment):
    def __init__(self, square):
        super().__init__(cost, size, sid)
        self.square = square


class Printer(OfficeEquipment):
    def __init__(self, speed):
        super().__init__(cost, size, sid)
        self.speed = speed


class Xerox(OfficeEquipment):
    def __init__(self, cost, size, sid, ip):
        super().__init__(cost, size, sid)
        self.ip = ip


st = Storage(20, 20, 30, 40)
print(st.get_equipment('printer', 2))
print(st.move_eq('printer', 2, 'Dean'))

print(st.get_equipment('printer', 'dva'))
print(st.get_equipment('printer', 2))
print(st.move_eq('printer', 'tri', 'Dean'))

# 7
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.a + other.a} + {self.b + other.b} * i'
    def __mul__(self, other):
        if self.b * other.a + self.a * other.b < 0:
            return f'Произведение комплексных чисел: {self.a * other.a - (self.b * other.b)} - {abs(self.b * other.a + self.a * other.b)} * i'
        else:
            return f'Произведение комплексных чисел: {self.a * other.a - (self.b * other.b)} + {self.b * other.a + self.a * other.b} * i'

z_1 = Complex(2, -2)
z_2 = Complex(5, 4)

print(z_1 + z_2)
print(z_1 * z_2)

