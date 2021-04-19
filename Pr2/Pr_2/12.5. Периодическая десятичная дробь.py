num = int(input())
r = 1
a = []
b = []
while r not in a:
    a.append(r)
    b.append(10*r//num)
    r = 10 * r % num
print(*b[a.index(r):])
