import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input8.txt")
inp = a.data

convert = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

len_to_dig = dd(set)
for x, value in convert.items():
    len_to_dig[len(value)].add(x)

# print(len_to_dig)
p1 = 0
p2 = 0
unique_lens = {2, 4, 3, 7}
for line in a.lines:
    key = dd(set)
    pat, out = line.split(" | ")
    pat = pat.split(" ")
    out = out.split(" ")
    for o in out:
        if len(o) in unique_lens:
            p1 += 1
    for two_letters in pat:
        key[tsorted(two_letters)] |= ( len_to_dig[len(two_letters)])
    # printd(key)
    f = {
        1: [x for x in key if len(x) == 2][0],
        7: [x for x in key if len(x) == 3][0],
        4: [x for x in key if len(x) == 4][0],
        8: [x for x in key if len(x) == 7][0],
    }

    f[9] = [x for x in key if len(n := set(f[8]) - set(x)) == 1 and not (n) < set(f[4])][0]
    f[6] = [x for x in key if len(n := set(f[8]) - set(x)) == 1 and (n) < set(f[1])][0]
    f[0] = [x for x in key if len(n := set(f[8]) - set(x)) == 1 and (n) < set(f[6]) & set(f[4])][0]
    f[5] = [x for x in key if len(set(f[6]) - set(x)) == 1 and set(x) < set(f[6]) ][0]
    f[3] = [x for x in key if len(set(f[9]) - set(x)) == 1 and (set(x) < set(f[9])) and set(f[1]) < set(x)][0]
    f[2] = (set(key.keys()) - set(f.values())).pop()

    r = rev_dict(f)
    t = "".join(str(r[tsorted(o)]) for o in out)
    p2 += int(t)

ans(p1)
ans(p2)
