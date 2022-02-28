import sys


def filter_price(num):
    #проверка содержит ли ввод цифры '.' может мешать, ее убираем для поверки
    #есть вопрос: если булет ',' то как ее заменить на '.', что-то делал наверняка не так,
    #но так и не получлось вывести число в файл, если в записи есть запятая
    if num.replace('.', '').isdigit():
        return True
    else:
        return False


price_f = open('bakery.csv', 'a', encoding='utf-8')

# фильтруем полученные данные из консоли
price = filter(filter_price, sys.argv[1:])
# преобразуем данные из строки в число (можно даже формат float cделать, по пока не разобрался с формата вывода)
price_format = list(map(int, price))
print(*price_format, sep='\n', file=price_f)

price_f.close()
