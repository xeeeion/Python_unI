string = input()
s = []
s1 = []
a = 0

one, all = int(string[:4]), int(string[4:])
for i in range(one):
    n = input()
    price, count, summ = int(n[0:7]), int(n[8:12]), int(n[13:18])
    if price * count != summ:
        s.append(i + 1)
    summ1 = count * price
    s1.append(summ1)
for i in s1:
    a += i
print(all - a)
for i in s:
    print(i, end=" ")

