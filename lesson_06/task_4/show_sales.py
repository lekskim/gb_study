import sys

show_f = open('bakery.csv', 'r', encoding='utf-8')

def read_f(start=-1, end=-1):
    # если интервал начинается не с 1 элемента
    if start > 0:
        for i in range(start - 1):
            show_f.readline()
    # для правильного вывода интервала с окончанием
    if end > 0:
        for i in range(abs(end - start) + 1):
            yield show_f.readline().replace("\n", "")
    # если пользователь не вводит интервал, тогда выводится весь список цен
    else:
        for el in show_f:
            yield el.replace("\n", "")


start_pos = -1
end_pos = -1
# считываем цифру начала отрезка
if len(sys.argv) >= 2 and sys.argv[1].isdigit():
    start_pos = int(sys.argv[1])
# считываем цифру конца отрезка
if len(sys.argv) == 3 and sys.argv[2].isdigit():
    end_pos = int(sys.argv[2])
# отправляем данные в функцию для выгрузки списка цен
for line in read_f(start_pos, end_pos):
    print(int(line))

show_f.close()
