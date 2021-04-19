"""
1 4 7
2 6
3 5
"""

num = int(input())
res = []
for i in range(num):
    res.append(input())
inn = int(input())
n = 0
print(res[0])
del res[0]
for i in range(num):
    if len(res) > n + inn - 1:
        n += inn - 1
        print(res[n])
        del res[n]
    else:
        n = 0
        if len(res) > n:
            print(res[n])
            del res[n]
