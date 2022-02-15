def num_translate_adv(number):
    number_vocablary = {'one': 'один', 'two': 'два', 'three': 'три',
                        'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                        }
    if number.istitle():
        number = number.lower()
        return (number_vocablary[number]).capitalize()
    elif number not in number_vocablary:
        return 'None'
    else:
        return number_vocablary[number]


your_number = input('Введите ваше число прописью на англ. языке: ')
trans_result = num_translate_adv(your_number)
print(trans_result)

