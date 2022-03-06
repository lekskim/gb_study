import os.path


def memory(way):
    # Проверка существования пути
    if not os.path.exists(way):
        return
    folder = os.scandir(way)
    for docs in folder:
        if os.path.isfile(docs):  # файл существует, тогда считаем его размер
            size_mem = 10 ** len(str(os.stat(docs).st_size))
            size[size_mem] = size.get(size_mem, 0) + 1
        elif os.path.isdir(docs):  # при иных: перезапускаем функцию
            memory(os.path.join(way, docs))


size = {}
memory(os.getcwd())
print(size)
