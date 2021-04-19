i = set()
j = set()
k = int(input())
for n in range(k):
    i.add(input())
k = int(input())
for n in range(k):
    d = int(input())
    for a in range(d):
        j.add(input())
print(*sorted(i-j), sep='\n')