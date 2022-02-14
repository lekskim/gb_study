from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number, noun, adverb, adjective):
    jokes = []
    for i in range(0, number):
        rd_id = randrange(len(nouns))
        noun = nouns[rd_id]
        rd_id = randrange(len(adverbs))
        adverb = adverbs[rd_id]
        rd_id = randrange(len(adjectives))
        adjective = adjectives[rd_id]
        jokes.append(' '.join([noun.capitalize(), adverb, adjective]))
        number = jokes
    return (number)

number_jokes = int(input("Введите количество шуток: "))
result = get_jokes(number_jokes, nouns, adverbs, adjectives)
print(result)