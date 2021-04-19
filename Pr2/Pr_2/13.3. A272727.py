a = [0]
n = int(input())
for i in range(n):
    b = 0
    for f in range(len(a)):
        if a[f] == a[-1 - f]:
            b += 1
    a.append(b)
del a[-1]
for i in a:
    print(i)
