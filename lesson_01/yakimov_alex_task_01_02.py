#Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.

sum = 0
number = 1
sum_numbers = 0
while number <= 1000:
    #проверка на нечетность
    if number % 2 != 0:
        number_cube = number ** 3
        number_part = number_cube
    # разбивка числа на части и поиск суммы этих частей
        while number_part != 0:
            sum = sum + number_part % 10
            number_part = number_part // 10
    # далее проверяем сумма делится ли на 7
        if sum % 7 == 0:
            sum_numbers += number
            print(str(number) + '^3: ' + str(number_cube) + ' sum: ' + str(sum_numbers) + ' [' + str(sum) + ']')
        sum = 0
    number = number + 1