stri = input()
count = input().split()
for i in count:
    if stri.upper() in i or stri.lower() in i:
        print(i)