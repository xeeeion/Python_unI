count_men = int(input())
men_list= [input() for _ in range(count_men)]
result = 0
for example in set(men_list):
    cout = 0
    for name in men_list:
        if example == name:
            cout += 1
    if cout > 1:
        result += cout
print(result)