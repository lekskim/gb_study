class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def value(self, weight_asphalt, thikness):
        result = self._length * self._width * weight_asphalt * thikness // 1000
        print(f'{self._length} м * {self._width} м * {weight_asphalt} кг * {thikness} см = {result} тонн')


road_weight = Road(20, 5000)
road_weight.value(25, 5)