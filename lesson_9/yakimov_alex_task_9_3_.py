class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


employee = Position('Alexander', 'Yakimov', 'specialist', 50, 40)
print(f'Атрибуты: {employee.name}, {employee.surname}, {employee.position}, {employee._income}')
print(f'Общий доход: {employee.get_total_income()} тыс. руб.')