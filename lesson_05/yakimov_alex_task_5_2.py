def iterator_yield(n):
    for i in range(1, n + 1, 2):
        yield i


number = 10
gen1 = iterator_yield(number)
for i in range(0, number):
    print(next(gen1))
