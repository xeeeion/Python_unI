num = int(input())

m2 = False
sl = False
char = 0
res = []

for i in range(num):
    string = input()
    while string[char] == " ":
        res.append(" ")
        char += 1
    for n in range(char, len(string)):
        if not sl:
            if string[n] == " ":
                res.append(string[n])
                m2 = not m2
            elif string[n] == "\\":
                res.append(string[n])
                sl = True
            elif string[n] == "#":
                if m2:
                    res.append(string[n])
                else:
                    break
            elif string[n] == " ":
                if m2:
                    res.append(string[n])
                else:
                    if n + 1 != len(string):
                        if string[n + 1] == "":
                            res.append("")
                        else:
                            res.append(string[n])
            else:
                res.append(string[n])
        else:
            sl = False
            res.append(string[n])
    print("".join(res))
    res = []
    m2 = False
    sl = False
    char = 0
