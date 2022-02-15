def thesaurus(names):
    name_el = {}
    for i in range(0, len(names)):
        letter_key = names[i][0]
        if letter_key not in name_el:
            name_el[letter_key] = []
        name_el[letter_key].append(names[i])
    return name_el

employees_names = (input("Введи имена сотрудников через пробел:").split())
employees_names.sort()

print(thesaurus(employees_names))
