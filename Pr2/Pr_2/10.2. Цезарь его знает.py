n = int(input())
string = input()

for i in string:
    if ord(i) >= 1101:
        i = chr(ord(i) - (32 - n))
    else:
        i = chr(ord(i) + n)
    print(i,end="")
