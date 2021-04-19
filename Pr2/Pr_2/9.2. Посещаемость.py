shklr = int(input())
lit = [set(input() for _ in range(int(input()))) for _ in range(shklr)]
res = lit[0]
for i in lit:
    res = res.intersection(i)
print(*sorted(res), sep="\n")
