def classmates(name, room):
    number_of_room = len(name) - len(room)
    if number_of_room != 0:
        room_for_gen = room.copy()
        for n in range(0, number_of_room):
            room_for_gen.append(None)
    item = ((name[i], room_for_gen[i]) for i in range(0, len(name)))

    return item


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена', 'Елизавета', 'Марк'
        ]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
        ]

gen = classmates(tutors, groups)
for j in range(0, len(tutors)):
    print(next(gen))