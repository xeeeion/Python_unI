stri = input()
count = 0
for i in stri:
    if i != ' ' and i != '\t':
        count += 1
print(count)