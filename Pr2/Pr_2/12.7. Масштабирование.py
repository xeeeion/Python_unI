lght = int(input())
wdth = int(input())
list_ = []
for i in range(lght):
    list_.append(input())
list_2 = []
for i in list_[::2]:
    list_2.append(i[::2])
lght = lght // 2
wdth = wdth // 2

for i in list_2:
    print(i)
