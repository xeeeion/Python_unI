def bracket_check(test_string):
    sp = []
    flag = False
    for i in range(len(test_string)):
        if test_string[i] == "(":
            sp.append(test_string[i])
        elif test_string[i] == ")" and len(sp) == 0:
            flag = True
            break
        elif test_string[i] == ")" and sp[-1] == "(":
            del sp[-1]
    if len(sp) == 0 and not flag:
        print("YES")
    else:
        print("NO")
