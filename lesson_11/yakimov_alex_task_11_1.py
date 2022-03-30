class Date:

    def __init__(self, date: str):
        self.d = date

    def __str__(self):
        self.day, self.month, self.year = Date.translate(self.d)
        if (self.month // 10 == 0 and self.day // 10 == 0):
            result = f'{self.year}.0{self.month}.0{self.day}'
        elif self.month // 10 == 0:
            result = f'{self.year}.0{self.month}.{self.day}'
        elif self.day // 10 == 0:
            result = f'{self.year}.{self.month}.0{self.day}'
        else:
            result = f'{self.year}.{self.month}.{self.day}'
        return result

    @staticmethod
    def correct(date: str):
        day: int
        month: int
        year: int

        try:
            day, month, year = Date.translate(date)
        except:
            return f'{date}, Неверный формат даты'

        if not 1 <= month <= 12:
            return f'{date}, Неверно указан месяц'

        if not 0 <= year:
            return f'{date}, Неверно указан год'

        if not 1 <= day <= 31:
            return f'{date}, Неверно указан день'

        # конец месяца
        if month in [4, 6, 9, 11] and day == 31:
            return f'{date}, Неверный формат даты'

        # Февраль
        if (
                month == 2 and
                day == 29 and
                year % 4 != 0 and
                year % 100 != 0 and
                year % 400 != 0
        ):
            return f'{date} Неверный формат даты'
        return f'{date}, Формат даты корректный'


    @classmethod
    def translate(cls, date: str):
        try:
            return(list(map(int, date.split("-"))))
        except:
            raise ValueError('Преобразование невозможно')



if __name__ == '__main__':
    d = Date('03-12-2010')
    print(f'Формат даты: {d}')
    print(d.correct('03-12-2010'))
    z = Date('45-01-2444')
    print(f'Формат даты: {z}')
    print(z.correct('45-01-2444'))
    y = Date('12-12&##x2013;2022')
    #print(f'Формат даты: {y}') в этом случае ошибка, запутался, как добавить исключение в цикл
    print(y.correct('12-12&##x2013;2022'))