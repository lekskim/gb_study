def iterator_without_yield(n):
    item = (i for i in range(1, n + 1, 2))
    return item


number = 10
gen1 = iterator_without_yield(number)
for i in range(0, number):
    print(next(gen1))

