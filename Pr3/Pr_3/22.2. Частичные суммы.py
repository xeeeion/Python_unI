def partial_sums(*k):
    sums = [0]
    for i, x in enumerate(k):
        sums.append(x + sums[i])
    return sums

print(partial_sums(1, 0.5, 0.25, 0.125))
