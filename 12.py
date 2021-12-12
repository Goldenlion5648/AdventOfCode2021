import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input12.txt")
inp = a.data


G = dd(list)
for line in a.lines:
    d, c = line.split("-")
    G[d].append(c)
    G[c].append(d)


def part1():
    fringe = deque([("start", ["start"])])
    seen = {}
    paths = set()

    while fringe :
        cur, seen = fringe.popleft()
        if cur == "end":
            paths.add(tuple(seen))
            continue
        counts = Counter(seen)
        for x in G[cur]:
            if x != "start":
                if x.isupper() or (counts[x] == 0):
                    fringe.append((x, seen + [x]))

    return len(paths)

def part2():
    fringe = deque([("start", ["start"], False)])
    seen = {}
    paths = set()

    while fringe :
        cur, seen, used_up = fringe.popleft()
        if cur == "end":
            paths.add(tuple(seen))
            continue
        counts = Counter(seen)
        for x in G[cur]:
            if x != "start":
                if x.isupper() or (used_up and counts[x] == 0) or not used_up:
                    fringe.append((x, seen + [x], used_up or (x.islower() and counts[x] == 1)))
    return len(paths)

ans(part1())
ans(part2())
