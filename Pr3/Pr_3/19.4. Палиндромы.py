def palindrome(s):

    string = str(s)
    if string[::-1].startswith(string):
        return "Палиндром"
    else:
        return "Не палиндром"
