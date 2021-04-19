stri = input()
stri = stri.upper()
counter = 0
for i in range(0, len(stri)):
    if stri.count(stri[i]) > counter: counter = stri.count(stri[i])
print(counter)
