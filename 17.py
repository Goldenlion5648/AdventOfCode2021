import sys
sys.path.append('C:/Users/cobou/Documents/Python/adventOfCodeMisc/library')
from AoCLibrary import *

a = AdventInput("input17.txt")
inp = a.data

highest = -inf
n = nums(inp)
xrange = irange(*n[:2])
yrange = irange(*n[2:4])

print(xrange)
print(yrange)
xlist = list(xrange)
ylist = list(yrange)
r = range(-100, 100)
c = 0
for tempx in range(-10, 210):
    xvel = tempx
    print("xvel",xvel)
    for tempy in range(-120, 2900):
        xvel = tempx
        yvel = tempy
        x = 0
        y = 0
        got = False
        highest_seen = -inf
        timeout = 0
        for t in range(300):
            x += xvel
            y += yvel
            if x > xlist[-1]:
                break
            if xvel > 0:
                xvel -= 1
            elif xvel < 0:
                xvel += 1
            else:
                if xvel == 0 and x not in xrange:
                    break
            if y < ylist[0]:
                break
            yvel -= 1
            highest_seen = max(highest_seen, y)
            if (x in xrange and y in yrange):
                got = True
                break
        if got:
            c += 1
            highest = max(highest, highest_seen)

ans(highest)
ans(c)