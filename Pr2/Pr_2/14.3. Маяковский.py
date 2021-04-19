import re


stri = input()
stri2 = re.sub(r'\s+', '\n', stri)
print(stri2)
