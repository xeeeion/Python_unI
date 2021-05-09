import string
import random


list = []
for i in string.ascii_letters:
    if i != "l" and i != "I" and i != "o" and i != "O":
        list.append(i)
        random.shuffle(list)
for j in string.digits:
    if j != "1" and j != "0":
        list.append(j)
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

print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")