from datetime import datetime
import requests


def currency_rates(code="", url='http://www.cbr.ru/scripts/XML_daily.asp'):
    code = code.upper()  # приводим буквы к верхнему регистру
    response = requests.get(url)  # отправили запрос к сайту с курсами
    if response.ok:  # если ссылка работает, то запршиваем курс
        course = response.text.split(code)
        if len(course) == 1:
            return None
        value = course[1].split("</Value>")[0].split("<Value>")[1]  # берем значение в виде строки
        value = float(value.replace(",", "."))  # преобразуем значение в float
        return value
    else:
        return None


def currency_rates_advanced(code="", url='http://www.cbr.ru/scripts/XML_daily.asp'):
    code = code.upper()  # приводим буквы к верхнему регистру
    response = requests.get(url)  # отправили запрос к сайту с курсами
    if response.ok:  # если ссылка работает, то запрашиваем курс
        course = response.text.split(code)
        date = response.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        if len(course) == 1:
            return date, None
        value = course[1].split("</Value>")[0].split("<Value>")[1]  # берем значение в виде строки
        value = float(value.replace(",", "."))  # преобразуем значение в float

        return date, value
    else:
        return None
