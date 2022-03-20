class Stationary:
    title = 'Drawing'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):

    def draw(self):
        self.title = 'pen'
        print(f'{self.title }: Нарисуй мне небо ручкой')


class Pencil(Stationary):

    def draw(self):
        self.title = 'pencil'
        print(f'{self.title}: Нарисуй мне солнце карандашом')


class Handle(Stationary):

    def draw(self):
        self.title = 'handle'
        print(f'{self.title}: Нарисуй мне Землю маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()