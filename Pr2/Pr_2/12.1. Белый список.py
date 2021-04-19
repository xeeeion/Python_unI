list = []
for i in range(int(input())):
    list.append(input())
check = []
for j in range(int(input())):
    check.append(input())
for k in check:
    if k in list:
        print(k)
