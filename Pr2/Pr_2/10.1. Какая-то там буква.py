string = input()
n = int(input())
if n > len(string) or n < 1:
    print("ОШИБКА")
else:
    print(string[n - 1])