string = input()
i = 0
k = 0
mx = 0
for n in string:
    if n == 'о' and k == 0:
        i += 1
    elif n == 'о' and k != 0:
        i = 1
        k = 0
    else:
        k = 1
    if i > mx:
        mx = i
print(mx)

