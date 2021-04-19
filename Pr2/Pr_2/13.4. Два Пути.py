data = int(input())
fst = [int(input()) for i in range(data)]
scnd = fst[:]
train = int(input())
for i in range(train):
    bro = int(input())
    if bro == 1:
        fst[int(input())] += int(input())
    elif bro == 2:
        scnd[int(input())] += int(input())
print(*fst)
print(*scnd)
dd = 0
for i in range(len(fst)):
    if fst[i] == scnd[i]:
        dd += 1
print(dd)
