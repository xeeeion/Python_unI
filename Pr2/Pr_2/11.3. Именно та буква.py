string = input()
n = int(input())
symbol = input()
if (0 < n <= len(string)) and (symbol in string) and (len(symbol)==1):
    print("НЕТ") if string[n] == symbol else print("ДА")
else:
    print("err")
