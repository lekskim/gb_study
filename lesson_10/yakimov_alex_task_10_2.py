class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def consumption_coat(self):
        return self.width / 6.5 + 0.5

    def consumption_costume(self):
        return self.height * 2 + 0.3

    @property
    def consumption_total(self):
        return str(f'Общий расход ткани \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_coat}'


class Costume(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_costume = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_costume}'


c1 = Coat(12, 1)
c2 = Coat(1, 1)
c3 = Coat(121, 1)
print(c1.consumption_total)
print(c2.consumption_total)
print(c3.consumption_total)
print(c1.consumption_coat())
print(c2.consumption_coat())
print(c3.consumption_coat())

