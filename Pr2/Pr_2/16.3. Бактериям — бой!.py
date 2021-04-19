n = int(input())
k = [[int(input()) for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    x = int(input())
    y = int(input())
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                if k[x + i][y + j] >= 8:
                    k[x + i][y + j] -= 8
                else:
                    k[x + i][y + j] = 0
            else:
                if (0 <= x + i <= n - 1) and (0 <= y + j <= n - 1):
                    if k[x + i][y + j] >= 4:
                        k[x + i][y + j] -= 4
                    else:
                        k[x + j] [y + j] = 0
for i in range(n):
    for j in range(n):
        print(k[i][j], end=" ")
    print("")