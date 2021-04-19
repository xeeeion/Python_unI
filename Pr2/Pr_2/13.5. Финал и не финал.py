data = int(input())
res = []
for i in range(data):
    res.append((input(),int(input())))

list_length = len(res)
for i in range(list_length - 1):
    for j in range(list_length - i - 1):
        if res[i][1] > res[j+1][1]:
            res[j], res[j+1] = res[j+1], res[j]

avg_list = list_length // 2
final = res [ avg_list :]
first = res [: avg_list ]

m = len(final)
for i in range(list_length - 1):
    for j in range(m - i - 1):
        if final[i] > final[j+1]:
            final[j], final[j+1] = final[j+1], final[j]
for i in final:
    print(i[0])

m = len(first)
for i in range(m-1):
    for j in range(m-i-1):
        if first[j] > first[j+1]:
            first[j], first[j+1] = first[j+1], first[j]

for i in first:
    print(i[0])
