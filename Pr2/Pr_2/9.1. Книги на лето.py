in_home_books = int(input())
for_school_books = int(input())
wbooks = []
for i in range(in_home_books):
    wbooks.append(input())
for j in range(for_school_books):
    a = input()
    if a in wbooks:
        print("YES")
    else:
        print("NO")
