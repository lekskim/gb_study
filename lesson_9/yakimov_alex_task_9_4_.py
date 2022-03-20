class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Скорость {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        speed = self.speed
        if speed > 0:
            print(f'Машина повернула {direction}')
        else:
            print(f'Скорость {speed} км/ч, повернуть нельзя')



    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости на {self.speed - 60} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(vehicle):
    print(f"Старт {'полицейского' if vehicle.is_police else ''} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(100)
    vehicle.show_speed()
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.show_speed()
    vehicle.stop()
    vehicle.turn('направо')
    vehicle.go(40)
    vehicle.turn('направо')
    vehicle.stop()
    print('Финиш', end='\n\n')



car = Car('белый', 'Kia', False)
test_drive(car)
polo = TownCar('коричневый', 'Ford')
test_drive(polo)
veyron = SportCar('желтый', 'Lamborghini')
test_drive(veyron)
largus = WorkCar('красный', 'Tractor')
test_drive(largus)
mondeo = PoliceCar('синий', 'Geep')
test_drive(mondeo)