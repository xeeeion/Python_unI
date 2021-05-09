import string
import random


list = []
for i in string.ascii_uppercase:
    if i != "l" and i != "I" and i != "o" and i != "O":
        list.append(i)
        random.shuffle(list)
for j in string.ascii_lowercase:
    if j != "l" and j != "I" and i != "o" and i != "O":
        list.append(j)
        random.shuffle(list)
for k in string.digits:
    if k != "1" and k != "0":
        list.append(k)
        random.shuffle(list)

def generate_password(m):
    a = []
    for _ in range(1, m + 1):
        a.append(str(random.choice(list)))
    a = "".join(a)
    return a

def main(n, m):
    list2 = []
    for q in range(1, n + 1):
        list2.append(generate_password(m))
    return list2
print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
