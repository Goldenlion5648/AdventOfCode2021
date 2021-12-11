import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input11.txt")
inp = a.data


def flash(y, x, seen):
    if (y, x) in seen:
        return
    seen.add((y, x))
    for dy, dx in adj8:
        if (y+dy, x+dx) in g:
            g[(y+dy, x+dx)] += 1
            if g[(y+dy, x+dx)] > 9:
                flash(y+dy, x+dx, seen)

def simulate(times_to_run, part2=False):
    total = 0
    for i in range(times_to_run):
        seen = set()
        for y, x in g:
            g[y, x] = int(g[y, x])
            g[y, x] += 1
        for y, x in g:
            if g[y, x] > 9:
                flash(y, x, seen)
        total += len(seen)
        for y, x in seen:
            g[y, x] = 0
        if part2 and len(seen) == len(g):
            return i + 1
    return (total)

g = grid(inp, True)
ans(simulate(100))
g = grid(inp, True)
ans(simulate(10000000, True))
