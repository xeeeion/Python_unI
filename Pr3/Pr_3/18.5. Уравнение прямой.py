def equation(a, b):
    x1 = float(a.split(";")[0])
    y1 = float(a.split(";")[1])
    x2 = float(b.split(";")[0])
    y2 = float(b.split(";")[1])

    if x1 == x2:
        print(x1)
    else:
        if y1 == y2:
            print(y1)
        else:
            k = (y2 - y1) / (x2 - x1)
            print(k, y2 - k * x2)