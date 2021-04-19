count = []
list = []
for i in range(int(input())):
    count.append(input())
    list.append(int(input()))
for i in range(len(list)):
    print(count[len(count) - 1 - i],
          list[len(list) - 1 - i])

