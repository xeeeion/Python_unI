import math


def range(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step

def dist(d):
    return math.hypot(0.75 - d[0], 0 - d[1])

coord = [(math.cos(3 * d),
          math.sin(3 * d))
         for d in range(0,2 * 3.14,0.1)]


dist = [round(dist(x), 4) for x in coord]
print(min(dist))