def prime(number):
    num = number
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return "Простое число" if count == 2 else "Составное число"
