def func(str):
    if len(str) == 0:
        return
    list = str.split()
    new_list = []
    for i, value in enumerate(list):
        first = value[0].upper()
        word = first + value[1:-1]
        new_list.append(word)
    return ' '.join(new_list)

print(func(''))