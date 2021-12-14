import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input14.txt")
inp = a.data

inserts = {}
for line in a.lines:
    if "->" in line:
        w, e = line.split(" -> ")
        inserts[w] = w[0] + e + w[1]
    else:
        if line:
            start = line


counts = Counter([start[i:i+2] for i in range(len(start) -1 )])
assert all(len(x) == 2 for x in counts)
for i in range(1, 41):
    temp = Counter()
    for two_letters in counts:
        if two_letters in inserts:
            assert len(two_letters) == 2
            temp[(inserts[two_letters][:2])] += counts[two_letters]
            temp[(inserts[two_letters][1:])] += counts[two_letters]
    counts = temp.copy()

    if i in [10, 40]:
        total = Counter()
        for two_letters in counts:
            total[two_letters[0]] += counts[two_letters]
    
        total[start[-1]] += 1
        ans(max(total.values()) - min(total.values()))