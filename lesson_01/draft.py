#Например, f(4) вернет 0,2,8,34

list = [0, 1, 1, 2, 3, 5, 8]

number = int(input('Введите число элементов последовательности'))
first = 0
second = 1
third = first + second
previous = second

for i in range(0, number + 1):
    next = previous + next
    i = i + 1
    print(i, next)


