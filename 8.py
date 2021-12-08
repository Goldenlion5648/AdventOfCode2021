import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input8.txt")
inp = a.data

c = 0
seen = Counter()
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
for x in convert:
    len_to_dig[len(convert[x])].add(x)
p1 = 0
lens = {2, 4, 3, 7}
scores = dd(lambda : dd(int))
for line in a.lines:
    f = {}
    key = dd(set)
    pat, out = line.split(" | ")
    pat = pat.split(" ") 
    out = out.split(" ") 
    seen = set()
    for p in pat:
        key[tsorted(p)] |= ( len_to_dig[len(p)])
    # printd(key)
    f[1] = [x for x in key if len(x) == 2][0]
    f[7] = [x for x in key if len(x) == 3][0]
    f[4] = [x for x in key if len(x) == 4][0]
    f[8] = [x for x in key if len(x) == 7][0]
    f[9] = [x for x in key if len(set(f[8]) - set(x)) == 1 and (set(f[8]) - set(x)).pop() not in f[4]][0]
    f[6] = [x for x in key if len(set(f[8]) - set(x)) == 1 and (set(f[8]) - set(x)).pop() in f[1]][0]
    f[0] = [x for x in key if len(set(f[8]) - set(x)) == 1 and (set(f[8]) - set(x)).pop() in set(f[6]) & set(f[4])][0]
    # temp = set(f[8]) ^ set(x)
    f[5] = [x for x in key if len(set(f[6]) - set(x)) == 1 and set(x) < set(f[6]) ][0]
    f[3] = [x for x in key if len(set(f[9]) - set(x)) == 1 and (set(x) < set(f[9])) and set(f[1]) < set(x)][0]
    f[2] = (set(key.keys()) - set(f.values())).pop()
    # print(key)
    # print(f[4])
    # print(f)
    r = rev_dict(f)
    t = ""
    for o in out:
        t += str(r[tsorted(o)])
    c += int(t)

    
    # break
    for o in out:
        # print(set(o))
        if len(o) in lens:
            p1 += 1
        # for x in convert:
        #     if set(convert[x]) == set(o) and x in [1,4,7,8]:
        #         p1 += 1
            

ans(p1)
ans(c)
