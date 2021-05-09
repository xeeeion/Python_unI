def golden_ratio(i):
    fi = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    j = abs(len(fi) - i)
    for n in range(i):
        if i > len(fi):
            for cc in range(j + 1):
                fi.append(fi[-2] + fi[-1])
    print(fi[i] / fi[i - 1])
golden_ratio(4)