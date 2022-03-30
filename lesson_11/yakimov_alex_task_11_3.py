class NoStr(Exception):

    def __init__(self, *args: object):
        super().__init__(*args)


class CheckAndAdd:
    lst = []
    while True:
        try:
            num = input()
            if num == "stop":
                break
            elif not num.isdigit():
                raise NoStr()
            else:
                lst.append(int(num))
        except NoStr:
            print('Ошибка! Значение не является числом')

