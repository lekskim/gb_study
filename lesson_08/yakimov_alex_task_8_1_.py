import re

address = re.compile(r"(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)")
msg = 'wrong email'


def email_parse(email):
    try:
        dict_user = list(map(lambda x: x.groupdict(), address.finditer(email)))
        print(dict_user[0])
    except:
        raise ValueError(f'{msg}: {email}')
