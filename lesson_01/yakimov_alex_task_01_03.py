# Реализовать склонение слова "процент" во фразе "N процентов"
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 150

number = 1

while number <= 150:
    # cмотрим числа, оканчивающиеся на 1,кроме числа 11 и числа при делении на 100 имеющие остаток 11
    if number % 10 == 1 and number % 100 != 11:
        print(str(number)+' процент')
    # cмотрим числа, оканчивающиеся на 2-4,кроме числа 12, 13, 14 и числа при делении на 100 имеющие остаток 12-14
    elif 2 <= number % 10 <= 4 and number % 100 != 12 and number % 100 != 13 and number % 100 != 14:
        print(str(number) + ' процента')
    # все прочие числа
    else:
        print(str(number) + ' процентов')
    number = number + 1