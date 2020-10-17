#  1
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# 2

class Road:
    def __init__(self):
        self._length = 20
        self._width = 5000

    def mass_cov(self, mass, rel):
        return self._length * self._width * mass * rel


roadE95 = Road()
roadE95._length = 20
roadE95._width = 5000
print(f'Необходимая масса асфальта, т: {int(roadE95.mass_cov(25, 5) / 1000)}')


# 3
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.position = 'researcher'
        self._income = {"wage": 1000, "bonus": 10000}


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


man1 = Position('Petr', 'Petrov', 'goodworker', {'wage': 200, 'bonus': 2000})
print(man1.name)
print(man1.surname)
print(man1.position)
print(man1._income)
print(man1.get_total_income())
print(man1.get_full_name())


# 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        if self.speed > 0:
            print('Машина поехала')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        if direction == 'направо':
            print('повернула направо')
        elif direction == 'налево':
            print('повернула налево')

    def show_speed(self):
        print(self.show_speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 60:
            return 'Превышение скорости'
        else:
            return 'Все в порядке'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            return 'Превышение скорости'
        else:
            return 'Все в порядке'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

towncar_1 = TownCar(70, 'red', 'BMW', False)
workcar_1 = WorkCar(35, 'blue', 'Lexus', False)
policecar_1 = PoliceCar(0, 'Black', 'LADA', True)

towncar_1.go()
print(f'{towncar_1.name} {towncar_1.color} {towncar_1.speed} км/ч - {towncar_1.show_speed()}')
towncar_1.turn("направо")

workcar_1.go()
print(f'{workcar_1.name} {workcar_1.color} {workcar_1.speed} км/ч - {(workcar_1.show_speed())}')
workcar_1.turn("налево")

print(f'{policecar_1.name} {policecar_1.color} {policecar_1.speed} км/ч')
policecar_1.stop()


# 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки.'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск отрисовки маркер'


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
print(pen.title, pen.draw())
print(pencil.title, pencil.draw())
print(handle.title, handle.draw())
