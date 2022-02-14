
employees = ['инженер-конструктор Игорь',
             'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

i = 0
for i in range(0, len(employees)):
    worker = employees[i].split()
    name = worker[-1].capitalize()
<<<<<<< HEAD
    print('Привет, %s!' % name)
    i = i + 1
=======
    print('Привет, %s!' % name)
>>>>>>> hometasks
