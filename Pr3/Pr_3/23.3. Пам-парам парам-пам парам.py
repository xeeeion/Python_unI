data = str(input())
big_data = data.split()

print(big_data)

lst = [sum(x in "уеыаоэяию" for x in data) for data in big_data]

if len(set(lst)) == 1:
    res = ""