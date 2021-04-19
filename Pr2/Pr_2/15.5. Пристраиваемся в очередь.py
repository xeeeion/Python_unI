queue = []
for i in range(int(input())):
    string = input()
    if "хватит тут стоять" in string:
        string = string.split(", ")
        queue.pop(queue.index(string[0]))
    elif "будет за тобой" in string:
        string = string.split("! ")
        string_a, string_b = string[1].split(" будет"), string[0].split(", ")
        name_a, name = string_a[0], string_b[1]
        queue.insert(queue.index(name) + 1, name_a)
    else:
        queue.append(string.split(" в")[0])
print("\n".join(queue))