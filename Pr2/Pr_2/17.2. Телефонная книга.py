dct = {}
for _ in range (int (input ())):
    val, key = input ().split ()
    if key in dct:
        dct[key].append (val)
    else:
        dct[key] = [val]

for _ in range (int (input ())):
    key = input ()
    print(*dct.get(key, ["Нет в телефонной книге"]))
