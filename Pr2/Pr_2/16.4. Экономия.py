n = int (input())
res = [[]]

for i in range (n - 1):
    res.append ([int (j) for j in input ().split ()])

station = input().split()
a, b = int(station[0]), int(station[1])

l = res[max (a, b)][min (a, b)]
c = -1

for i in range (n):
    if i != a and i != b:
        if (l > res[max (a, i)][min (a, i)] + res[max (i, b)][min (i, b)]):
            l = res[max (i, b)][min (i, b)] + res[max (i, b)][min (i, b)]
            c = i

if c != -1:
    print (c)
else:
    print (a)
