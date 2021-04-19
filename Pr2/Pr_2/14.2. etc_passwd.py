res = [ ]
string = list(input().split(":"))
while string != ['']:
    res.append(string)
    string = list(input().split(":"))
thrd = list(input().split(";"))
for i in range(len(res)):
    if thrd.count(res[i][1]) != 0:
        print("To: ", res[i][0])
        m = res[i][4].split(",")
        print(m[0] + "," + "ваш пароль слишком простой, смените его.")
