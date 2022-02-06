
forcast = ['примерно в', '10', 'часов', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']

print(forcast)
i = 0
while i < len(forcast):
    # Проверка на наличие цифр
    if forcast[i].isdigit() or forcast[i][1:].isdigit():
        # Проверка на наличие знака (в зависимости от наличия знака добавляем ноль)
        if forcast[i][0] == '+' or forcast[i][0] == '-':
            forcast[i] = forcast[i][0] + forcast[i][1:].zfill(2)
        else:
            forcast[i] = forcast[i].zfill(2)
        # Добавили ноль, если элемент цифра, то добавляем кавычки слева и справа
        forcast.insert(i, '"')
        forcast.insert(i + 2, '"')
        i = i + 2
    i = i + 1
print(forcast)

# Слепили список в строку
final = ' '.join(forcast)
i = 0
# Выводим по 1 элементу, пробелы между цифрой и кавычкой убираем (уверен, что можно гораздо проще, но не придумал)
while i < len(final):
    if (final[i] == '"' and (final[i + 2].isdigit() or final[i + 2] == '+' or final[i + 2] == '-')) or (final[i].isdigit() and final[i + 2] == '"'):
        print(final[i], end="")
        i = i + 1
    else:
        print(final[i], end="")
    i = i + 1

