data = []
for i in range(int(input())):
    string = input().split(",")
    data.append(string)
for i in range(int(input())):
    red = [int(i) for i in input().split(",")]
    d = data[red[0]]
    word = d[red[1]]
    print(word)
