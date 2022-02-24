import json

users = open('task_3_users.csv', 'r', encoding='utf-8')
hobby = open('task_3_hobby.csv', 'r', encoding='utf-8')
name = []
users_hobby = []

# преобразуем данные из файла users и выделением ФИО
for line in users:
    line = line.split(',')
    line = line[0][0]+line[1][0]+line[2][0]
    name.append(line)

users.close()

# преобразуем данные из файла hobby в список с заменой не нужных нам элементов
for line in hobby:
    users_hobby.append(line.replace('\n', '').replace(',', ';'))

hobby.close()

# позаимствовал ваш код с прошлого урока, и немного изменил для двух списков с формированием словаря
result = dict((name[i], users_hobby[i] if i < len(users_hobby) else None) for i in range(len(name)))
print(result)

with open('task_3_result.txt', 'w') as f:
    json.dump(result, f)
