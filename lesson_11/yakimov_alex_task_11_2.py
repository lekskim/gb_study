class ExceptionZero(Exception):

    def div_zero_func(self, a, b):
        try:
            result = round(a / b, 2)
        except ZeroDivisionError:
            print(f'{a} / {b} -> на ноль делить нельзя!')
        else:
            print(f'{a} / {b} = {result}')


number_res = ExceptionZero()

number_res.div_zero_func(1.5, 2)
number_res.div_zero_func(1, 0)
number_res.div_zero_func(-10, 3)
number_res.div_zero_func(0.5, 4)
