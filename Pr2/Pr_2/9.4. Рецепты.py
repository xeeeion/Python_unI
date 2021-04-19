data = set()
for i in range(int(input())):
    data.add(input())
for i in range(int(input())):
    recipe = input()
    rec = set()
    for j in range(int(input())):
        rec.add(input())
    if len(rec & data) == len(rec):
        print(recipe)
