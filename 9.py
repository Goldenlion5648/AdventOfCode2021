import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input9.txt")
inp = a.data
class R:
    def __init__(self) -> None:
        self.val = 0

c = 0
a = a.lines
starts = []
for y in range(len(a)):
    for x in range(len(a[y])):
        if all(a[y][x] < a[y+dy][x+dx] for dy, dx in adj if y + dy in range(len(a)) and x + dx in range(len(a[y]))):
            c += int(a[y][x])  + 1
            starts.append((y, x))
ans(c)

fringe = deque()
for y, x in starts:
    fringe.append(((y, x), set(), R()))
seen = {}
a = grid(inp, True)
groups = set()
all_seen = set()
# print(a)
dp =dd(int)
while fringe:
    cur, seen, ref = fringe.popleft()
    y, x = cur
    if cur in seen:
        continue
    seen.add(cur)
    dp[y, x] = ref
    ref.val = max(ref.val, len(seen))
    added = False
    for dy, dx in adj:
        if (y + dy,x+dx) in a and a[y + dy,x+dx] > a[y, x] and a[y + dy,x+dx] != "9" :
            fringe.append(((y+dy, x+dx), seen, ref))
            added = True

seen = set()
sizes = []
for x in dp.values():
    if x in seen:
        continue
    seen.add(x)
    sizes.append(x.val)
ans(prod(sorted(sizes)[-3:]))
