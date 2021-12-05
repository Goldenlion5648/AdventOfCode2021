import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input5.txt")
inp = a.data
d = [nums(line) for line in a.lines]

def solve(p2=False):
    lap = dd(int)
    for (x1, y1, x2, y2) in d:
        if p2 and abs(y1 - y2) == abs(x1 - x2):
            x_range = range(x1, x2 + 1) if x1 < x2 else range(x1, x2-1, -1)
            y_range = range(y1, y2 + 1) if y1 < y2 else range(y1, y2-1, -1)
            for x, y in zip(x_range, y_range):
                lap[x, y] += 1

        x1, x2 = minmax(x1, x2)
        y1, y2 = minmax(y1, y2)
        if x1 == x2:
            for i in range(y1, y2 + 1):
                lap[x1, i] += 1
        if y1 == y2:
            for i in range(x1, x2 + 1):
                lap[i, y1] += 1
    return sum(1 for x in lap if lap[x] > 1)
ans(solve())
ans(solve(True))