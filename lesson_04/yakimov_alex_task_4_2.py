#Написать функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
# и возвращающую курс этой валюты по отношению к рублю.

import requests


def currency_rates(url, code=""):
    code = code.upper() #приводим буквы к верхнему регистру
    response = requests.get(url) #отправили запрос к сайту с курсами
    if response.ok: #если ссылка работает, то запршиваем курс
        course = response.text.split(code)
        if len(course) == 1:
            return None
        value = course[1].split("</Value>")[0].split("<Value>")[1] #берем значение в виде строки
        value = float(value.replace(",", ".")) #преобразуем значение в float
        return value
    else:
        return None

url = 'http://www.cbr.ru/scripts/XML_daily.asp'

print((currency_rates(url, "Usd")))
print((currency_rates(url, "eUR")))
print((currency_rates(url, "GBP")))
print((currency_rates(url, "NNN")))