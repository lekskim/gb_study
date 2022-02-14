 # Написать функцию currency_rates(),
 # принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
 # и возвращающую курс этой валюты по отношению к рублю.
from datetime import datetime
import requests


def currency_rates_advanced(url, code=""):
    code = code.upper()  # приводим буквы к верхнему регистру
    response = requests.get(url)  # отправили запрос к сайту с курсами
    if response.ok:  # если ссылка работает, то запрашиваем курс
        course = response.text.split(code)
        date = response.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        if len(course) == 1:
            return date, None
        value = course[1].split("</Value>")[0].split("<Value>")[1] #берем значение в виде строки
        value = float(value.replace(",", ".")) #преобразуем значение в float

        return (date, value)
    else:
        return None



url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print((currency_rates_advanced(url, "Usd")))
print((currency_rates_advanced(url, "eUR")))
print((currency_rates_advanced(url, "GBP")))
print((currency_rates_advanced(url, "NNN")))