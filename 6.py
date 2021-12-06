import sys

# from numpy import positive
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input6.txt")
inp = a.data

x = nums(inp)

def simulate(times):
    new = Counter(x)
    for _ in range(times):
        temp = Counter()
        for p in new:
            if p - 1 == -1:
                temp[6] += new[p]
                temp[8] += new[p]
            else:
                temp[p-1] += new[p]
        # print(temp)
        new = temp.copy()

    ans(sum(new.values()))
simulate(80)
simulate(256)

#OLD PART 1
# for j in range(256):
#     i = 0
#     stop = len(x)
#     while 0 <= i < stop:
#         x[i] -= 1
#         if x[i] == -1:
#             x[i] = 6
#             x.append(8)
#         i += 1
#     print(j, len(x))
# ans(len(x))