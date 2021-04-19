data = [input() for _ in range(int(input()))]
for _ in range(int(input())):
    temp = [data[int(input()) - 1] for _ in  range(int(input()))]
    data = temp
print("\n".join(data))