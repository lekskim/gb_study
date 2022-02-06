#4. Обработка списка чисел.

price = [57.8, 46.40, 97, 12.3, 67.54, 8.07, 982.12, 1245.67, 4.5, 5000.00]

print(price)
for i in range(0, len(price)):  #Вывод рублей и поиск значения копеек
    rub = int(price[i] // 1)
    kop = int(price[i] * 100 % 100)
    if 0 <= kop <= 9: #Ищем значение копеек, где нужно добавить ноль
        kop = str(kop).zfill(2)
    print('{} руб {} коп, '.format(rub, kop), end="")
print(end='\n')

print('Доказательство операции in place:') #вывод id и сортировка по возрастанию
# id перед сортировкой
print('id перед сортировкой ', id(price))
price.sort()
print('id после сортировки ', id(price))
print(price)

new_price = price.copy()
new_price.reverse() #развернули список, чтобы цены были убыванию
print('id нового списка ',id(new_price))
print('5 самых дорогих товаров')
for i in range(0, 5): #выводим первые 5 значений
    print(new_price[i])