def num_translate(number):
    number_vocablary = {'one': 'один', 'two': 'два', 'three': 'три',
                        'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
                        }
    if number not in number_vocablary:
        return 'None'
    else:
        return number_vocablary[number]


your_number = input('Введите ваше число прописью на англ. языке: ')
k = num_translate(your_number)
print(k)

