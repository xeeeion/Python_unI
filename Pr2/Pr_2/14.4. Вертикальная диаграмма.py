inp = list(map(int, input().split()))
xMax = len(inp)
yMax = max(inp)

print('*' * (xMax + 2))
print('*' + ' ' * xMax + '*')
for i in range(1, yMax + 1):
    print(end='*')
    for n in inp:
        if n >= yMax - i + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')
