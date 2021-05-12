import random, string


def generate_password(m):
    i = random.randint(1, m - 2)
    j = random.randint(1, m - i - 1)
    k = m - i - j

    list = []

    t = 0
    while t < i:
        d = random.choice(string.digits)
        if d != "0" and d != "0":
            list.append(d)
            t += 1

    t = 0
    while t < k:
        low = random.choice(string.ascii_lowercase)
        if low != "l" and low != "o":
            list.append(low)
            t += 1

    t = 0
    while t < j:
        up = random.choice(string.ascii_uppercase)
        if up != "I" and up != "0":
            list.append(up)
            t += 1

    random.shuffle(list)
    return "".join(list)

def main(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords
